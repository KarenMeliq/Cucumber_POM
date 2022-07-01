import pytest
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from features.locatorsGlobalsQA import LocatorsGlobalsQA
from features.locatorTestCustomer import LocatorsTestCustomer
from features.test_datas import TestData
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import pathlib
import time




class GlobalSqa:
    @pytest.fixture()
    @given('globalsqa home page')
    def open_globalsqa(self):
        driver_path = str(pathlib.Path().resolve()) + "\\resources\\chromedriver.exe"
        url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
        s = Service(driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.get(url)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()



    @when('I click on Bank manager login')
    def click_bank_manager(self):
        self.driver.find_element(By.XPATH,LocatorsGlobalsQA.bank_manager_btn).click()
        self.driver.find_element(By.XPATH, LocatorsGlobalsQA.add_customer_btn).click()


    @then('I click on Add customers')
    def add_customer(self):
        self.driver.find_element(By.XPATH, LocatorsGlobalsQA.cust_input_name).\
            send_keys(TestData.testname)
        self.driver.find_element(By.XPATH, LocatorsGlobalsQA.cust_input_lname).\
            send_keys(TestData.testLastName)
        self.driver.find_element(By.XPATH, LocatorsGlobalsQA.cust_input_postal).\
            send_keys(TestData.testPostalCode)
        self.driver.find_element(By.XPATH, LocatorsGlobalsQA.submit_customer).click()
        self.driver.switch_to.alert.accept()


    @then('I Search the customer in the Customers list')
    def search_customer(self):
        self.driver.find_element(By.XPATH, LocatorsGlobalsQA.customers).click()
        inp_field = self.driver.find_element(By.XPATH, LocatorsGlobalsQA.search_field)
        inp_field.send_keys(TestData.testPostalCode)

    time.sleep(10)
    @then('I Delete customer')
    def remove_customer(self):
        self.driver.find_element(By.XPATH, LocatorsGlobalsQA.delete_btn).click()

    @then('I close browser')
    def close_browser(self):
        self.driver.quit()




