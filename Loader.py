import sys
import urllib.request
import requests

import Control
from Champion import Champion
location_in_file = 0
wiki_data_file = "text"
champ_count = 0
champ_array = []
champion_data = None
json_data_string = None

# TODO load json into a dictionary

# get the html from the wiki page to process into champion data
def get_webpage_html():
    global wiki_data_file
    result = requests.request("GET", "https://leagueoflegends.fandom.com/wiki/Module:ChampionData/data?action=edit")
    if Control.TEST:
        print(result)
    wiki_data_file = result.text
    if wiki_data_file is None:
        print("wiki_data_file is None")
        sys.exit(-1)

# find the champion data on the wiki page
def crawl():
    global wiki_data_file, location_in_file
    get_webpage_html()
    try:
        # the while in question
        while find('["id"]'):
            try:
                parse_champ_data()
            except ValueError:
                print("No aram found on last of file")

        # read the last entry in the file
        parse_champ_data()
    except ValueError:
        print("End File Read")

    if Control.TEST:
        print(champ_array)
        for val in champ_array:
            print(val.str())
    # convert_data_to_json()
    if Control.TEST:
        x = champ_array
    return champ_array

# parse champ data
def parse_champ_data():
    global wiki_data_file, location_in_file
    if wiki_data_file.index(
            '["aram"]', location_in_file) < wiki_data_file.index('["id"]', location_in_file):
        loc = location_in_file
        print_titles(loc, True)
    else:
        loc = location_in_file
        print_titles(loc, False)

# print and save the data for each champion
def print_titles(location, aram):
    global champ_array
    global location_in_file

    loc = location_in_file
    find("= ")
    location = (location_in_file - loc) + location
    loc = location_in_file
    end = wiki_data_file.index(',', loc)
    champ_id = wiki_data_file[location:end]
    if Control.TEST:
        print(champ_id)

    loc = location_in_file
    find('["apiname"]')
    location = (location_in_file - loc) + location
    loc = location_in_file
    start = wiki_data_file.index('"', location)
    end = wiki_data_file.index('"', start + 1)
    name = wiki_data_file[start + 1:end]
    if Control.TEST:
        print(name)

    find('["title"]')
    location = (location_in_file - loc) + location
    loc = location_in_file
    start = wiki_data_file.index('"', location)
    end = wiki_data_file.index('"', start + 1)
    title = wiki_data_file[start + 1:end]
    if Control.TEST:
        print(title)

    if Control.TEST:
        a = Champion(champ_id, name, title, "some aram stuff")
    if aram:
        find('["aram"]')
        stats = wiki_data_file[location_in_file:wiki_data_file.index("}", location_in_file)]
        champ_array.append(Champion(champ_id, name, title, stats))
    else:
        champ_array.append(Champion(champ_id, name, title, "No changes"))



# find and increment the character count to the location of the target string
def find(string_target):
    global location_in_file, wiki_data_file
    loc = wiki_data_file.index(string_target, location_in_file)
    if loc != -1:
        location_in_file = loc + len(string_target)
        temp = wiki_data_file[loc:location_in_file]
        return True
    else:
        print(string_target)
    return False

# def read_json():


# turn the data scraped from the wiki into a json to be easily processed and packaged
def convert_data_to_json():
    global json_data_string
    json_data_string = '{\n"type": "champion",\n"data": { \n'
    for val in champ_array:
        # the key is champ id in the format id:<champ id>
        json_data_string = json_data_string + '{}: {}\n"name":{},\n"title":{},\n"aram":{}'.format('"id:' + val.champ_id + '"', "{", '"' + val.name + '"', '"' + val.title + '"', val.aram_data + "}\n")
        json_data_string = json_data_string + '}\n,'
    json_data_string = json_data_string.removesuffix(',')
    json_data_string = json_data_string + '\n}'
    json_data_string = json_data_string + '\n}'

    # with open('Champs.json', 'w') as f:
    #     print(json_data_string, file=f)

    #print(json_data_string)

def get_champion_array():
    x = champ_array
    return champ_array
