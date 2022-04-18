from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

import time

TWITTER_EMAIL = "pycharmtester1@gmail.com"
TWITTER_PASSWORD = "XX"
PROMISED_DOWN = 150
PROMISED_UP = 10

chrome_path = r"C:\Users\pc\PycharmProjects\Web Development_DONE/chromedriver.exe"

service = Service(chrome_path)
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service)


class InternetSpeedTwitterBot:
    def __init__(self, driver, down, up):
        self.driver = driver
        self.down = down
        self.up = up

    def get_internet_speed(self):
        self.download = 46.78
        self.upload = 10.09
        # ______________________________________________________________________#
        # WORKS>
        #      driver.maximize_window()

    #     driver.get("https://www.speedtest.net/")

    #    launch_test = driver.find_element(By.ID, "_evidon-banner-acceptbutton")
    #   launch_test.click()

    #  launch_test = driver.find_element(By.XPATH,
    #                            "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
    # launch_test.click()

    # time.sleep(60)
    # self.download = driver.find_element(By.XPATH,
    #                          "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text

    #  self.upload = driver.find_element(By.XPATH,
    #                         "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text
    # driver.quit()

    # print(self.download, self.upload)
    # ______________________________________________________________________#

    def tweet_at_provider(self):
        driver.maximize_window()
        driver.get("https://www.twitter.com/")
        time.sleep(2)
        cookies = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span/span")
        cookies.click()
        time.sleep(2)
        login = driver.find_element(By.XPATH,
                                    "/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")
        login.click()
        time.sleep(2)
        print("3")
        name = driver.find_element(By.XPATH,

                                   "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        name.send_keys(TWITTER_EMAIL)
        name.send_keys(Keys.ENTER)
        time.sleep(3)
        activity = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        activity.click()
        activity.send_keys("lukas_minster")
        activity.send_keys(Keys.ENTER)
        time.sleep(2)
        pw = driver.find_element(By.XPATH,
                                 "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        pw.send_keys(TWITTER_PASSWORD)
        pw.send_keys(Keys.ENTER)
        time.sleep(3)

        post_win = driver.find_element(By.XPATH,
                                       "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        post_win.send_keys(
            f"Hey Internet provider, why is my speed {self.download}down/{self.upload}up when I pay for {self.down}down/{self.up}up?")

        post = driver.find_element(By.XPATH,
                                   "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        post.click()


bot = InternetSpeedTwitterBot(driver, PROMISED_DOWN, PROMISED_UP)
bot.get_internet_speed()
bot.tweet_at_provider()








