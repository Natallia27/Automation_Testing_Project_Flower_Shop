import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from pages.category_page import CategoryPage
from pages.clientpage import ClientPage
from pages.page_cart import CartPage
from pages.page_main import MainPage
from pages.productpage import ProductPage


def test_category_select():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('C:\\Users\\natal\\PycharmProjects\\resource\\chromedriver.exe')
    driver_g = webdriver.Chrome(options=options, service=g)
    print('Start test 1')

    pm = MainPage(driver_g)
    pm.category_product_select()

    cp = CategoryPage(driver_g)
    cp.category_product_select()

    pp = ProductPage(driver_g)
    pp.product_add()

    pc = CartPage(driver_g)
    pc.cart_sum()

    clp = ClientPage(driver_g)
    clp.input_client_info()

    print(pp.price_value)
    print(clp.price_cart_value)
    pp.price_value_changed = pp.price_value.replace("ZŁ", "")
    print(float(pp.price_value_changed))
    clp.price_cart_value_changed = clp.price_cart_value.replace("zł", "")
    print(float(clp.price_cart_value_changed))
    assert pp.price_value_changed == clp.price_cart_value_changed
    print("Price assert good")
    print('Finish test 1')
    time.sleep(10)
    driver_g.quit()



