import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from pymongo import MongoClient
from copy import deepcopy
from time import sleep

# URLs of Top 5 European Leagues, the second string is concatenated with the season and
# stat we are looking for
LEAGUE_URLS = {
    "Premier League": ["https://fbref.com/en/comps/9/","Premier-League-Stats"],
    "Bundesliga": ["https://fbref.com/en/comps/20/","Bundesliga-Stats"],
    "LaLiga": ["https://fbref.com/en/comps/12/","La-Liga-Stats"],
    "Serie A": ["https://fbref.com/en/comps/11/","Serie-A-Stats"],
    "Ligue 1": ["https://fbref.com/en/comps/13/", "Ligue-1-Stats"]
}

# Stats to be scraped from FBref.com, key is the category, value is a list of stat names to be pulled
STATS = {
    "stats": ["player", "nationality", "position", "team", "age", "birth_year", "games", "games_starts", "minutes", "minutes_90s", "goals", "assists", "goals_assists", "goals_pens", "pens_made", "pens_att", "cards_yellow", "cards_red", "xg", "npxg", "xg_assist", "npxg_xg_assist", "progressive_carries", "progressive_passes", "progressive_passes_received", "goals_per90", "assists_per90", "goals_assists_per90", "goals_pens_per90", "goals_assists_pens_per90", "xg_per90", "xg_assist_per90", "xg_xg_assist_per90", "npxg_per90", "npxg_xg_assist_per90"],
    "shooting": ["minutes_90s", "goals", "shots", "shots_on_target", "shots_on_target_pct", "shots_per90", "shots_on_target_per90", "goals_per_shot", "goals_per_shot_on_target", "average_shot_distance", "shots_free_kicks", "pens_made", "pens_att", "xg", "npxg", "npxg_per_shot", "xg_net", "npxg_net"],
    "passing":["passes_completed", "passes", "passes_pct", "passes_total_distance", "passes_progressive_distance", "passes_completed_short", "passes_short", "passes_pct_short", "passes_completed_medium", "passes_medium", "passes_pct_medium", "passes_completed_long", "passes_long", "passes_pct_long", "assists", "xg_assist", "pass_xa", "xg_assist_net", "assisted_shots", "passes_into_final_third", "passes_into_penalty_area", "crosses_into_penalty_area", "progressive_passes"],
    "passing_types": ["passes", "passes_live", "passes_dead", "passes_free_kicks", "through_balls", "passes_switches", "crosses", "throw_ins", "corner_kicks", "corner_kicks_in", "corner_kicks_out", "corner_kicks_straight", "passes_completed", "passes_offsides", "passes_blocked"],
    # goal and shot creation
    "gca": ["sca", "sca_per90", "sca_passes_live", "sca_passes_dead", "sca_take_ons", "sca_shots", "sca_fouled", "sca_defense", "gca", "gca_per90", "gca_passes_live", "gca_passes_dead", "gca_take_ons", "gca_shots", "gca_fouled", "gca_defense"],
    "defense": ["tackles", "tackles_won", "tackles_def_3rd", "tackles_mid_3rd", "tackles_att_3rd", "challenge_tackles", "challenges", "challenge_tackles_pct", "challenges_lost", "blocks", "blocked_shots", "blocked_passes", "interceptions", "tackles_interceptions", "clearances", "errors"],
    "possession": ["touches", "touches_def_pen_area", "touches_def_3rd", "touches_mid_3rd", "touches_att_3rd", "touches_att_pen_area", "touches_live_ball", "take_ons", "take_ons_won", "take_ons_won_pct", "take_ons_tackled", "take_ons_tackled_pct", "carries", "carries_distance", "carries_progressive_distance", "progressive_carries", "carries_into_final_third", "carries_into_penalty_area", "miscontrols", "dispossessed", "passes_received", "progressive_passes_received"],
    "misc": ["cards_yellow", "cards_red", "cards_yellow_red", "fouls", "fouled", "offsides", "crosses", "interceptions", "tackles_won", "pens_won", "pens_conceded", "own_goals", "ball_recoveries", "aerials_won", "aerials_lost", "aerials_won_pct"]
}

