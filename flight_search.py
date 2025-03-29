import requests
from data_manager import DataManager
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class FlightSearch:
    def __init__(self, departure_date="2025-06-13"):
        self.origin = "SIN"
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.departure_date = departure_date
        self.flights_available = []
        self.flights_number_per_country = []
        self.dm = DataManager()
        self.dm.get_data()
        self.flight_data_list = self.dm.flight_data

    def fetch_flights(self):
        """
        Fetch flight offers from the Amadeus API for each destination.
        """
        for flight in self.flight_data_list:
            headers = {
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json"
            }
            params = {
                "originLocationCode": self.origin,
                "destinationLocationCode": flight["iataCode"],
                "departureDate": self.departure_date,
                "adults": 1,
                "currencyCode": "SGD",
                "maxPrice": flight["lowestPrice"]
            }
            flight_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
            response = requests.get(flight_url, headers=headers, params=params)

            if response.status_code == 200:
                data = response.json()
                self._process_flights(data, flight)
            else:
                print(f"Error fetching flights for {flight['city']}: {response.status_code} {response.text}")

    def _process_flights(self, data, flight_data):
        """
        Process the API response to extract flight details.
        """
        flight_count = data["meta"]["count"]
        self.flights_number_per_country.append(flight_count)  # Store actual count, not boolean
        if flight_count > 0:
            for flight_offer in data["data"]:
                itinerary = flight_offer["itineraries"][0]
                segments = itinerary["segments"]

                # Extract airline from the first segment
                carrier_code = segments[0]["carrierCode"]
                airline = data["dictionaries"]["carriers"].get(carrier_code, "Unknown Airline")

                # Build the full flight route including all segments
                flight_route = [segments[0]["departure"]["iataCode"]]  # Start with first departure
                for segment in segments:
                    flight_route.append(segment["arrival"]["iataCode"])  # Add each arrival
                    combined_route = " to ".join(flight_route)

                # Extract the total price
                price = flight_offer["price"]["total"]

                # Extract departure date from the first segment (adjust key if necessary)
                departure_date = segments[0]["departure"]["at"]

                # Extract available seats (using a default if key is not present)
                seats_left = flight_offer.get("numberOfBookableSeats", "N/A")

                # Store flight details with additional date and seats left
                self.flights_available.append({
                    "flight_route": combined_route,
                    "to_city": flight_data["city"],
                    "airline": airline,
                    "price": price,
                    "departure_date": departure_date,
                   "seats_left": seats_left
                })

    def get_flights(self):
        """
        Return the list of available flights.
        """
        return self.flights_available