
from behave import *
from features.pageElementsGlobalsQA import PageElementsGlobalsQA
from features.test_datas import TestData
from selenium.webdriver.common.by import By
from features.steps.browser import Browser

'''
class GlobalSqa:

   
    @given('globalsqa home page')
    def open_globals_qa(self):
        Browser.driver.get(PageElementsGlobalsQA.url)
        Browser.driver.implicitly_wait(10)
        Browser.driver.maximize_window()


    @when('I click on Bank manager login')
    def click_bank_manager(self):
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.bank_manager_btn).click()
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.add_customer_btn).click()



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
    '''
