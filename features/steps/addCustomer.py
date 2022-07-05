from behave import *
from features.pageElementsGlobalsQA import PageElementsGlobalsQA
from features.test_datas import TestData
from selenium.webdriver.common.by import By
from features.steps.browser import Browser

class AddCustomer:

    @then('I click on Add customers')
    def add_customer(self):
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.cust_input_name). \
            send_keys(TestData.testname)
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.cust_input_lname). \
            send_keys(TestData.testLastName)
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.cust_input_postal). \
            send_keys(TestData.testPostalCode)
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.submit_customer).click()
        Browser.driver.switch_to.alert.accept()