# This will be removed for final version, this is our connection string to mongoDB
CONNECTIONSTRING = r"mongodb+srv://anduarielsivansteven:aass123!@ballondor.csw3klm.mongodb.net/?retryWrites=true&w=majority"


def categoryFrame(category, url):
    """Returns a dataframe of a given category"""
    def getTable(url):
        """Returns the table containing player stats"""
        res = requests.get(url)
        comm = re.compile("<!--|-->")
        soup = BeautifulSoup(comm.sub("",res.text),"lxml")
        allTables = soup.findAll("tbody")
        playerTable = allTables[2]
        return playerTable

    def getFrame(category, playerTable):
        """Returns a dataframe of a given category, from the
        table containing player stats"""
        dfDict = {}
        features = STATS[category]
        rows = playerTable.find_all("tr")
        for row in rows:
            if row.find("th",{"scope":"row"}):
                for f in features:
                    cell = row.find("td",{"data-stat": f})
                    if not cell:
                        text = 'NaN'
                    else:
                        text = cell.text.strip().encode().decode("utf-8")
                    if (text == ''):
                        text = '0'
                    if f in dfDict:
                        dfDict[f].append(text)
                    else:
                        dfDict[f] = [text]
        playerdf = pd.DataFrame.from_dict(dfDict)
        return playerdf
    
    url = url[0] + category + url[1]
    print(url)
    playerTable = getTable(url)
    dfPlayer = getFrame(category, playerTable)
    return dfPlayer

def getPlayerData(url):
    """Returns a dataframe of all stats for players in a given league"""
    dfStats = categoryFrame("stats", url)
    dfShooting = categoryFrame("shooting", url)
    dfPassing = categoryFrame("passing", url)
    dfPassingTypes = categoryFrame("passing_types", url)
    dfGCA = categoryFrame("gca", url)
    dfDefense = categoryFrame("defense", url)
    dfPossession = categoryFrame("possession", url)
    dfMisc = categoryFrame("misc", url)
    df = pd.concat([dfStats, dfShooting, dfPassing, dfPassingTypes, dfGCA, dfDefense, dfPossession, dfMisc], axis=1)
    df = df.loc[:,~df.columns.duplicated()]
    return df

class FBrefScraper:
    def __init__(self, leagues, seasons):
        self.leagues = leagues
        self.seasons = seasons
    
    def scrapePlayers(self, csvPath=None):
        """Scrapes player data from FBref.com and writes to a given csv file.
        returns a dataframe of player data, for every league."""
        count = 0
        outfieldStats = pd.DataFrame()
        for season in self.seasons:
            for league in self.leagues:
                count += 1
                # FBref blocks scraping more than 20 times in a minute, so we sleep for a minute every 20 scrapes
                if count == 20:
                    sleep(60)
                    count = 0
                print(f"Scraping {league}, {season - 1}/{season}...")
                url = deepcopy(LEAGUE_URLS[league])
                url[0] = f"{url[0]}{season - 1}-{season}/"
                url[1] = f"/{season - 1}-{season}-{url[1]}"
                outfieldStatsLeague = getPlayerData(url)
                outfieldStatsLeague["season"] = season
                outfieldStats = outfieldStats._append(outfieldStatsLeague, ignore_index=True)
        if csvPath:
            outfieldStats.to_csv(csvPath, index=False)
        return outfieldStats     


def addCSVToMongoDB(csvPath, connectionString, collectionName="BallondOrPredictor",dbName="FootballPredictor"):
    """Adds csv data to a mongoDB database"""
    client = MongoClient(connectionString)
    db = client[dbName]
    collection = db[collectionName]
    df = pd.read_csv(csvPath)
    data = df.to_dict(orient='records')
    collection.insert_many(data)


def clearMongoDB(connectionString, collectionName="BallondOrPredictor",dbName="FootballPredictor"):
    """Clears a mongoDB database"""
    client = MongoClient(connectionString)
    db = client[dbName]
    collection = db[collectionName]
    collection.delete_many({})

FBrefScraper(["Premier League", "Bundesliga", "LaLiga", "Serie A", "Ligue 1"], [2023, 2022, 2021, 2020, 2019, 2018]).scrapePlayers("outfieldData.csv")
addCSVToMongoDB("outfieldData.csv", CONNECTIONSTRING)