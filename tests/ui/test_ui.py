import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# import time

@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    

    # відкриваємо сторінку https://github.com/login
    driver.get("https://github.com/login")
    

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача або поштову адресу
    login_elem = driver.find_element(By.ID, "login_field" )

    # Вводимо неправильне ім'я користувача або поштову адресу
    login_elem.send_keys("sergiibutenko@mistakeinemail.com")
    
    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("123456789")

    # Знаходимо кнопку "Sign in" та натискаємо на неї
    sign_in_elem = driver.find_element(By.CLASS_NAME, "js-sign-in-button")
    sign_in_elem.click()
    
    # Перевіряємо, що з'явилося повідомлення про помилку
    error_elem = driver.find_element(By.CLASS_NAME, "js-flash-alert")
    error_text = error_elem.text

    # Перевіряємо що назва сторінки така,яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"
    # time.sleep(3) # Затримка для перевірки, що сторінка завантажилася

    # Перевіряємо, що повідомлення про помилку відображається
    # і що його текст відповідає очікуваному
    assert error_elem.is_displayed() == True
    assert error_text.startswith("Incorrect username or password.") == True



    # закриваємо браузер
    driver.close()

