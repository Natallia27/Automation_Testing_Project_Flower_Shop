import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure

class ClientPage(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g
        self.price_cart_value = 0

        # Lokators

    first_name = "//input[@id='billing_first_name']"
    last_name = "//input[@id='billing_last_name']"
    phone = "//input[@id='billing_phone']"
    email = "//input[@id='billing_email']"
    check_box_vat = "//input[@id='checkout-invoice-checkbox']"
    order_comments = "//textarea[@id='order_comments']"

    check_box_anonymous_delivery = "//input[@id='anonymous_delivery']"
    check_box_ecological_paper = "//input[@id='ecological_paper']"
    check_box_bouquet_photo = "//input[@id='bouquet_photo']"

    price_cart = "//*[@id='order_review']/table/tfoot/tr[2]/td/strong/span/bdi"
    product_name_and_size = "/html/body/div[1]/main/div/div[2]/div[1]/form/table/tbody/tr[1]/td[3]/a"

    new_date = "//*[@id='datetimepicker']/div/table/tbody/tr[6]/td[1]/a"
    delivery_hour = "//select[@id='delivery-hour']"
    select_hour = "//*[@id='delivery-hour']/option[3]"
    check_box_terms = "//input[@id='terms']"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_phone(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_email(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_check_box_vat(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_vat)))

    def get_order_comments(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_comments)))

    def get_check_box_anonymous_delivery(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_anonymous_delivery)))

    def get_check_box_ecological_paper(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_ecological_paper)))

    def get_check_box_bouquet_photo(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_bouquet_photo)))

    def get_price_cart(self):
        return self.driver_g.find_element(By.XPATH, self.price_cart)

    def get_product_name_and_size(self):
        return self.driver_g.find_element(By.XPATH, self.product_name_and_size)

    def get_new_date(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_date)))


    def get_delivery_hour(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_hour)))


    def get_select_hour(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_hour)))

    def get_check_box_terms(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_terms)))
    # Actions

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input first_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last_name")

    def input_phone(self, phone):
        self.get_phone().send_keys(phone)
        print("Input phone")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def click_check_box_vat(self):
        self.get_check_box_vat().click()
        print("Click check_box_vat")

    def input_order_comments(self, order_comments):
        self.get_order_comments().send_keys(order_comments)
        print("Input order_comments")

    def click_check_box_anonymous_delivery(self):
        self.get_check_box_anonymous_delivery().click()
        print("Click check_box_anonymous_delivery")

    def click_check_box_ecological_paper(self):
        self.get_check_box_ecological_paper().click()
        print("Click check_box_ecological_paper")

    def click_check_box_bouquet_photo(self):
        self.get_check_box_bouquet_photo().click()
        print("Click check_box_bouquet_photo")

    def print_price(self):
        price_cart = self.get_price_cart().text
        print("Price_cart:" + price_cart)
        self.price_cart_value = price_cart

    def click_new_date(self):
        self.get_new_date().click()
        print("Click new_date")

    def click_delivery_hour(self):
        self.get_delivery_hour().click()
        print("Click delivery_hour")

    def click_select_hour(self):
        self.get_select_hour().click()
        print("Click select_hour")

    def click_check_box_terms(self):
        self.get_check_box_terms().click()
        print("Click check_box_terms")

    # Methods
    def input_client_info(self):
        with allure.step("Input_client_info"):
            Logger.add_start_step(method="Input_client_info")
            self.input_first_name("Adam")
            self.input_last_name("Kozanowski")
            self.input_phone("793645789")
            self.input_email("kazanowski@gmail.com")
            self.driver_g.execute_script("scrollTo(0,600)")
            time.sleep(5)
            self.click_check_box_vat()
            self.input_order_comments("Phone me, please")
            time.sleep(5)
            self.driver_g.execute_script("scrollTo(0,1100)")
            time.sleep(5)
            self.click_check_box_anonymous_delivery()
            self.click_check_box_ecological_paper()
            self.click_check_box_bouquet_photo()
            self.driver_g.execute_script("scrollTo(0,100)")
            time.sleep(5)
            self.get_current_url()
            self.get_assert_url("https://bloomflowers.pl/zamowienie/")
            self.get_screenshot()
            self.print_price()
            self.driver_g.execute_script("scrollTo(0,500)")
            time.sleep(5)
            self.click_new_date()
            time.sleep(5)
            self.click_delivery_hour()
            time.sleep(5)
            self.click_select_hour()
            time.sleep(5)
            self.driver_g.execute_script("scrollTo(0,1200)")
            time.sleep(5)
            self.click_check_box_terms()
            time.sleep(5)
            Logger.add_end_step(url=self.driver_g.current_url, method="Input_client_info")



