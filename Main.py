import requests
import sys

from Champion import Champion

# api_url_champion_selected = "https://127.0.0.1:65406/lol-champ-select/v1/grid-champions/"
LCU = None
exceptions = None

def main():
    # win = Window()
    api_url_champion_selected = None
    # self.read_lockfile()
    setup_api()
    # call_api()

# class Main:




def setup_api():
    global LCU, exceptions

    sys.path.append('.')
    from lcuapi import LCU
    from lcuapi import exceptions

    # Create the LCU object. Make sure the client is open on your computer.
    lcu = LCU()

    # Optionally attach `EventProcessor` classes to handle incoming events. See usage.py
    # lcu.attach_event_processor(...)

    lcu.wait_for_client_to_open()
    lcu.wait_for_login()

    # Open a background thread and listen for & process incoming events
    # using the EventProcessors that were attached to the LCU (not shown here, see usage.py).
    lcu.process_event_stream()

    # Here is an example request to get data from the LCU
    finished = lcu.get('/lol-platform-config/v1/initial-configuration-complete')
    print("Has the client finished it's starting up?", finished)

    ...  # Make more requests to the LCU if you want.

    # Prevent this program from exiting so that the event stream continues to be read.
    # Press Ctrl+C (and wait for another event to get triggered by the LCU) to gracefully terminate the program.
    lcu.wait()


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

