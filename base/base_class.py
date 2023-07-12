import pytz
from datetime import datetime
import allure

class Base():

    def __init__(self, driver_g):
        self.driver_g = driver_g

    def get_current_url(self):
        get_url = self.driver_g.current_url
        print("Current url " + get_url)

    def get_screenshot(self):
        """
        Method Screenshot
        """

    # Time_zone
        timezone = pytz.timezone("Europe/Warsaw")

    # Time

        now_date = datetime.now(timezone).strftime(" time in Warsaw %Y-%m-%d %H-%M")
        name_screenshot = 'finish_page' + now_date + '.png'

        self.driver_g.save_screenshot('screen\\' + name_screenshot)
    #
    def get_assert_url(self, result):
        """
        Method Assert url
        """
        get_url = self.driver_g.current_url
        assert get_url == result
        print('Good url')

