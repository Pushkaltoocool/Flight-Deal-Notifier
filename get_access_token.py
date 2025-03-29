import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Your API credentials
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

# API endpoint for token request
token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"

# Request body (must be sent as application/x-www-form-urlencoded)
payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

# Request headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Send the request
response = requests.post(token_url, data=payload, headers=headers)

# Parse the response
if response.status_code == 200:
    token_data = response.json()
    access_token = token_data["access_token"]  # Extract the token
    print("New Access Token:", access_token)
else:
    print("Error:", response.status_code, response.text)