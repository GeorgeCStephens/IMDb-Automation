from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox() 
URL = "https://www.imdb.com/"
TimeForBrowserToCatchUp=5


driver.get(URL)
time.sleep(TimeForBrowserToCatchUp)

SignInButton = driver.find_element(By.CLASS_NAME, "imdb-header__signin-text")
SignInButton.click()
time.sleep(TimeForBrowserToCatchUp)

PotentialSignOptions = driver.find_elements(By.CLASS_NAME, "auth-provider-text")
SignInOptions = {
    "IMDbSignIn":PotentialSignOptions[0],
    "AmazonSignIn":PotentialSignOptions[1],
    "GoogleSignIn":PotentialSignOptions[2],
    "AppleSignIn":PotentialSignOptions[3]
}
print(SignInOptions["IMDbSignIn"])

time.sleep(TimeForBrowserToCatchUp)

SignInOptions["IMDbSignIn"].click()
time.sleep(TimeForBrowserToCatchUp)