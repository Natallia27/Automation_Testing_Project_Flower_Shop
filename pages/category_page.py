import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CategoryPage(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #Lokators

    accept = "//a[@id='cn-accept-cookie']"
    new_max_price = "//input[@name='filter_price_max']"
    check_box_hit = "/html/body/div[1]/main/div[2]/div/div/aside/div/form/div[2]/div[2]/label[3]/span[1]"
    check_box_size = "/html/body/div[1]/main/div[2]/div/div/aside/div/form/div[2]/div[3]/label[1]/span[1]"
    filtr_button = "//button[@class='btn-submit btn-cta-1']"
    product = "/html/body/div[1]/main/div[2]/div/div/div/div[1]/div/div/div[2]/a/figure/img"


    #Getters

    def get_accept(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.accept)))

    def get_new_max_price(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.new_max_price)))
    def get_max_price(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.new_max_price)))

    def get_check_box_hit(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_hit)))
    def get_check_box_size(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_box_size)))
    def get_filtr_button(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filtr_button)))

    def get_product(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product)))


  #Actions


    def select_accept(self):
        self.get_accept().click()
        print("Select accept cookies")

    def clear_max_price(self):
        self.get_new_max_price().send_keys(Keys.BACKSPACE*10)
        print("Input clear_max_price")

    def input_max_price(self, max_price):
        self.get_max_price().send_keys(max_price)
        print("Input max_price")

    def select_check_box_hit(self):
        self.get_check_box_hit().click()
        print("Select check_box_hit")

    def select_check_box_size(self):
        self.get_check_box_size().click()
        print("Select check_box_size")

    def click_filtr_button(self):
        self.get_filtr_button().click()
        print("Click filtr_button")

    def add_product(self):
        self.get_product().click()
        print("Add product")

    # Methods

    def category_product_select(self):
        self.select_accept()
        time.sleep(3)
        self.clear_max_price()
        self.input_max_price("200")
        time.sleep(3)
        self.driver_g.execute_script("scrollTo(0,1000)")
        time.sleep(3)
        self.select_check_box_hit()
        self.select_check_box_size()
        self.click_filtr_button()
        time.sleep(3)
        self.add_product()


