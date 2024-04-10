import schedule
import time
from database import Database

def update_data():
    db = Database()
    db.update_room_rate(5, 90.00)  # Example: Update room rate for room_id 5

def main():
    # Schedule data update and analytics tasks
    schedule.every().day.at("01:00").do(update_data)
    # Add more schedule tasks for analytics if needed

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
