import time
import requests
import sys

import Loader
from Champion import Champion

# api_url_champion_selected = "https://127.0.0.1:65406/lol-champ-select/v1/grid-champions/"
# Stores the LCU variable for api interaction
LCU = None
# Allows a required library to be imported
exceptions = None
# Stores current location in the html file
location_in_file = 0

lcu_system = None

def main():
    #Loader.read_json()
    api_url_champion_selected = None
    setup_api()

def setup_api():
    global LCU, exceptions, lcu_system

    sys.path.append('.')
    from lcuapi import LCU
    from lcuapi import exceptions

    # Create the LCU object. Make sure the client is open on your computer.
    lcu_system = LCU()

    # Optionally attach `EventProcessor` classes to handle incoming events. See usage.py
    # lcu.attach_event_processor(...)

    lcu_system.wait_for_client_to_open()
    lcu_system.wait_for_login()

    # Open a background thread and listen for & process incoming events
    # using the EventProcessors that were attached to the LCU (not shown here, see usage.py).
    lcu_system.process_event_stream()

    # Here is an example request to get data from the LCU
    finished = lcu_system.get('/lol-platform-config/v1/initial-configuration-complete')
    print("Has the client finished it's starting up?", finished)



def call_api():
    global lcu_system

    i = 1

    while i < 154:
        champ_stats = lcu_system.get('/lol-champ-select/v1/grid-champions/{}'.format(i))
        pick_status = champ_stats['selectionStatus']
        #print(pick_status)
        if pick_status['pickIntented']:
            print("Pick intended on number {}".format(i))
        time.sleep(0.001)
        i += 1


# def call_api():
#
#     i = 1
#     while i < 154:
#         headers = {
#             'accept': 'application/json',
#             'Authorization': 'Basic cmlvdDprRmMtWEJQdzRNVGtSWTB0T0RILVRn'
#         }
#         api_call = requests.get(self.api_url_champion_selected + str(i), None, headers=headers)
#         i += 1
#         print(api_call)

# def read_lockfile(self):
#     file_path = "example.txt"  # Replace "example.txt" with the path to your file
#     try:
#         with open(file_path, "r") as file:
#             # Read the contents of the file
#             file_contents = file.read()
#             # Print the contents
#             print(file_contents)
#     except FileNotFoundError:
#         print("File not found.")
#     except IOError:
#         print("Error reading the file.")


if __name__ == "__main__":
    main()

