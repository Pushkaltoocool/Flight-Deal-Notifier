import requests

class DataManager:
    def __init__(self):
        # Store the full flight data as a list of dictionaries
        self.flight_data = []

    def get_data(self):
        # Fetch data from the Sheety API
        url = "your own google sheet"
        response = requests.get(url)
        sheet_data = response.json()
        self.flight_data = sheet_data["prices"]