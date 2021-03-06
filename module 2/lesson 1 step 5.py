from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # вытаскиваю значение X из текста и произвожу математическое вычисление.
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # вставляю полученное значение в поле
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    # кликаю на чекбокс
    input_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    input_checkbox.click()

    # переставляю радиобаттон
    input_radiobutton = browser.find_element_by_css_selector('#robotsRule')
    input_radiobutton.click()

    # submit
    submit = browser.find_element_by_css_selector(".btn")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()