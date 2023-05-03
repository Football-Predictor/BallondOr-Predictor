# source https://en.wikipedia.org/wiki/2022_Ballon_d%27Or
import csv
import pandas as pd
winners = {
    "Karim Benzema, 2022": [549, 1],
    "Sadio Mané, 2022": [193, 2],
    "Kevin De Bruyne, 2022": [175, 3],
    "Robert Lewandowski, 2022": [170, 4],
    "Mohamed Salah, 2022": [116, 5],
    "Kylian Mbappé, 2022": [85, 6],
    "Thibaut Courtois, 2022": [82, 7],
    "Vinicius Júnior, 2022": [61, 8],
    "Luka Modrić, 2022": [20, 9],
    "Erling Haaland, 2022": [18, 10],
    "Son Heung-min, 2022": [5, 11],
    "Riyad Mahrez, 2022": [4, 12],
    "Sébastien Haller, 2022": [2, 13],
    "Rafael Leão, 2022": [2, 14],
    "Fabinho, 2022": [2, 14],
    "Virgil van Dijk, 2022": [1, 16],
    "Casemiro, 2022": [1, 17],
    "Dušan Vlahović, 2022": [1, 17],
    "Luis Díaz, 2022": [1, 17],
    "Lionel Messi, 2021": [613, 1],
    "Robert Lewandowski, 2021": [580, 2],
    "Jorginho, 2021": [460, 3],
    "Karim Benzema, 2021": [239, 4],
    "N'Golo Kanté, 2021": [186, 5],
    "Cristiano Ronaldo, 2021": [178, 6], 
    "Mohamed Salah, 2021": [121, 7],
    "Kevin De Bruyne, 2021": [73, 8],
    "Kylian Mbappé, 2021": [58, 9],
    "Gianluigi Donnarumma, 2021": [36, 10],
    "Erling Haaland, 2021": [33, 11],
    "Giorgio Chiellini, 2021": [26, 12],
    "Romelu Lukaku, 2021": [26, 12],
    "Leonardo Bonucci, 2021": [18, 14],
    "Raheem Sterling, 2021": [10, 15],
    "Neymar, 2021": [9, 16],
    "Luis Suárez, 2021": [8, 17],
    "Simon Kjær, 2021": [8, 17],
    "Mason Mount, 2021": [7, 19],
    "Riyad Mahrez, 2021": [7, 19],
    "Bruno Fernandes, 2021": [6, 21],
    "Lautaro Martínez, 2021": [6, 21],
    "Harry Kane, 2021": [4, 23],
    "Pedri, 2021": [3, 24],
    "Phil Foden, 2021": [2, 25],
    "Gerard Moreno, 2021": [1, 26],
    "Nicolò Barella, 2021": [1, 26],
    "Rúben Dias, 2021": [1, 26],
    "Lionel Messi, 2019": [1678, 1],
    "Virgil van Dijk, 2019": [1174, 2],
    "Cristiano Ronaldo, 2019": [1038, 3],
    "Sadio Mané, 2019": [347, 4],
    "Mohamed Salah, 2019": [178, 5],
    "Kylian Mbappé, 2019": [89, 6],
    "Alisson, 2019": [67, 7],
    "Robert Lewandowski, 2019": [44, 8],
    "Bernardo Silva, 2019": [41, 9],
    "Riyad Mahrez, 2019": [33, 10],
    "Frenkie de Jong, 2019": [31, 11],
    "Raheem Sterling, 2019": [30, 12],
    "Eden Hazard, 2019": [25, 13],
    "Kevin De Bruyne, 2019": [14, 14],
    "Matthijs de Ligt, 2019": [13, 15],
    "Sergio Agüero, 2019": [12, 16],
    "Roberto Firmino, 2019": [11, 17],
    "Antoine Griezmann, 2019": [9, 18],
    "Trent Alexander-Arnold, 2019": [8, 19],
    "Pierre-Emerick Aubameyang, 2019": [5, 20],
    "Dušan Tadić, 2019": [5, 20],
    "Son Heung-min, 2019": [4, 22],
    "Hugo Lloris, 2019": [3, 23],
    "Marc-André ter Stegen, 2019": [2, 24],
    "Kalidou Koulibaly, 2019": [2, 24],
    "Karim Benzema, 2019": [1, 26],
    "Georginio Wijnaldum, 2019": [1, 26],
    "Luka Modrić, 2018": [753, 1],
    "Cristiano Ronaldo, 2018": [478, 2],
    "Antoine Griezmann, 2018": [414, 3],
    "Kylian Mbappé, 2018": [347, 4],
    "Lionel Messi, 2018": [280, 5],
    "Mohamed Salah, 2018": [188, 6],
    "Raphaël Varane, 2018": [121, 7],
    "Eden Hazard, 2018": [119, 8],
    "Kevin De Bruyne, 2018": [29, 9],
    "Harry Kane, 2018": [25, 10],
    "N'Golo Kanté, 2018": [24, 11],
    "Neymar, 2018": [19, 12],
    "Luis Suárez, 2018": [17, 13],
    "Thibaut Courtois, 2018": [12, 14],
    "Paul Pogba, 2018": [9, 15],
    "Sergio Agüero, 2018": [7, 16],
    "Gareth Bale, 2018": [6, 17],
    "Karim Benzema, 2018": [6, 17],
    "Roberto Firmino, 2018": [4, 19],
    "Ivan Rakitić, 2018": [4, 19],
    "Sergio Ramos, 2018": [4, 19],
    "Edinson Cavani, 2018": [3, 22],
    "Sadio Mané, 2018": [3, 22],
    "Marcelo, 2018": [3, 22],
    "Alisson, 2018": [2, 25],
    "Mario Mandžukić, 2018": [2, 25],
    "Jan Oblak, 2018": [2, 25],
    "Diego Godín, 2018": [1, 28]
}

