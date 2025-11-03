from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.home_page_locators import *
from locators.order_page_locators import *
from locators.base_page_locators import *
import allure

class OrderPageScooter:
    def __init__(self, driver):
        self.driver = driver 

    @allure.step('Клик на верхнюю кнопку "Заказать"')    
    def click_button_top(self):
        self.driver.find_element(*button_top).click()

    @allure.step('Скролл до нижней кнопки "Заказать" и клик на неё') 
    def scroll_and_click_button_lower(self):
        button = self.driver.find_element(*button_lower)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
        button.click()

    @allure.step('Заполнение поля ввода "Имя"') 
    def set_name(self, name):
        self.driver.find_element(*name_input).send_keys(name)

    @allure.step('Заполнение поля ввода "Фамилия"') 
    def set_last_name(self, last_name):
        self.driver.find_element(*last_name_input).send_keys(last_name)

    @allure.step('Заполнение поля ввода "Адрес"') 
    def set_address(self, address):
        self.driver.find_element(*address_input).send_keys(address)

    @allure.step('Выбор станции метро') 
    def choiсe_first_station_metro(self):
        self.driver.find_element(*station_metro).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(first_station_metro))
        self.driver.find_element(*first_station_metro).click()
    
    @allure.step('Заполнение поля ввода "Телефон"') 
    def set_number_phone(self, phone):
        self.driver.find_element(*number_phone_input).send_keys(phone)

    @allure.step('Клик на кнопку "Далее"') 
    def click_button_next(self):
        self.driver.find_element(*button_next).click()

    @allure.step('Заполнение поля ввода "Дата"') 
    def set_date_input(self, date):
        self.driver.find_element(*date_input).send_keys(date)

    @allure.step('Выбор срока аренды: сутки') 
    def choice_first_time_rent(self):
        self.driver.find_element(*time_rent).click()
        self.driver.find_element(*first_time_rent).click()

    @allure.step('Выбор срока аренды: семеро суток') 
    def choice_last_time_rent(self):
        self.driver.find_element(*time_rent).click()
        element = self.driver.find_element(*last_time_rent)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step('Выбор цвета самоката: черный') 
    def choice_color_black_pearl(self):
        self.driver.find_element(*color_black_pearl).click()

    @allure.step('Выбор цвета самоката: серый') 
    def choice_color_grey_hopelessness(self):
        self.driver.find_element(*color_grey_hopelessness).click()

    @allure.step('Заполнение поля ввода "Комментарий"') 
    def set_comment_input(self, comment):
        self.driver.find_element(*comment_input).send_keys(comment)

    @allure.step('Клик на кнопку "Заказать"') 
    def click_button_order(self):
        self.driver.find_element(*button_order).click()

    @allure.step('Клик на кнопку "Да"') 
    def click_button_order_yes(self):
        self.driver.find_element(*button_yes).click()

    @allure.step('Получение текста о принятии заказа') 
    def get_text_about_order_accept(self):
        return self.driver.find_element(*header_order_accept).text

    @allure.step('Заказ самоката черного цвета на станцию метро "Лихоборы"') 
    def order_scooter_on_last_station(self, name, last_name, address, phone, comment, date):
        self.click_button_top()
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.choiсe_first_station_metro()
        self.set_number_phone(phone)
        self.click_button_next()
        self.choice_last_time_rent()
        self.choice_color_black_pearl()
        self.set_comment_input(comment)
        self.set_date_input(date)
        self.click_button_order()
        self.click_button_order_yes()
        return self.get_text_about_order_accept()
    
    @allure.step('Заказ самоката серого цвета на станцию метро "Бульвар Рокоссовского"') 
    def order_scooter_on_first_station(self, name, last_name, address, phone, comment, date):
        self.scroll_and_click_button_lower()
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.choiсe_first_station_metro()
        self.set_number_phone(phone)
        self.click_button_next()
        self.choice_first_time_rent()
        self.choice_color_grey_hopelessness()
        self.set_comment_input(comment)
        self.set_date_input(date)
        self.click_button_order()
        self.click_button_order_yes()
        return self.get_text_about_order_accept()