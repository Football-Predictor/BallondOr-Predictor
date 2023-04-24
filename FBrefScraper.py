import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sys, getopt
import csv

LEAGUE_URLS = {
    "Premier League": "https://fbref.com/en/comps/9/",
    "Bundesliga": "https://fbref.com/en/comps/20/",
    "La Liga": "https://fbref.com/en/comps/12/",
    "Serie A": "https://fbref.com/en/comps/11/",
    "Ligue 1": "https://fbref.com/en/comps/13/"
}
    

class FBrefScraper:
    def __init__(self, leagues, seasons):
        self.leagues = leagues
        self.seasons = seasons
    
    def scrapePlayers(self, csvPath=None):
        outfieldStats = pd.DataFrame()
        for league in self.leagues:
            for season in self.seasons:
                print(f"Scraping {league}, {season - 1}/{season}...")
                url = LEAGUE_URLS[league] + f"{season - 1}-{season}"
                # TODO implement getPlayerData
                outfieldStatsLeague = getPlayerData(url)
                outfieldStatsLeague["season"] = season
                outfieldStats = outfieldStats.append(outfieldStatsLeague, ignore_index=True)
        if csvPath:
            outfieldStats.to_csv(csvPath, index=False)
        return outfieldStats        

