import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

LEAGUE_URLS = {
    "Premier League": ["https://fbref.com/en/comps/9/","Premier-League-Stats"],
    "Bundesliga": ["https://fbref.com/en/comps/20/","Bundesliga-Stats"],
    "LaLiga": ["https://fbref.com/en/comps/12/","La-Liga-Stats"],
    "Serie A": ["https://fbref.com/en/comps/11/","Serie-A-Stats"],
    "Ligue 1": ["https://fbref.com/en/comps/13/", "Ligue-1-Stats"]
}

STATS = {
    "stats": ["player", "nationality"]
}


def getTable(url):
    res = requests.get(url)
    comm = re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("",res.text),'lxml')
    allTables = soup.findAll("tbody")
    playerTable = allTables[2]
    print(playerTable)
    return playerTable

def getFrame(category, playerTable):
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

def categoryFrame(category, url):
    url = (url[0] + category + url[1])
    playerTable = getTable(url)
    dfPlayer = getFrame(category, playerTable)
    return dfPlayer

def getPlayerData(url):
    df1 = categoryFrame("stats", url)
    # TODO add stats to STATS and call all here
    df = pd.concat([df1], axis=1)
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


if __name__ == "__main__":
    leagues = ["Premier League"]
    seasons = [2021]
    scraper = FBrefScraper(leagues, seasons)
    outfieldStats = scraper.scrapePlayers("players.csv")
