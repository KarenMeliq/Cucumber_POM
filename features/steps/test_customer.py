import pytest
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from features.locatorsGlobalsQA import LocatorsGlobalsQA
from features.locatorTestCustomer import LocatorsTestCustomer
from features.test_datas import TestData
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('open_globalsqa')
class testCustomer:

    @then('I test that customer is added with correct info')
    def test_customer(self):
        f_name = self.driver.find_element(By.XPATH, LocatorsTestCustomer.name)
        l_name = self.driver.find_element(By.XPATH, LocatorsTestCustomer.lname)
        postal_code = self.driver.find_element(By.XPATH, LocatorsTestCustomer.postal)
        assert f_name.text == TestData.testname
        assert l_name.text == TestData.testLastName
        assert postal_code.text == TestData.testPostalCode

    @then('I test that customer is deleted')
    def test_customer_removed(self):
        self.driver.find_element(By.XPATH, LocatorsGlobalsQA.search_field).clear()
        users = self.driver.find_element(By.XPATH, LocatorsTestCustomer.user_table).get_attribute("innerHTML")
        assert TestData.testname not in users
