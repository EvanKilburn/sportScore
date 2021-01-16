from bs4 import BeautifulSoup #BeautifulSoup is in bs4 package 
import requests
import time
from datetime import datetime

def getScores(URL):
    content = requests.get(URL)
    soup = BeautifulSoup(content.text, 'html.parser')
    body = soup.find("body")
    scores = body.findAll("div", {"class": "Matchup__teamScore--2BeCA"})
    homeScore = scores[0].string
    awayScore = scores[1].string
    teams = body.findAll("div", {"class": "Matchup__teamName--vqpde"})
    homeTeam = teams[0].string
    awayTeam = teams[1].string
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Score Update @ "+dt_string+": "+homeTeam+": "+homeScore+" | "+awayTeam+": "+awayScore)

URL = input("Add the link to thescore.com sporting event you would like to watch: ")
while True:
    getScores(URL)
    time.sleep(60)
