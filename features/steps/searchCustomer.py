from behave import *
from features.pageElementsGlobalsQA import PageElementsGlobalsQA
from features.test_datas import TestData
from selenium.webdriver.common.by import By
from features.steps.browser import Browser


class Searchcustomer:
    @then('I search the customer in the Customers list')
    def search_customer(self):
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.customers).click()
        inp_field = Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.search_field)
        inp_field.send_keys(TestData.testPostalCode)

    @then('I delete customer')
    def remove_customer(self):
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.delete_btn).click()

    @then('I close browser')
    def close_self(self):
        Browser.driver.quit()