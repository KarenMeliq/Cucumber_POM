import pytest
from _pytest import pathlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Browser(object):

        driver_path = str(pathlib.Path().resolve()) + "\\resources\\chromedriver.exe"
        s = Service(driver_path)
        driver = webdriver.Chrome(service=s)


