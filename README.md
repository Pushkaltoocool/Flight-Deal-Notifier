# Flight Deals Notifier

A Python-based application that fetches flight deals from Singapore (SIN) to various destinations using the Amadeus API, formats the results, and sends them via email. The system retrieves destination data from a Sheety API, searches for flights within budget constraints, and notifies users of available options, including flight routes, airlines, prices, and departure dates.

## Features

- Fetches flight data from the Amadeus API based on predefined destinations and price limits.
- Groups flight results by destination city.
- Formats flight details (route, airline, price, and departure date) for readability.
- Sends notifications via email using Gmail's SMTP server.
- Keeps sensitive credentials secure using environment variables.

## Prerequisites

- Python 3.7+
- A Gmail account with an App Password (if using 2FA).
- An Amadeus API account with a client ID, client secret, and access token.
- Access to the Sheety API endpoint (provided in the code).

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/flight-deals-notifier.git
cd flight-deals-notifier
```

### Install Dependencies

Install the required Python packages using pip:

```bash
pip install requests python-dotenv
```

### Set Up Environment Variables

Create a `.env` file in the project root:

```bash
touch .env
```

Add the following variables to `.env` (replace with your own values):

```ini
CLIENT_ID=your_amadeus_client_id
CLIENT_SECRET=your_amadeus_client_secret
ACCESS_TOKEN=your_amadeus_access_token
EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password
RECIPIENT_EMAIL=recipient_email@gmail.com
```

*Note:* The `.env` file is ignored by `.gitignore` to keep secrets safe.

## Usage

### Run the Application

Execute the main script to fetch flight deals and send an email:

```bash
python main.py
```

### Expected Output

The script will fetch flight data for the specified departure date (default: `2025-06-13`).

Results are grouped by city and emailed to the recipient specified in `.env`.

Example email content:

```
Subject: Flight Deals

Flights to New York: SIN-JFK, Airline: Singapore Airlines, Price: 1500 SGD, Departure: June 13, 2025 12:00
```

### Customize Departure Date

Edit the `FlightSearch` instantiation in `flight_data.py` to change the departure date:

```python
self.fs = FlightSearch("your-date-here")  # e.g., "2025-07-01"
```

## Project Structure

```
flight-deals-notifier/
│
├── data_manager.py         # Fetches destination data from Sheety API
├── flight_data.py          # Formats flight results for display
├── flight_search.py        # Queries Amadeus API for flight offers
├── get_access_token.py     # Generates a new Amadeus access token (optional)
├── main.py                 # Entry point to run the application
├── notification_manager.py # Sends flight deals via email
└── README.md               # This file
```

## Configuration

- **Amadeus API**: Update `get_access_token.py` with your credentials to generate a new token if needed, then set it in `.env`.
- **Email**: Ensure your Gmail account allows SMTP access. Use an App Password if 2FA is enabled.
- **Sheety API**: The URL is hardcoded; modify `data_manager.py` if your endpoint differs.

## Notes

- The Amadeus API used here is the test environment (`test.api.amadeus.com`). For production, switch to the live API and update the URL.
- Error handling is basic; check console output for API request failures.
- Departure dates are formatted as `Month Day, Year HH:MM` (UTC). Adjust time zones in `flight_data.py` if needed.

## Contributing

Feel free to fork this repository, submit issues, or create pull requests. Suggestions for improving error handling, adding features (e.g., multiple origins), or enhancing formatting are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- **Amadeus for Developers**: for flight data.
- **Sheety**: for destination data management.

## Instructions

1. Save this as `README.md` in your project root.
2. Replace `your-username` in the clone URL with your GitHub username.
3. Add a `LICENSE` file if you want to include licensing (e.g., MIT License text).
4. Push to GitHub:

```bash
git add .
git commit -m "Add README and secure secrets"
git push origin main
```

