import pytest
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from features.pageElementsGlobalsQA import PageElementsGlobalsQA
from features.locatorTestCustomer import LocatorsTestCustomer
from features.test_datas import TestData
from selenium.webdriver.common.by import By
from features.steps.browser import Browser
import time



class TestCustomer:

    @then('I test that customer is added with correct info')
    def test_customer(self):
        f_name = Browser.driver.find_element(By.XPATH, LocatorsTestCustomer.name)
        l_name = Browser.driver.find_element(By.XPATH, LocatorsTestCustomer.lname)
        postal_code = Browser.driver.find_element(By.XPATH, LocatorsTestCustomer.postal)
        assert f_name.text == TestData.testname
        assert l_name.text == TestData.testLastName
        assert postal_code.text == TestData.testPostalCode

    @then('I test that customer is deleted')
    def test_customer_removed(self):
        Browser.driver.find_element(By.XPATH, PageElementsGlobalsQA.search_field).clear()
        users = Browser.driver.find_element(By.CSS_SELECTOR, LocatorsTestCustomer.user_table).get_attribute("innerHTML")
        assert TestData.testname not in users
        time.sleep(3)

