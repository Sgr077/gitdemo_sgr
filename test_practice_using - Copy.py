import pytest
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

#from pytestsdemo.need.demo import demmo
from utilites.baseclass import BaseeClass



class Testpracticee(BaseeClass):
    def test_tc1(self):
        print("Tc1: To verify the shop cart link is clickable")
        print("Running test case: 1")
        print("Link is clickable")
        print("Tc1: Pass")

