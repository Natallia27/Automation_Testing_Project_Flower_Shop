from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger
import allure

class MainPage(Base):
    url = "https://bloomflowers.pl/"

    def __init__(self, driver_g):
        super().__init__(driver_g)
        self.driver_g = driver_g

    # Lokators

    menu_item = "//li[@id='menu-item-79']"
    main_word = "//h1[@class='heading-3 title']"

    # Getters

    def get_menu_item(self):
        return WebDriverWait(self.driver_g, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_item)))

    def get_main_word(self):
        return WebDriverWait(self.driver_g, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_menu_item(self):
        self.get_menu_item().click()
        print("Click menu_item")

    def get_assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good katalog')

    # Methods

    def category_product_select(self):
        with allure.step("Category_product_select"):
            Logger.add_start_step(method="Category_product_select")
            self.driver_g.get(self.url)
            self.driver_g.maximize_window()
            self.get_current_url()
            self.click_menu_item()
            self.get_assert_word(self.get_main_word(), 'Katalog kwiatów')
            Logger.add_end_step(url=self.driver_g.current_url, method="Category_product_select")
