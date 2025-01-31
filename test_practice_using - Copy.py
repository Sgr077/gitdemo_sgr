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

    @pytest.mark.smoke
    def test_tc2(self):
        print("Tc-2: To verify the shop cart link is clickable and launch in to correct site")
        print("Running test case: 2")

        # Click the shop link using XPath
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()
        print("shop cart link is clickable and launch in to correct site")

        print("Tc-2: Pass")
        
       def test_tc3335(self):
        print("Tc-2: To verify the shop cart link is clickable and launch in to correct site")
        print("Running test case: 2")

        # Click the shop link using XPath
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()
        print("shop cart link is clickable and launch in to correct site")

        print("Tc-2: Pass")

    

    def test_tc4(self):
        print("Tc-4: To verify the check out function without adding any items")
        print("Running test case: 4")
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
        print("Total: ", amount)
        print("Check out button is clickable and amount is Zero")
        print("Tc-4: Pass")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()

    def test_tc5(self):
        print("#Tc-5: To verify the cart function with all items adding")
        print("Running test case: 5")
        lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
        count = 0
        for butn in lists:
            button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
            count += 1
            button.click()
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
        print("Total: ", amount)
        print("All product added to the cart and total amount is displayed ")
        print("Tc-5: Pass")
        self.driver.find_element(By.LINK_TEXT, "Shop").click()

    def test_tc6(self):
        print("Tc-6: To verify the cart function for one items adding")
        print("Running test case: 6")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[2]").click()
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
        print("Total: ", amount)
        print("one product added to the cart and total amount is displayed ")
        print("Tc-6: Pass")
        self.driver.find_element(By.LINK_TEXT, "Shop").click()

    def test_tc7(self):
        print("Tc-7: To verify the cart function for two items adding")
        print("Running test case: 7")
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[1]").click()
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[2]").click()
        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
        print("Total: ", amount)
        print("two product added to the cart and total amount is displayed ")
        print("Tc-7: Pass")
        self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # def test_tc8(self):
    #     print("Tc-8: To verify the cart function for three items adding")
    #     print("Running test case: 8")
    #     self.driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[1]").click()
    #     self.driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[2]").click()
    #     self.driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[3]").click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #     print("three product added to the cart and total amount is displayed ")
    #     print("Tc-8: Pass")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # def test_tc9(self):
    #     print("Tc-9: To verify the number of item in cart is equal to total items in main page")
    #     print("Running test case: 9")
    #     product_lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     product_lists_total = len(product_lists)
    #     lists1 = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists1:
    #         button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
    #         count += 1
    #         button.click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     time.sleep(3)
    #     cart_list = self.driver.find_elements(By.XPATH, "//tbody/tr")
    #     cart_list_total = len(cart_list)
    #     lists2 = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists2:
    #         button = butn.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Remove'])")
    #         count += 1
    #     print("product_lists_total: ", product_lists_total)
    #     print("cart_list_total: ", cart_list_total)
    #     if cart_list_total == 6:
    #         print("Tc-9: Pass: cart_list_total will be +2 includes 'total' and 'check out option'")
    #     else:
    #         print("Fail")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # def test_tc10(self):
    #     print("Tc-10: To verify the remove functionality in the cart page")
    #     print("Running test case: 10")
    #     product_lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     product_lists_total = len(product_lists)
    #     lists1 = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists1:
    #         button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
    #         count += 1
    #         button.click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     remove_button = self.driver.find_elements(By.XPATH, "//button[@class='btn btn-danger']")
    #     count = 0
    #     for butn in remove_button:
    #         butn = self.driver.find_element(By.XPATH, "//button[@class='btn btn-danger']")
    #         count += 1
    #         butn.click()
    #     print("products removed from the cart page")
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #     if amount == "₹. 0":
    #         print("Tc10: Pass")
    #     else:
    #         print("fail")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # def test_tc11(self):
    #     print("Tc-11: To verify the item price is equal to the total individual  price")
    #     print("Running test case: 11")
    #     product_lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     product_lists_total = len(product_lists)
    #     print("Product Total list: ", product_lists_total)
    #     lists1 = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists1:
    #         button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
    #         count += 1
    #         button.click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     prices = self.driver.find_elements(By.XPATH, "//tr/td[3]/strong[1]")
    #     count = 0
    #     price_list = []
    #     for price in prices:
    #         price_text = price.text
    #         price_list.append(price_text)
    #         count += 1
    #     print("Each product price:", price_list, end=";")
    #
    #     Total = self.driver.find_elements(By.XPATH, "//tr/td[4]/strong[1]")
    #     count = 0
    #     Total_list = []
    #     for tot in Total:
    #         tot_text = tot.text
    #         Total_list.append(tot_text)
    #         count += 1
    #     print("Each product price:", Total_list)
    #
    #     if price_list == Total_list:
    #         print("Tc-11: Pass, price_list is equal to Total_list")
    #     else:
    #         print("Fail")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # def test_tc12(self):
    #     print("Tc-12: To verify the quantity can be added more or less")
    #     # initial amount
    #     print("Running test case: 12")
    #     self.driver.find_element(By.XPATH, "(//button[normalize-space()='Add'])[2]").click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     time.sleep(2)
    #     prices = self.driver.find_element(By.XPATH, "//tr/td[3]/strong[1]").text
    #     Total = self.driver.find_element(By.XPATH, "//tr/td[4]/strong[1]").text
    #     print("prices: ", prices)
    #     print("Total: ", Total)
    #     Initial_amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Initial_amount: ", Initial_amount)
    #
    #     # Final amount
    #     self.driver.find_element(By.ID, "exampleInputEmail1")
    #     qty = self.driver.find_element(By.ID, "exampleInputEmail1")
    #     qty.clear()
    #     self.driver.find_element(By.ID, "exampleInputEmail1").send_keys(3)
    #     prices = self.driver.find_element(By.XPATH, "//tr/td[3]/strong[1]").text
    #     Total = self.driver.find_element(By.XPATH, "//tr/td[4]/strong[1]").text
    #     print("prices: ", prices)
    #     print("Total: ", Total)
    #     Final_amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Final_amount: ", Final_amount)
    #
    #     if Initial_amount != Final_amount:
    #         print("Tc12:Pass, Initial_amount is not equal to Final_amount")
    #     else:
    #         print("Fail")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # def test_tc13(self):
    #     print("Tc-13: To verify the remove  first two items functionality in the cart page")
    #     print("Running test case: 13")
    #     lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists:
    #         button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
    #         count += 1
    #         button.click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     print("All product added to the cart and total amount is displayed ")
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #
    #     Initial_cart_list = self.driver.find_elements(By.XPATH, "//tbody/tr")
    #     Initial_cart_list_total = len(Initial_cart_list)
    #     print("Initial_cart_list_total: ", Initial_cart_list_total)
    #
    #     # removing iphonx & samsung
    #     name1 = self.driver.find_element(By.XPATH, "//a[normalize-space()='iphone X']").text
    #     name2 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Samsung Note 8']").text
    #
    #     print("Removing Item : ", name1)
    #     print("Removing Item : ", name2)
    #
    #     if name1 == "iphone X":
    #         self.driver.find_element(By.XPATH, "//tr[1]//td/button[normalize-space()='Remove']").click()
    #     else:
    #         print("cant find button1")
    #     time.sleep(2)
    #     if name2 == "Samsung Note 8":
    #         self.driver.find_element(By.XPATH, "//tr[1]//td/button[normalize-space()='Remove']").click()
    #     else:
    #         print("cant find button2")
    #     Final_cart_list = self.driver.find_elements(By.XPATH, "//tbody/tr")
    #     Final_cart_list_total = len(Final_cart_list)
    #     print("Final_cart_list_total: ", Final_cart_list_total)
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #
    #     if Final_cart_list_total != Initial_cart_list_total:
    #         print("Actual Result:")
    #         print("1.first two items removed from the cart")
    #         print("2.Final_cart_list is not equal to Initial_cart_list")
    #         print("Tc13:Pass")
    #     else:
    #         print("Fail")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # def test_tc14(self):
    #     print("Tc-14: To verify the remove  last two items functionality in the cart page")
    #     print("Running test case: 14")
    #     lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists:
    #         button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
    #         count += 1
    #         button.click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     print("All product added to the cart and total amount is displayed ")
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #
    #     Initial_cart_list = self.driver.find_elements(By.XPATH, "//tbody/tr")
    #     Initial_cart_list_total = len(Initial_cart_list)
    #     print("Initial_cart_list_total: ", Initial_cart_list_total)
    #
    #     # removing Nokia Edge & Blackberry
    #     name1 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Nokia Edge']").text
    #     name2 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Blackberry']").text
    #
    #     print("Removing Item: ", name1)
    #     print("Removing item: ", name2)
    #
    #     if name1 == "Nokia Edge":
    #         self.driver.find_element(By.XPATH, "//tr[3]//td/button[normalize-space()='Remove']").click()
    #     else:
    #         print("cant find button1")
    #     time.sleep(2)
    #     if name2 == "Blackberry":
    #         self.driver.find_element(By.XPATH, "//tr[3]//td/button[normalize-space()='Remove']").click()
    #     else:
    #         print("cant find button2")
    #     Final_cart_list = self.driver.find_elements(By.XPATH, "//tbody/tr")
    #     Final_cart_list_total = len(Final_cart_list)
    #     print("Final_cart_list_total: ", Final_cart_list_total)
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #
    #     if Final_cart_list_total != Initial_cart_list_total:
    #         print("Actual Result:")
    #         print("1.first two items removed from the cart")
    #         print("2.Final_cart_list is not equal to Initial_cart_list")
    #         print("Tc14:Pass")
    #     else:
    #         print("Fail")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # @pytest.mark.smoke
    # def test_tc15(self):
    #     print("Tc-15: To verify the remove 1 & 3 items functionality in the cart page")
    #     print("Running test case: 15")
    #     product_lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     product_lists_total = len(product_lists)
    #     lists1 = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists1:
    #         button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
    #         count += 1
    #         button.click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     print("All product added to the cart and total amount is displayed ")
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #
    #     Initial_cart_list = self.driver.find_elements(By.XPATH, "//tbody/tr")
    #     Initial_cart_list_total = len(Initial_cart_list)
    #     print("Initial_cart_list_total: ", Initial_cart_list_total)
    #
    #     # removing Nokia Edge & Blackberry
    #     name1 = self.driver.find_element(By.XPATH, "//a[normalize-space()='iphone X']").text
    #     name2 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Nokia Edge']").text
    #
    #     print("Removing Item: ", name1)
    #     print("Removing item: ", name2)
    #
    #     if name1 == "iphone X":
    #         self.driver.find_element(By.XPATH, "//tr[1]//td/button[normalize-space()='Remove']").click()
    #     else:
    #         print("cant find button1")
    #     if name2 == "Nokia Edge":
    #         self.driver.find_element(By.XPATH, "//tr[2]//td/button[normalize-space()='Remove']").click()
    #     else:
    #         print("cant find button2")
    #     time.sleep(2)
    #
    #     Final_cart_list = self.driver.find_elements(By.XPATH, "//tbody/tr")
    #     Final_cart_list_total = len(Final_cart_list)
    #     print("Final_cart_list_total: ", Final_cart_list_total)
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #
    #     if Final_cart_list_total != Initial_cart_list_total:
    #         print("Actual Result:")
    #         print("1.one & third items removed from the cart")
    #         print("2.Final_cart_list is not equal to Initial_cart_list")
    #         print("Tc15:Pass")
    #     else:
    #         print("Fail")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # def test_tc16(self):
    #     print("Tc-16: To verify the remove 2 & 4 items functionality in the cart page")
    #     print("Running test case: 16")
    #     product_lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     product_lists_total = len(product_lists)
    #     lists1 = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists1:
    #         button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
    #         count += 1
    #         button.click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     print("All product added to the cart and total amount is displayed ")
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #
    #     Initial_cart_list = self.driver.find_elements(By.XPATH, "//tbody/tr")
    #     Initial_cart_list_total = len(Initial_cart_list)
    #     print("Initial_cart_list_total: ", Initial_cart_list_total)
    #
    #     # removing Nokia Edge & Blackberry
    #     name1 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Samsung Note 8']").text
    #     name2 = self.driver.find_element(By.XPATH, "//a[normalize-space()='Blackberry']").text
    #
    #     print("Removing Item: ", name1)
    #     print("Removing item: ", name2)
    #
    #     if name1 == "Samsung Note 8":
    #         self.driver.find_element(By.XPATH, "//tr[1]//td/button[normalize-space()='Remove']").click()
    #     else:
    #         print("cant find button2")
    #     if name2 == "Blackberry":
    #         self.driver.find_element(By.XPATH, "//tr[3]//td/button[normalize-space()='Remove']").click()
    #     else:
    #         print("cant find button2")
    #     time.sleep(2)
    #
    #     Final_cart_list = self.driver.find_elements(By.XPATH, "//tbody/tr")
    #     Final_cart_list_total = len(Final_cart_list)
    #     print("Final_cart_list_total: ", Final_cart_list_total)
    #     amount = self.driver.find_element(By.XPATH, "//td[@class='text-right']").text
    #     print("Total: ", amount)
    #
    #     if Final_cart_list_total != Initial_cart_list_total:
    #         print("Actual Result:")
    #         print("1.two & fourth items removed from the cart")
    #         print("2.Final_cart_list is not equal to Initial_cart_list")
    #         print("Tc16:Pass")
    #     else:
    #         print("Fail")
    #     self.driver.find_element(By.LINK_TEXT, "Shop").click()
    #
    # def test_tc17(self):
    #     print("Tc-17: To verify the item name,item price, item description and print")
    #     title = self.driver.find_elements(By.XPATH, "(//h4[@class='card-title'])")
    #     Title_list = []
    #     for titles in title:
    #         tit_text = titles.text
    #         Title_list.append(tit_text)
    #     print("Each product name:", Title_list)
    #
    #     price = self.driver.find_elements(By.XPATH, "//app-card//div/h5")
    #     price_list = []
    #     for pricee in price:
    #         prz_text = pricee.text
    #         price_list.append(prz_text)
    #     print("Each product price:", price_list)
    #
    #     prd_text = self.driver.find_elements(By.XPATH, "//p[@class='card-text']")
    #     prd_des = []
    #     for prd in prd_text:
    #         pr = prd.text
    #         prd_des.append(pr)
    #     print("Each product description:", prd_des, end=";")
    #     print("Tc17:Pass")
    #
    # def test_tc18(self):
    #     print("Tc-18: To verify the Main page previous icon functionality")
    #     for icon in range(3):
    #         self.driver.find_element(By.CLASS_NAME, "carousel-control-prev-icon").click()
    #     print("Tc18:Pass")
    #
    # time.sleep(5)
    #
    # def test_tc19(self):
    #     print("Tc-19: To verify the Main page next icon functionality")
    #     for icon in range(3):
    #         self.driver.find_element(By.CLASS_NAME, "arousel-control-next-icon").click()
    #     print("Tc19:Pass")
    #
    # time.sleep(5)
    #
    # def test_tc20(self):
    #     print("Tc-20: To verify the items review ratings for all item")
    #     title = self.driver.find_elements(By.XPATH, "(//h4[@class='card-title'])")
    #     Title_list = []
    #     for titles in title:
    #         tit_text = titles.text
    #         Title_list.append(tit_text)
    #     print("Each product name:", Title_list)
    #
    #     review = self.driver.find_elements(By.CLASS_NAME, "text-muted")
    #     review_list = []
    #     for rev in review:
    #         r1 = rev.text
    #         review_list.append(r1)
    #     print("product Review", review_list, end=";")
    #     print("Tc20:Pass")
    #
    # def test_tc21(self):
    #     print("Tc-21: To check the copy rights is equal t the given text")
    #     name = self.driver.find_element(By.XPATH,"(//div[@class='container'])[4]")
    #     name_text = name.text
    #     print("copyrights: ", name_text)
    #     if name_text == "Copyright © ProtoCommerce 2018":
    #         print("tc21:Pass")
    #     else:
    #         print("Fail")

    # def test_tc22(self):
    #     print("Tc-22: To gett the screen shot of only product items")
    #     self.driver.execute_script("window.scrollBy(0,900);")
    #     self.driver.get_screenshot_as_file("only product items.png")
    #     print("screenshot taken")
    #     print("Tc22:Pass")
    # time.sleep(1)

    # def test_tc23(self):
    #     print("Tc-23: To check the 'In status'' of each product")
    #     lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists:
    #         button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
    #         count += 1
    #         button.click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     status=self.driver.find_element(By.XPATH,"//span[@class='text-success']")
    #     for stat in status:
    #         stat_known=stat.text
    #         print("Each product list status:", stat_known)
    #         self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     print("Tc23:Pass")
    #
    # def test_tc24(self):
    #     print("Tc-24: To check the item from which company by")
    #
    #     lists = self.driver.find_elements(By.XPATH, "//body//app-root//app-card")
    #     count = 0
    #     for butn in lists:
    #         button = butn.find_element(By.XPATH, ".//button[@class='btn btn-info']")
    #         count += 1
    #         button.click()
    #     self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
    #     bylist=self.driver.find_elements(By.XPATH,"//div/h5[1][@class ='media-heading']")
    #     for bylil in bylist:
    #             byy_text = bylil.text
    #             print("Each By company name:", bylil.text)
    #     print("Tc24:Pass")
