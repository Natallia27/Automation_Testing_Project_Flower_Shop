import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g


    #Lokators

    card_text = "//textarea[@name='card_text']"
    update_card_button = "//button[@name='update_cart']"
    forward_button = "//a[@class='checkout-button button alt wc-forward']"


    #Getters

    def get_card_text(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.card_text)))


    def get_update_card_button(self):
        return WebDriverWait(self.driver_g, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.update_card_button)))


    def get_forward_button(self):
        return WebDriverWait(self.driver_g, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.forward_button)))

 #Actions

    def input_card_text(self, card_text):
        self.get_card_text().send_keys(card_text)
        print("Input card_text")

    def click_update_card_button(self):
        self.get_update_card_button().click()
        print("Click update_card_button")

    def click_forward_button(self):
        self.get_forward_button().click()
        print("Click forward_button")

    # Methods

    def cart_sum(self):
        self.input_card_text('For you')
        time.sleep(10)
        self.click_update_card_button()
        time.sleep(10)
        self.click_forward_button()
        time.sleep(10)






