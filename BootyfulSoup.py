import urllib.request
import requests
from bs4 import BeautifulSoup


def get_soup():
    result = urllib.request.urlopen("https://leagueoflegends.fandom.com/wiki/Module:ChampionData/data?action=edit")
    return str(result.read())
