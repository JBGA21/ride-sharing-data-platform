import time 
import json
from src.generators.ride_event_generator import generate_uber_ride_confirmation
from src.producers.eventhub_producer import send_to_event_hub

NUM_EVENTS = 3
INTERVAL_SECONDS = 5

def main():
    print("Generating 10 New Uber Ride Events... \n")
    for i in range(NUM_EVENTS):
        ride = generate_uber_ride_confirmation()
        print(f"{i})")
        print(json.dumps(ride, indent=2))
        print("\n")
        print("Sending Uber Ride Event Data to Azure Event Hub")
        result = send_to_event_hub(ride)
        print(f"Single ride sent to Event Hub: {result} \n")
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
