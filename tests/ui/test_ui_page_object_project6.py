from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import pytest
import time

class UZ_booking(BasePage):
    URL = 'https://booking.uz.gov.ua/'

    def __init__(self) -> None:
        super().__init__()

    # Метод який відкриває сторінку по заданому юрл
    def go_to(self):
        self.driver.get(UZ_booking.URL)

    # Метод що встановлює значення відправлення
    def try_set_departure(self, depart_city):
        depart_elem = self.driver.find_element(By.ID, "headlessui-combobox-input-v-0-0-0")

        depart_elem.send_keys(depart_city)
        time.sleep(2)

        select_option = self.driver.find_element(By.CSS_SELECTOR, "ul[role=listbox] > li:first-child")
        select_option.click()
    
    # Метод що встановлює значення прибуття
    def try_set_arrival(self, arrival_city):
        arrival_elem = self.driver.find_element(By.ID, "headlessui-combobox-input-v-0-0-3")

        
        arrival_elem.send_keys(arrival_city)
        time.sleep(2)

        select_option = self.driver.find_element(By.CSS_SELECTOR, "ul[role=listbox] > li:first-child")
        select_option.click()

    # Метод що знаходить та клікає кнопку Знайти
    def button_find(self):
        button = self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
        button.click()

    # Метод що перевіряє title html сторінки
    def check_title(self, expected_title):
        return self.driver.title == expected_title

# Проєктне завдання № 6
@pytest.mark.uz
def test_find_tickets():
    UZ_page = UZ_booking()

    UZ_page.go_to()

    UZ_page.try_set_departure("Київ-Пасажирський")
    time.sleep(3)

    UZ_page.try_set_arrival("Львів")
    time.sleep(3)

    UZ_page.button_find()
    time.sleep(3)

    page_title_is_correct = UZ_page.check_title("Квитки на потяг Київ-Пас — Львів | Укрзалізниця: квитки на потяг")

    assert page_title_is_correct == True
