
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