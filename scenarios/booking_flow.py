# scenarios/booking_flow.py

from faker import Faker
from utils.logger import get_logger
from bs4 import BeautifulSoup
from config import settings

fake = Faker()
logger = get_logger()


def search_flights(user):
    response = user.client.get("/", name="Search Flights")
    if response.status_code == 200:
        logger.info("Homepage loaded successfully.")
    else:
        logger.warning(f"Failed to load homepage. Status: {response.status_code}")


def select_flight(user):
    from_city = fake.city()
    to_city = fake.city()

    logger.info(f"Booking flight: {from_city} to {to_city}")

    response = user.client.post("/reserve.php", {
        "fromPort": from_city,
        "toPort": to_city
    }, name="Select Flight")

    if "Flights from" in response.text:
        logger.info("Flight selection successful.")
    else:
        logger.warning("Unexpected response content during flight selection.")




def book_flight(user):
    logger.info(" Booking flight...")
    payload = {
        "inputName": fake.name(),
        "address": fake.address(),
        "city": fake.city(),
        "state": fake.state(),
        "zipCode": fake.zipcode(),
        "cardType": "Visa",
        "creditCardNumber": fake.credit_card_number(),
        "creditCardMonth": "12",
        "creditCardYear": "2025",
        "nameOnCard": fake.name(),
    }
    DEBUG_MODE = settings.DEBUG_MODE
    

    # Send the POST request to the confirmation endpoint
    response = user.client.post("/confirmation.php", payload, name="Book Flight")
    
    
    if DEBUG_MODE:
        logger.debug(f"Payload: {payload}")
        logger.debug(f"Response: {response.text}")

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    success_message = soup.find("h1").text if soup.find("h1") else None
    booking_id = soup.find("p", text=lambda x: x and "Id" in x).text if soup.find("p", text=lambda x: x and "Id" in x) else None

    # Validate the response
    if success_message and "Thank you for your purchase today!" in success_message:
        logger.info(f"Flight booking successful. Booking ID: {booking_id}")
    else:
        logger.warning(f" Flight booking failed. Status: {response.status_code}, Response: {response.text}")