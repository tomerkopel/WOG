from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys

def test_scores_service(url):
    driver = webdriver.Chrome(service=Service("//home/tomer/PycharmProjects/WorldOfGames/Utils/chromedriver"))
    try:
        driver.get(url)
        score_element = driver.find_element('id', 'score')
        score = int(score_element.text)
        return score >= 0 and score <= 1000
    except:
        print("URL unavailable")
        return False
def main_function ():
    result = test_scores_service("http://localhost:8777")

    if result:
        sys.exit(0)
    else:
        sys.exit(-1)


main_function()
