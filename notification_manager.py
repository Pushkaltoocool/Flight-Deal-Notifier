import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flight_data import FlightData
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("EMAIL_PASSWORD")
        self.flight_data = FlightData()
        self.message = self.flight_data.return_formatted_flights()
        self.recipient_email = os.getenv("RECIPIENT_EMAIL")

    def send_message(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            print(f"Sending email = {self.message}")
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.recipient_email,
                msg=f"Subject: Flight Deals \n\n  {self.message}"
            )