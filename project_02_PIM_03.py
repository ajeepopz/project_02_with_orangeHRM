# Test case Project_02 ID:TC_PIM_03

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


class PIM03:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.sleep(5)

    def sleep(self, second):
        sleep(second)

    def inputBox(self, value, keys): #login page
        self.driver.find_element(by=By.NAME, value=value).send_keys(keys)
        self.sleep(5)

    def submitBtn(self): #clicking the login button
        self.driver.find_element(by=By.TAG_NAME, value='button').click()
        self.sleep(10)

    def quit(self):  #quit the login page
        self.driver.quit()

    def findElementByXpath(self, xpath): #inspect by xpath
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def login(self): #main process
        try:
            self.boot()
            self.inputBox('username', self.username)
            self.inputBox('password', self.password)
            self.submitBtn()
            self.sleep(3)
            # This for Admin valitation
            self.findElementByXpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
            self.sleep(3)

            #This for PIM valitation
            self.findElementByXpath(
               ' //*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
            self.sleep(3)

            # This for leave valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span').click()
            self.sleep(3)

            # This for Time valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span').click()
            self.sleep(3)

            # This for Recuriment valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
            self.sleep(3)

            # This for myinfo valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').click()
            self.sleep(3)

            # This for Performance valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').click()
            self.sleep(3)

            # This for Dashboard valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span').click()
            self.sleep(3)

            # This for Directory valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span').click()
            self.sleep(3)

            # This for Manitance valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span')
            self.sleep(3)

            # This for Claim valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span').click()
            self.sleep(3)

            # This for Buzz valitation
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span').click()
            self.sleep(3)

            print('successful')
        except:
            print('error')


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/nationality'
obj = PIM03(url, 'Admin', 'admin123')
obj.login()