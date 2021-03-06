from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаем кнопку.
    button = browser.find_element_by_css_selector(".btn")
    button.click()

    first_window = browser.window_handles[0]  # Первая по счёту вкладка
    new_window = browser.window_handles[1]  # Вторая по счёту вкладка

    # Переключиться на вторую вкладку
    browser.switch_to.window(new_window)

    # вытаскиваю значение X из текста и произвожу математическое вычисление
    x_value = browser.find_element_by_css_selector('#input_value')
    x = x_value.text
    y = calc(x)

    #Получаю данные для заполнения формы с ответом
    firstname = browser.find_element_by_css_selector('#answer')
    firstname.send_keys(y)

    button = browser.find_element_by_css_selector(".btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

