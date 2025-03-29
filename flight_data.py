from flight_search import FlightSearch
from datetime import datetime  # Import datetime for formatting

class FlightData:
    def __init__(self):
        self.fs = FlightSearch("2025-06-13")
        self.fs.fetch_flights()
        self.flights = self.fs.get_flights()

    def return_formatted_flights(self):
        """
        Return flights grouped by destination city with full route details, including departure date.
        """
        # Group flights by destination city
        flights_by_city = {}
        for flight in self.flights:
            city = flight["to_city"]
            if city not in flights_by_city:
                flights_by_city[city] = []
            flights_by_city[city].append(flight)

        # Format the output
        result = []
        for city, flights in flights_by_city.items():
            flight_details = []
            for flight in flights:
                # Parse and format the departure date for readability
                raw_date = flight["departure_date"]
                formatted_date = datetime.fromisoformat(raw_date.replace("Z", "+00:00")).strftime("%B %d, %Y %H:%M")
                # Include departure date in the output
                detail = (
                    f"{flight['flight_route']}, Airline: {flight['airline']}, "
                    f"Price: {flight['price']} SGD, Departure: {formatted_date} \n\n"
                )
                flight_details.append(detail)
            result.append(f"Flights to {city}: {', '.join(flight_details)}")
        return "\n".join(result)