leaguepositions = {'Arsenal,2023': '1', 'Manchester City,2023': '2', 'Newcastle Utd,2023': '3', 'Manchester Utd,2023': '4', 'Liverpool,2023': '5', 'Tottenham,2023': '6', 'Aston Villa,2023': '7', 'Brighton,2023': '8', 'Brentford,2023': '9', 'Fulham,2023': '10', 'Crystal Palace,2023': '11', 'Chelsea,2023': '12', 'Bournemouth,2023': '13', 'Wolves,2023': '14', 'West Ham,2023': '15', 'Leicester City,2023': '16', 'Leeds United,2023': '17', "Nott'ham Forest,2023": '18', 'Everton,2023': '19', 'Southampton,2023': '20', 'Bayern Munich,2023': '1', 'Dortmund,2023': '2', 'Union Berlin,2023': '3', 'Freiburg,2023': '4', 'RB Leipzig,2023': '5', 'Leverkusen,2023': '6', 'Wolfsburg,2023': '7', 'Mainz 05,2023': '8', 'Eint Frankfurt,2023': '9', "M'Gladbach,2023": '10', 'Köln,2023': '11', 'Werder Bremen,2023': '12', 'Augsburg,2023': '13', 'Hoffenheim,2023': '14', 'Stuttgart,2023': '15', 'Bochum,2023': '16', 'Schalke 04,2023': '17', 'Hertha BSC,2023': '18', 'Barcelona,2023': '1', 'Real Madrid,2023': '2', 'Atlético Madrid,2023': '3', 'Real Sociedad,2023': '4', 'Villarreal,2023': '5', 'Betis,2023': '6', 'Athletic Club,2023': '7', 'Girona,2023': '8', 'Osasuna,2023': '9', 'Rayo Vallecano,2023': '10', 'Sevilla,2023': '11', 'Mallorca,2023': '12', 'Celta Vigo,2023': '13', 'Almería,2023': '14', 'Cádiz,2023': '15', 'Valladolid,2023': '16', 'Valencia,2023': '17', 'Espanyol,2023': '18', 'Getafe,2023': '19', 'Elche,2023': '20', 'Napoli,2023': '1', 'Lazio,2023': '2', 'Juventus,2023': '3', 'Inter,2023': '4', 'Milan,2023': '5', 'Roma,2023': '6', 'Atalanta,2023': '7', 'Bologna,2023': '8', 'Fiorentina,2023': '9', 'Monza,2023': '10', 'Sassuolo,2023': '11', 'Torino,2023': '12', 'Udinese,2023': '13', 'Salernitana,2023': '14', 'Empoli,2023': '15', 'Lecce,2023': '16', 'Spezia,2023': '17', 'Hellas Verona,2023': '18', 'Cremonese,2023': '19', 'Sampdoria,2023': '20', 'Paris S-G,2023': '1', 'Marseille,2023': '2', 'Lens,2023': '3', 'Monaco,2023': '4', 'Lille,2023': '5', 'Rennes,2023': '6', 'Lyon,2023': '7', 'Clermont Foot,2023': '8', 'Nice,2023': '9', 'Lorient,2023': '10', 'Reims,2023': '11', 'Montpellier,2023': '12', 'Toulouse,2023': '13', 'Auxerre,2023': '14', 'Strasbourg,2023': '15', 'Nantes,2023': '16', 'Brest,2023': '17', 'Troyes,2023': '18', 'Ajaccio,2023': '19', 'Angers,2023': '20', 'Manchester City,2022': '1', 'Liverpool,2022': '2', 'Chelsea,2022': '3', 'Tottenham,2022': '4', 'Arsenal,2022': '5', 'Manchester Utd,2022': '6', 'West Ham,2022': '7', 'Leicester City,2022': '8', 'Brighton,2022': '9', 'Wolves,2022': '10', 'Newcastle Utd,2022': '11', 'Crystal Palace,2022': '12', 'Brentford,2022': '13', 'Aston Villa,2022': '14', 'Southampton,2022': '15', 'Everton,2022': '16', 'Leeds United,2022': '17', 'Burnley,2022': '18', 'Watford,2022': '19', 'Norwich City,2022': '20', 'Bayern Munich,2022': '1', 'Dortmund,2022': '2', 'Leverkusen,2022': '3', 'RB Leipzig,2022': '4', 'Union Berlin,2022': '5', 'Freiburg,2022': '6', 'Köln,2022': '7', 'Mainz 05,2022': '8', 'Hoffenheim,2022': '9', "M'Gladbach,2022": '10', 'Eint Frankfurt,2022': '11', 'Wolfsburg,2022': '12', 'Bochum,2022': '13', 'Augsburg,2022': '14', 'Stuttgart,2022': '15', 'Hertha BSC,2022': '16', 'Arminia,2022': '17', 'Greuther Fürth,2022': '18', 'Real Madrid,2022': '1', 'Barcelona,2022': '2', 'Atlético Madrid,2022': '3', 'Sevilla,2022': '4', 'Betis,2022': '5', 'Real Sociedad,2022': '6', 'Villarreal,2022': '7', 'Athletic Club,2022': '8', 'Valencia,2022': '9', 'Osasuna,2022': '10', 'Celta Vigo,2022': '11', 'Rayo Vallecano,2022': '12', 'Elche,2022': '13', 'Espanyol,2022': '14', 'Getafe,2022': '15', 'Mallorca,2022': '16', 'Cádiz,2022': '17', 'Granada,2022': '18', 'Levante,2022': '19', 'Alavés,2022': '20', 'Milan,2022': '1', 'Inter,2022': '2', 'Napoli,2022': '3', 'Juventus,2022': '4', 'Lazio,2022': '5', 'Roma,2022': '6', 'Fiorentina,2022': '7', 'Atalanta,2022': '8', 'Hellas Verona,2022': '9', 'Torino,2022': '10', 'Sassuolo,2022': '11', 'Udinese,2022': '12', 'Bologna,2022': '13', 'Empoli,2022': '14', 'Sampdoria,2022': '15', 'Spezia,2022': '16', 'Salernitana,2022': '17', 'Cagliari,2022': '18', 'Genoa,2022': '19', 'Venezia,2022': '20', 'Paris S-G,2022': '1', 'Marseille,2022': '2', 'Monaco,2022': '3', 'Rennes,2022': '4', 'Nice,2022': '5', 'Strasbourg,2022': '6', 'Lens,2022': '7', 'Lyon,2022': '8', 'Nantes,2022': '9', 'Lille,2022': '10', 'Brest,2022': '11', 'Reims,2022': '12', 'Montpellier,2022': '13', 'Angers,2022': '14', 'Troyes,2022': '15', 'Lorient,2022': '16', 'Clermont Foot,2022': '17', 'Saint-Étienne,2022': '18', 'Metz,2022': '19', 'Bordeaux,2022': '20', 'Manchester City,2021': '1', 'Manchester Utd,2021': '2', 'Liverpool,2021': '3', 'Chelsea,2021': '4', 'Leicester City,2021': '5', 'West Ham,2021': '6', 'Tottenham,2021': '7', 'Arsenal,2021': '8', 'Leeds United,2021': '9', 'Everton,2021': '10', 'Aston Villa,2021': '11', 'Newcastle Utd,2021': '12', 'Wolves,2021': '13', 'Crystal Palace,2021': '14', 'Southampton,2021': '15', 'Brighton,2021': '16', 'Burnley,2021': '17', 'Fulham,2021': '18', 'West Brom,2021': '19', 'Sheffield Utd,2021': '20', 'Bayern Munich,2021': '1', 'RB Leipzig,2021': '2', 'Dortmund,2021': '3', 'Wolfsburg,2021': '4', 'Eint Frankfurt,2021': '5', 'Leverkusen,2021': '6', 'Union Berlin,2021': '7', "M'Gladbach,2021": '8', 'Stuttgart,2021': '9', 'Freiburg,2021': '10', 'Hoffenheim,2021': '11', 'Mainz 05,2021': '12', 'Augsburg,2021': '13', 'Hertha BSC,2021': '14', 'Arminia,2021': '15', 'Köln,2021': '16', 'Werder Bremen,2021': '17', 'Schalke 04,2021': '18', 'Atlético Madrid,2021': '1', 'Real Madrid,2021': '2', 'Barcelona,2021': '3', 'Sevilla,2021': '4', 'Real Sociedad,2021': '5', 'Betis,2021': '6', 'Villarreal,2021': '7', 'Celta Vigo,2021': '8', 'Granada,2021': '9', 'Athletic Club,2021': '10', 'Osasuna,2021': '11', 'Cádiz,2021': '12', 'Valencia,2021': '13', 'Levante,2021': '14', 'Getafe,2021': '15', 'Alavés,2021': '16', 'Elche,2021': '17', 'Huesca,2021': '18', 'Valladolid,2021': '19', 'Eibar,2021': '20', 'Inter,2021': '1', 'Milan,2021': '2', 'Atalanta,2021': '3', 'Juventus,2021': '4', 'Napoli,2021': '5', 'Lazio,2021': '6', 'Roma,2021': '7', 'Sassuolo,2021': '8', 'Sampdoria,2021': '9', 'Hellas Verona,2021': '10', 'Genoa,2021': '11', 'Bologna,2021': '12', 'Fiorentina,2021': '13', 'Udinese,2021': '14', 'Spezia,2021': '15', 'Cagliari,2021': '16', 'Torino,2021': '17', 'Benevento,2021': '18', 'Crotone,2021': '19', 'Parma,2021': '20', 'Lille,2021': '1', 'Paris S-G,2021': '2', 'Monaco,2021': '3', 'Lyon,2021': '4', 'Marseille,2021': '5', 'Rennes,2021': '6', 'Lens,2021': '7', 'Montpellier,2021': '8', 'Nice,2021': '9', 'Metz,2021': '10', 'Saint-Étienne,2021': '11', 'Bordeaux,2021': '12', 'Angers,2021': '13', 'Reims,2021': '14', 'Strasbourg,2021': '15', 'Lorient,2021': '16', 'Brest,2021': '17', 'Nantes,2021': '18', 'Nîmes,2021': '19', 'Dijon,2021': '20', 'Liverpool,2020': '1', 'Manchester City,2020': '2', 'Manchester Utd,2020': '3', 'Chelsea,2020': '4', 'Leicester City,2020': '5', 'Tottenham,2020': '6', 'Wolves,2020': '7', 'Arsenal,2020': '8', 'Sheffield Utd,2020': '9', 'Burnley,2020': '10', 'Southampton,2020': '11', 'Everton,2020': '12', 'Newcastle Utd,2020': '13', 'Crystal Palace,2020': '14', 'Brighton,2020': '15', 'West Ham,2020': '16', 'Aston Villa,2020': '17', 'Bournemouth,2020': '18', 'Watford,2020': '19', 'Norwich City,2020': '20', 'Bayern Munich,2020': '1', 'Dortmund,2020': '2', 'RB Leipzig,2020': '3', "M'Gladbach,2020": '4', 'Leverkusen,2020': '5', 'Hoffenheim,2020': '6', 'Wolfsburg,2020': '7', 'Freiburg,2020': '8', 'Eint Frankfurt,2020': '9', 'Hertha BSC,2020': '10', 'Union Berlin,2020': '11', 'Schalke 04,2020': '12', 'Mainz 05,2020': '13', 'Köln,2020': '14', 'Augsburg,2020': '15', 'Werder Bremen,2020': '16', 'Düsseldorf,2020': '17', 'Paderborn 07,2020': '18', 'Real Madrid,2020': '1', 'Barcelona,2020': '2', 'Atlético Madrid,2020': '3', 'Sevilla,2020': '4', 'Villarreal,2020': '5', 'Real Sociedad,2020': '6', 'Granada,2020': '7', 'Getafe,2020': '8', 'Valencia,2020': '9', 'Osasuna,2020': '10', 'Athletic Club,2020': '11', 'Levante,2020': '12', 'Valladolid,2020': '13', 'Eibar,2020': '14', 'Betis,2020': '15', 'Alavés,2020': '16', 'Celta Vigo,2020': '17', 'Leganés,2020': '18', 'Mallorca,2020': '19', 'Espanyol,2020': '20', 'Juventus,2020': '1', 'Inter,2020': '2', 'Atalanta,2020': '3', 'Lazio,2020': '4', 'Roma,2020': '5', 'Milan,2020': '6', 'Napoli,2020': '7', 'Sassuolo,2020': '8', 'Hellas Verona,2020': '9', 'Fiorentina,2020': '10', 'Parma,2020': '11', 'Bologna,2020': '12', 'Udinese,2020': '13', 'Cagliari,2020': '14', 'Sampdoria,2020': '15', 'Torino,2020': '16', 'Genoa,2020': '17', 'Lecce,2020': '18', 'Brescia,2020': '19', 'SPAL,2020': '20', 'Paris S-G,2020': '1', 'Marseille,2020': '2', 'Rennes,2020': '3', 'Lille,2020': '4', 'Nice,2020': '5', 'Reims,2020': '6', 'Lyon,2020': '7', 'Montpellier,2020': '8', 'Monaco,2020': '9', 'Strasbourg,2020': '10', 'Angers,2020': '11', 'Bordeaux,2020': '12', 'Nantes,2020': '13', 'Brest,2020': '14', 'Metz,2020': '15', 'Dijon,2020': '16', 'Saint-Étienne,2020': '17', 'Nîmes,2020': '18', 'Amiens,2020': '19', 'Toulouse,2020': '20', 'Manchester City,2019': '1', 'Liverpool,2019': '2', 'Chelsea,2019': '3', 'Tottenham,2019': '4', 'Arsenal,2019': '5', 'Manchester Utd,2019': '6', 'Wolves,2019': '7', 'Everton,2019': '8', 'Leicester City,2019': '9', 'West Ham,2019': '10', 'Watford,2019': '11', 'Crystal Palace,2019': '12', 'Newcastle Utd,2019': '13', 'Bournemouth,2019': '14', 'Burnley,2019': '15', 'Southampton,2019': '16', 'Brighton,2019': '17', 'Cardiff City,2019': '18', 'Fulham,2019': '19', 'Huddersfield,2019': '20', 'Bayern Munich,2019': '1', 'Dortmund,2019': '2', 'RB Leipzig,2019': '3', 'Leverkusen,2019': '4', "M'Gladbach,2019": '5', 'Wolfsburg,2019': '6', 'Eint Frankfurt,2019': '7', 'Werder Bremen,2019': '8', 'Hoffenheim,2019': '9', 'Düsseldorf,2019': '10', 'Hertha BSC,2019': '11', 'Mainz 05,2019': '12', 'Freiburg,2019': '13', 'Schalke 04,2019': '14', 'Augsburg,2019': '15', 'Stuttgart,2019': '16', 'Hannover 96,2019': '17', 'Nürnberg,2019': '18', 'Barcelona,2019': '1', 'Atlético Madrid,2019': '2', 'Real Madrid,2019': '3', 'Valencia,2019': '4', 'Getafe,2019': '5', 'Sevilla,2019': '6', 'Espanyol,2019': '7', 'Athletic Club,2019': '8', 'Real Sociedad,2019': '9', 'Betis,2019': '10', 'Alavés,2019': '11', 'Eibar,2019': '12', 'Leganés,2019': '13', 'Villarreal,2019': '14', 'Levante,2019': '15', 'Valladolid,2019': '16', 'Celta Vigo,2019': '17', 'Girona,2019': '18', 'Huesca,2019': '19', 'Rayo Vallecano,2019': '20', 'Juventus,2019': '1', 'Napoli,2019': '2', 'Atalanta,2019': '3', 'Inter,2019': '4', 'Milan,2019': '5', 'Roma,2019': '6', 'Torino,2019': '7', 'Lazio,2019': '8', 'Sampdoria,2019': '9', 'Bologna,2019': '10', 'Sassuolo,2019': '11', 'Udinese,2019': '12', 'SPAL,2019': '13', 'Parma,2019': '14', 'Cagliari,2019': '15', 'Fiorentina,2019': '16', 'Genoa,2019': '17', 'Empoli,2019': '18', 'Frosinone,2019': '19', 'Chievo,2019': '20', 'Paris S-G,2019': '1', 'Lille,2019': '2', 'Lyon,2019': '3', 'Saint-Étienne,2019': '4', 'Marseille,2019': '5', 'Montpellier,2019': '6', 'Nice,2019': '7', 'Reims,2019': '8', 'Nîmes,2019': '9', 'Rennes,2019': '10', 'Strasbourg,2019': '11', 'Nantes,2019': '12', 'Angers,2019': '13', 'Bordeaux,2019': '14', 'Amiens,2019': '15', 'Toulouse,2019': '16', 'Monaco,2019': '17', 'Dijon,2019': '18', 'Caen,2019': '19', 'Guingamp,2019': '20', 'Manchester City,2018': '1', 'Manchester Utd,2018': '2', 'Tottenham,2018': '3', 'Liverpool,2018': '4', 'Chelsea,2018': '5', 'Arsenal,2018': '6', 'Burnley,2018': '7', 'Everton,2018': '8', 'Leicester City,2018': '9', 'Newcastle Utd,2018': '10', 'Crystal Palace,2018': '11', 'Bournemouth,2018': '12', 'West Ham,2018': '13', 'Watford,2018': '14', 'Brighton,2018': '15', 'Huddersfield,2018': '16', 'Southampton,2018': '17', 'Swansea City,2018': '18', 'Stoke City,2018': '19', 'West Brom,2018': '20', 'Bayern Munich,2018': '1', 'Schalke 04,2018': '2', 'Hoffenheim,2018': '3', 'Dortmund,2018': '4', 'Leverkusen,2018': '5', 'RB Leipzig,2018': '6', 'Stuttgart,2018': '7', 'Eint Frankfurt,2018': '8', "M'Gladbach,2018": '9', 'Hertha BSC,2018': '10', 'Werder Bremen,2018': '11', 'Augsburg,2018': '12', 'Hannover 96,2018': '13', 'Mainz 05,2018': '14', 'Freiburg,2018': '15', 'Wolfsburg,2018': '16', 'Hamburger SV,2018': '17', 'Köln,2018': '18', 'Barcelona,2018': '1', 'Atlético Madrid,2018': '2', 'Real Madrid,2018': '3', 'Valencia,2018': '4', 'Villarreal,2018': '5', 'Betis,2018': '6', 'Sevilla,2018': '7', 'Getafe,2018': '8', 'Eibar,2018': '9', 'Girona,2018': '10', 'Espanyol,2018': '11', 'Real Sociedad,2018': '12', 'Celta Vigo,2018': '13', 'Alavés,2018': '14', 'Levante,2018': '15', 'Athletic Club,2018': '16', 'Leganés,2018': '17', 'La Coruña,2018': '18', 'Las Palmas,2018': '19', 'Málaga,2018': '20', 'Juventus,2018': '1', 'Napoli,2018': '2', 'Roma,2018': '3', 'Inter,2018': '4', 'Lazio,2018': '5', 'Milan,2018': '6', 'Atalanta,2018': '7', 'Fiorentina,2018': '8', 'Torino,2018': '9', 'Sampdoria,2018': '10', 'Sassuolo,2018': '11', 'Genoa,2018': '12', 'Chievo,2018': '13', 'Udinese,2018': '14', 'Bologna,2018': '15', 'Cagliari,2018': '16', 'SPAL,2018': '17', 'Crotone,2018': '18', 'Hellas Verona,2018': '19', 'Benevento,2018': '20', 'Paris S-G,2018': '1', 'Monaco,2018': '2', 'Lyon,2018': '3', 'Marseille,2018': '4', 'Rennes,2018': '5', 'Bordeaux,2018': '6', 'Saint-Étienne,2018': '7', 'Nice,2018': '8', 'Nantes,2018': '9', 'Montpellier,2018': '10', 'Dijon,2018': '11', 'Guingamp,2018': '12', 'Amiens,2018': '13', 'Angers,2018': '14', 'Strasbourg,2018': '15', 'Caen,2018': '16', 'Lille,2018': '17', 'Toulouse,2018': '18', 'Troyes,2018': '19', 'Metz,2018': '20'}

df = pd.read_csv('outfieldData.csv')
df = df.drop('ballondor_points', axis=1)
df = df.drop('ballondor_position', axis=1)
print("Number of columns:", len(df.columns))
ballondor_position = []
ballondor_points = []
for row in df.iterrows():
    player = row[1][0]
    year = row[1][-2]
    key = f"{player}, {year}"
    if key not in winners:
        ballondorpos = -1
        ballondorpi = 0
    else:
        ballondorpos = winners[key][1]
        ballondorpi = winners[key][0]
    ballondor_position.append(ballondorpos)
    ballondor_points.append(ballondorpi)

df['ballondor_position'] = ballondor_position
df['ballondor_points'] = ballondor_points
df.to_csv('testing1.csv', index=False)


