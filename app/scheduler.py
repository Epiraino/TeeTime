import time
from browser_automation import check_and_book_tee_time

def start_scheduler(driver, check_interval=60):
    """Start the scheduler to check for tee times every `check_interval` seconds."""
    while True:
        try:
            available = check_and_book_tee_time(driver)
            if available:
                print("Tee time booked successfully!")
                break
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(check_interval)
