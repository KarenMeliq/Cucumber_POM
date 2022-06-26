import pytest
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from features.locators import Locators
from features.test_datas import TestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pathlib
import time
#from steps.browser import Browser



class GlobalSqa(Locators, TestData):


    @given('globalsqa home page')
    def open_globalsqa(self):
        driver_path = str(pathlib.Path().resolve()) + "\\resources\\chromedriver.exe"
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        while (True):
            pass
        return self.driver




    @when('Globalsqa home page click on Bank manager login')
    def click_bank_manager(self):
        driver = GlobalSqa.open_globalsqa()
        driver.find_element(By.XPATH, Locators.bank_manager_btn).click()
        driver.find_element(By.XPATH, Locators.add_customer_btn).click()


    @then('add customers')
    def add_customer():
        self.driver.find_element(By.XPATH, Locators.cust_input_name).send_keys(TestData.testname)
        self.driver.find_element(By.XPATH, Locators.cust_input_lname).send_keys(TestData.testLastName)
        self.driver.find_element(By.XPATH, Locators.cust_input_postal).send_keys(Locators.testPostalCode)
        self.driver.find_element(By.XPATH, Locators.add_customer_btn).click()

        iframe = driver.find_element(By.XPATH,pop_up)
        driver.switch_to.frame(iframe)
        popUp = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,)))
        popUp.click()
        driver.switch_to.default_content()


    @then('search the customer on Customers list')
    def search_customer():
        self.driver.find_element(By.XPATH, Locators.customers_list_btn).click()
        cust_list = self.driver.find_element(By.XPATH, Locators.customer_list)
        return cust_list

    @then('Assert that customer is added with correct info')
    def test_customer(context):
        raise NotImplementedError(u'STEP: Then Assert that customer is added with correct info')


    @then('Delete customer')
    def remove_customer(context):
        raise NotImplementedError(u'STEP: Then Delete customer')


    @then('Assert that customer is deleted')
    def test_customer_removed(context):
        raise NotImplementedError(u'STEP: Then Assert that customer is deleted')


    @then('close browser')
    def close_browser(context):
        raise NotImplementedError(u'STEP: Then close browser')


