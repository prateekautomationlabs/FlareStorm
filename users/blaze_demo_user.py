from locust import HttpUser, SequentialTaskSet, task, between
from config import settings
from scenarios import booking_flow

class FlightBookingFlow(SequentialTaskSet):
    @task
    def search_flights(self):
        booking_flow.search_flights(self)

    @task
    def select_flight(self):
        booking_flow.select_flight(self)

    @task
    def book_flight(self):
        booking_flow.book_flight(self)

class BlazeDemoUser(HttpUser):
    wait_time = between(settings.MIN_WAIT, settings.MAX_WAIT)
    host = settings.BASE_URL
    tasks = [FlightBookingFlow]