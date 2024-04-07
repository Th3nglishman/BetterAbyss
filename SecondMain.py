import requests
from Champion import Champion

class SecondMain:
    i = 1
    while i < 154:
        headers = {
            'accept': 'application/json',
            'Authorization': 'Basic cmlvdDprRmMtWEJQdzRNVGtSWTB0T0RILVRn'
        }
        api_call = requests.get(self.api_url_champion_selected + str(i), None, headers=headers)
        i += 1
        print(api_call)


