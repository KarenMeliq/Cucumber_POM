
from behave import *
from features.pageElementsGlobalsQA import PageElementsGlobalsQA
from features.test_datas import TestData
from selenium.webdriver.common.by import By
from features.steps.browser import Browser

class GlobalSqa_login:

    @given('globalsqa home page')
    def open_globals_qa(self):
        Browser.driver.get(PageElementsGlobalsQA.url)
        Browser.driver.implicitly_wait(10)
        Browser.driver.maximize_window()

    @when('I click on Bank manager login')
    def click_bank_manager(self):
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.bank_manager_btn).click()
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.add_customer_btn).click()
