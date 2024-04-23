# Test case Project_02 ID:TC_PIM_02

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


class PIM02:
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

    def quit(self): #quit the login page
        self.driver.quit()

    def findElementByXpath(self, xpath): #inspect by xpath
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def login(self): #main process
        try:
            self.boot()
            self.inputBox('username', self.username)
            self.inputBox('password', self.password)
            self.submitBtn() # for clicking the button
            self.sleep(1)
            #for validate the user management
            self.findElementByXpath('//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span').click()
            self.sleep(5)

            # for validate the job
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span').click()
            self.sleep(3)

            # for validate the organization
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span').click()
            self.sleep(3)

            # for validate the qualification
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span').click()
            self.sleep(3)

            # for validate the nationlities
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]').click()
            self.sleep(3)

            # for validate the corporate banking
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a').click()
            self.sleep(3)

            # for validate the configuration
            self.findElementByXpath(
                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span').click()
            self.sleep(3)



            print('successful')
        except NoSuchElementException:
            print('error')


url = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
obj = PIM02(url, 'Admin', 'admin123')
obj.login()
