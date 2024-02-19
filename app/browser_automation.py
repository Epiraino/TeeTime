from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from config import DESIRED_TIMES, URL
from selenium.webdriver.common.by import By
from config import USERNAME, PASSWORD
import datetime
def init_browser():
    """Initialize the web browser."""
    driver = webdriver.Chrome()  # Or the driver you are using
    driver.get(URL)
    return driver

def login(driver):
    """Log in to the website."""
    driver.find_element
    driver.find_element(By.ID, "username_field_id").send_keys(USERNAME)
    driver.find_element(By.ID, "password_field_id").send_keys(PASSWORD + Keys.RETURN)


def find_tee_time(driver):
    """Find an available tee time."""
    # Navigate to the booking page, adjust selectors based on actual page structure
    driver.find_element(By.ID, "booking_page_link").click()
    # Example logic to find a tee time; adjust as needed
    for time_slot in DESIRED_TIMES:
        try:
            time_element = driver.find_element(By.XPATH, f"//button[text()='{time_slot}']")
            if time_element:
                return time_element
        except NoSuchElementException:
            continue
    return None

def book_tee_time(driver, time_element):
    """Book the found tee time."""
    time_element.click()
    # Complete the booking process, adjust selectors based on actual page structure
    driver.find_element(By.ID, "confirm_booking_button").click()

def check_and_book_tee_time(driver):
    """Check for and book a tee time if available."""
    time_element = find_tee_time(driver)
    if time_element:
        book_tee_time(driver, time_element)
        return True
    return False
