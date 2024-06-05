from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# Path to Brave browser executable
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Update the path if necessary

# Set up Chrome options to use Brave
chrome_options = Options()
chrome_options.binary_location = brave_path

# Path to ChromeDriver
webdriver_path = "chromedriver-win64\chromedriver.exe"  # Update with the actual path to your ChromeDriver

# Initialize the WebDriver with the specified options
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


# LinkedIn

VERIFY_LOGIN_ID = "global-nav__primary-link"
REMEMBER_PROMPT = 'remember-me-prompt__form-primary'


import getpass
# from . import constants as c
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def __prompt_email_password():
  u = input("Email: ")
  p = getpass.getpass(prompt="Password: ")
  return (u, p)

def page_has_loaded(driver):
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'

def login(driver, email=None, password=None, cookie = None, timeout=10):
    if cookie is not None:
        return _login_with_cookie(driver, cookie)
  
    if not email or not password:
        email, password = __prompt_email_password()
  
    driver.get("https://www.linkedin.com/login")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
  
    email_elem = driver.find_element(By.ID,"username")
    email_elem.send_keys(email)
  
    password_elem = driver.find_element(By.ID,"password")
    password_elem.send_keys(password)
    password_elem.submit()
  
    if driver.current_url == 'https://www.linkedin.com/checkpoint/lg/login-submit':
        remember = driver.find_element(By.ID, REMEMBER_PROMPT)
        if remember:
            remember.submit()
  
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, VERIFY_LOGIN_ID)))
  
def _login_with_cookie(driver, cookie):
    driver.get("https://www.linkedin.com/login")
    driver.add_cookie({
      "name": "li_at",
      "value": cookie
    })

login(driver=driver, email='smartboyrathore@gmail.com', password='Ashish@123')


from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def search_students(institution):
    search_url = f"https://www.linkedin.com/search/results/people/?keywords=student%20at%20{institution}&origin=GLOBAL_SEARCH_HEADER"
    driver.get(search_url)
    time.sleep(5)  # Wait for the search results to load

    profile_links = []
    names = []

    # Find all the profile links on the current search results page
    profiles = driver.find_elements(By.CLASS_NAME, "reusable-search__result-container")
    for profile in profiles:
        link_element = profile.find_element(By.CSS_SELECTOR, 'a.app-aware-link')
        link = link_element.get_attribute('href')
        profile_links.append(link)

        try:
            # Extract the name from the specified span element
            name_element = profile.find_element(By.CSS_SELECTOR, 'span[dir="ltr"] > span[aria-hidden="true"]')
            name = name_element.text
        except NoSuchElementException:
            name = "Name not found"
        names.append(name)

    return profile_links, names


profiles , names = search_students('Student at ACROPOLIS INSTITUTE OF TECHNOLOGY AND RESEARCH')

# Save the profiles and names to an Excel file
df = pd.DataFrame({
    "LinkedIn Profile URL": profiles,
    "Names": names
})

df.to_excel("Test.xlsx", index=False)

for profile in profiles:
    print(profile)