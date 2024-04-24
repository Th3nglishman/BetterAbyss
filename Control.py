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
champ_array = None
lcu_system = None
TEST = False


def setup_api():
    global LCU, exceptions, lcu_system

    api_url_champion_selected = None

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
    global lcu_system, champ_array

    result = ""

    champ_array = Loader.get_champion_array()
    if TEST:
        x = champ_array
        j = 0
    i = -1

    for a in champ_array:
        if (float(a.champ_id) % 1) == 0:

            i = int(a.champ_id)
            champ_stats = lcu_system.get('/lol-champ-select/v1/grid-champions/{}'.format(i))
            pick_status = champ_stats['selectionStatus']
            for x in pick_status:
                if pick_status[x]:
                    print(x+" is true for {}".format(a.name))
            if pick_status['pickIntentedByMe']:
                result += "Your champ is {}".format(a.name)+"\n"
                result += "With aram stats: {}".format(a.aram_data)+"\n"

                if TEST:
                    print("Your champ is number {}".format(i))
                    print("Named: {}".format(a.name))
                    print("With aram stats: {}".format(a.aram_data))

            elif pick_status['pickIntented']:
                result += "Pick intended for {}".format(a.name)+"\n"
                result += "With aram stats: {}".format(a.aram_data)+"\n"

                if TEST:
                    print("Pick intended on number {}".format(i))
                    print("Named: {}".format(a.name))
                    print("With aram stats: {}".format(a.aram_data))
            if pick_status['selectedByMe']:
                result += "Your champ is {}".format(a.name)+"\n"
                result += "With aram stats: {}".format(a.aram_data)+"\n"

                if TEST:
                    print("Your champ is number {}".format(i))
                    print("Named: {}".format(a.name))
                    print("With aram stats: {}".format(a.aram_data))

            elif pick_status['pickedByOtherOrBanned']:
                result += "Pick intended for {}".format(a.name)+"\n"
                result += "With aram stats: {}".format(a.aram_data)+"\n"

            time.sleep(0.001)
            if TEST:
                j += 1
                print(j)
        else:
            if TEST:
                print(a.champ_id)
                print(a.name)

    # champ_stats = lcu_system.get('/lol-champ-select/v1/grid-champions/{}'.format(i))

    return result







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

