import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure

class ProductPage(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g
        self.price_value = 0

    # Lokators

    change_size = "/html/body/div[1]/main/section/div/div/div[2]/form/div[5]/label[2]/span"
    new_price = "/html/body/div[1]/main/section/div/div/div[2]/form/div[4]/div/div[2]/span/bdi"
    product_name = "//h1[@class ='title heading-3']"
    cart = "//a[@class='btn-cta-2 btn-small js-ajax-add-to-cart btn-add-to-cart btn']"
    cart_page = "//*[@id='main-header']/div[2]/div/div[3]/div[1]/a"
    main_word_cart = "/html/body/div[1]/main/div/div[2]/div[2]/div/h2"

    # Getters

    def get_change_size(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.change_size)))

    def get_new_price(self):
        return self.driver_g.find_element(By.XPATH, self.new_price)

    def get_product_name(self):
        return self.driver_g.find_element(By.XPATH, self.product_name)

    def get_cart(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_cart_page(self):
        return WebDriverWait(self.driver_g, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_page)))

    def get_main_word_cart(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_cart)))

    # Actions

    def select_size(self):
        self.get_change_size().click()
        print("Select size")

    def print_new_price(self):
        price = self.get_new_price().text
        print("New price:" + price)
        self.price_value = price

    def print_product_name(self):
        product_name = self.get_product_name().text
        print("Product_name:" + product_name)

    def click_cart(self):
        self.get_cart().click()
        print("Add to cart")

    def click_cart_page(self):
        self.get_cart_page().click()
        print("Click cart")

    def assert_word_cart(self, word_cart, result_cart):
        value_word_cart = word_cart.text
        assert value_word_cart == result_cart
        print('Good word')

    # Methods

    def product_add(self):
        with allure.step("Product_add"):
            Logger.add_start_step(method="Product_add")
            self.driver_g.execute_script("scrollTo(0,500)")
            time.sleep(5)
            self.select_size()
            self.print_new_price()
            self.print_product_name()
            self.click_cart()
            time.sleep(5)
            self.click_cart_page()
            self.assert_word_cart(self.get_main_word_cart(), 'Podsumowanie koszyka')
            Logger.add_end_step(url=self.driver_g.current_url, method="Product_add")
