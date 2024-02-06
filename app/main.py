from browser_automation import init_browser, login
from scheduler import start_scheduler

def main():
    driver = init_browser()
    login(driver)
    start_scheduler(driver, check_interval=300)  # Check every 5 minutes

    # Keep the script running until an exception occurs or the process is manually stopped.
    try:
        while True:
            pass
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
