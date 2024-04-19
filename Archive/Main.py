import requests
from Champion import Champion

location_in_file = 0
wiki_data_file = "empty string"
champ_count = 0
champ_array = []
api_port = None
password = None
protocol = None


class Main:
    summoner_name = 'TheEnglishman'
    puuid = 0
    api_key = "RGAPI-8efc58c9-a7c3-4f73-885a-25e3afa175a6"  # needs to be refreshed each day
    api_url_account = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    api_url_challenges = "https://na1.api.riotgames.com/lol/challenges/v1/player-data/"
    api_url_active_game = "https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"
    api_url_champion_selected = "https://127.0.0.1:65406/lol-champ-select/v1/grid-champions/"

    def __init__(self):
        #win = Window()
        self.read_lockfile()
        self.call_api()

    def call_api(self):

        global wiki_data_file
        self.api_url_account = self.api_url_account + self.summoner_name + '?api_key=' + self.api_key
        api_call = requests.get(self.api_url_account)
        player_info = api_call.json()
        print(repr(player_info))
        #self.puuid = player_info["puuid"]
        player_id = player_info.get("id")
        #self.api_url_challenges = self.api_url_challenges + self.puuid + '?api_key=' + self.api_key
        api_call = requests.get(self.api_url_challenges)
        challenge_info = api_call.json()
        self.api_url_active_game = self.api_url_active_game + player_id + '?api_key=' + self.api_key
        api_call = requests.get(self.api_url_active_game)
        game_info = api_call.json()
        print(game_info)
        print(self.api_url_active_game)
#        champ_id = game_info["gameId"]

        print(player_info)
        print(self.puuid)
        print(challenge_info)
#        print(champ_id)

        wiki_data_file = BootyfulSoup.get_webpage_html()
        self.crawl()

        i = 1
        while i < 154:
            headers = {
                'accept': 'application/json',
                'Authorization': 'Basic cmlvdDprRmMtWEJQdzRNVGtSWTB0T0RILVRn'
            }
            api_call = requests.get(self.api_url_champion_selected+str(i), None, headers=headers)
            i += 1
            print(api_call)

    def crawl(self):
        global wiki_data_file
        try:
            while self.find('["id"]'):
                try:
                    if wiki_data_file.index(
                            '["aram"]', location_in_file) < wiki_data_file.index('["id"]', location_in_file):
                        loc = location_in_file
                        self.print_titles(self, loc)
                        self.find('["aram"]')
                        testing = wiki_data_file.index("}", location_in_file)
                        #print(str(location_in_file)+" "+str(testing))
                        result = wiki_data_file[location_in_file:testing]
                        print(result)
                        print("")
                    else:
                        self.find("}")
                except ValueError:
                    print("No aram found on last of file")

        except ValueError:
            print("End File Read")

    @staticmethod
    def print_titles(self, location):
        global champ_array
        global location_in_file
        loc = location_in_file
        self.find('["apiname"]')
        location = (location_in_file-loc)+location
        loc = location_in_file
        start = wiki_data_file.index('"', location)
        end = wiki_data_file.index('"', start+1)
        name = wiki_data_file[start+1:end]
        print(name)
        self.find('["title"]')
        location = (location_in_file-loc)+location
        loc = location_in_file
        start = wiki_data_file.index('"', location)
        end = wiki_data_file.index('"', start+1)
        title = wiki_data_file[start+1:end]
        print(title)
        champ_array.append(Champion(name, title, " "))
        return

    @staticmethod
    def find(string_target):
        global location_in_file
        if wiki_data_file.index(string_target, location_in_file) != -1:
            loc = wiki_data_file.index(string_target, location_in_file)
            location_in_file = loc+len(string_target)
            temp = wiki_data_file[loc:location_in_file]
            return True
        return False

    def read_lockfile(self):
        file_path = "example.txt"  # Replace "example.txt" with the path to your file
        try:
            with open(file_path, "r") as file:
                # Read the contents of the file
                file_contents = file.read()
                # Print the contents
                print(file_contents)
        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Error reading the file.")


