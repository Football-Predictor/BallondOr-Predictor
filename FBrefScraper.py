import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# URLs of Top 5 European Leagues, the second string is concatenated with the season and
# stat we are looking for
LEAGUE_URLS = {
    "Premier League": ["https://fbref.com/en/comps/9/","Premier-League-Stats"],
    "Bundesliga": ["https://fbref.com/en/comps/20/","Bundesliga-Stats"],
    "LaLiga": ["https://fbref.com/en/comps/12/","La-Liga-Stats"],
    "Serie A": ["https://fbref.com/en/comps/11/","Serie-A-Stats"],
    "Ligue 1": ["https://fbref.com/en/comps/13/", "Ligue-1-Stats"]
}

# Stats to be scraped from FBref.com, key is the category, value is a lsit of stat names to be pulled
STATS = {
    "stats": ["player", "nationality", "position","squad","age","birth_year","games","games_starts","minutes","goals","assists","pens_made","pens_att","cards_yellow","cards_red","goals_per90","assists_per90","goals_assists_per90","goals_pens_per90","goals_assists_pens_per90","xg","npxg","xa","xg_per90","xa_per90","xg_xa_per90","npxg_per90","npxg_xa_per90"],
    "shooting": ["minutes_90s","goals","pens_made","pens_att","shots_total","shots_on_target","shots_free_kicks","shots_on_target_pct","shots_total_per90","shots_on_target_per90","goals_per_shot","goals_per_shot_on_target","xg","npxg","npxg_per_shot","xg_net","npxg_net"],
    "passing":["passes_completed","passes","passes_pct","passes_total_distance","passes_progressive_distance","passes_completed_short","passes_short","passes_pct_short","passes_completed_medium","passes_medium","passes_pct_medium","passes_completed_long","passes_long","passes_pct_long","assists","xa","xa_net","assisted_shots","passes_into_final_third","passes_into_penalty_area","crosses_into_penalty_area","progressive_passes"],
    "passing_types": ["passes","passes_live","passes_dead","passes_free_kicks","through_balls","passes_pressure","passes_switches","crosses","corner_kicks","corner_kicks_in","corner_kicks_out","corner_kicks_straight","passes_ground","passes_low","passes_high","passes_left_foot","passes_right_foot","passes_head","throw_ins","passes_other_body","passes_completed","passes_offsides","passes_oob","passes_intercepted","passes_blocked"],
    # goal and shot creation
    "gca": ["sca","sca_per90","sca_passes_live","sca_passes_dead","sca_dribbles","sca_shots","sca_fouled","gca","gca_per90","gca_passes_live","gca_passes_dead","gca_dribbles","gca_shots","gca_fouled","gca_defense"]
}


def categoryFrame(category, url):
    """Returns a dataframe of a given category"""
    def getTable(url):
        """Returns the table containing player stats"""
        res = requests.get(url)
        comm = re.compile("<!--|-->")
        soup = BeautifulSoup(comm.sub("",res.text),'lxml')
        allTables = soup.findAll("tbody")
        playerTable = allTables[2]
        return playerTable

    def getFrame(category, playerTable):
        """Returns a dataframe of a given category, from the
        table containing player stats"""
        dfDict = {}
        features = STATS[category]
        rows = playerTable.find_all('tr')
        for row in rows:
            if row.find('th',{"scope":"row"}):
                for f in features:
                    cell = row.find("td",{"data-stat": f})
                    text = cell.text.strip().encode().decode("utf-8")
                    if (text == ''):
                        text = '0'
                    if f in dfDict:
                        dfDict[f].append(text)
                    else:
                        dfDict[f] = [text]
        playerdf = pd.DataFrame.from_dict(dfDict)
        return playerdf
    
    url = (url[0] + category + url[1])
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
    df = pd.concat([dfStats, dfShooting, dfPassing, dfPassingTypes, dfGCA], axis=1)
    df = df.loc[:,~df.columns.duplicated()]
    return df

class FBrefScraper:
    def __init__(self, leagues, seasons):
        self.leagues = leagues
        self.seasons = seasons
    
    def scrapePlayers(self, csvPath=None):
        """Scrapes player data from FBref.com and writes to a given csv file.
        returns a dataframe of player data, for every league."""
        outfieldStats = pd.DataFrame()
        for league in self.leagues:
            for season in self.seasons:
                print(f"Scraping {league}, {season - 1}/{season}...")
                url = LEAGUE_URLS[league]
                url[1] = f"/{season - 1}-{season}-{url[1]}"
                outfieldStatsLeague = getPlayerData(url)
                outfieldStatsLeague["season"] = season
                outfieldStats = outfieldStats._append(outfieldStatsLeague, ignore_index=True)
        if csvPath:
            outfieldStats.to_csv(csvPath, index=False)
        return outfieldStats       
