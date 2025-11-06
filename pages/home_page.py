from locators.home_page_locators import *
from locators.base_page_locators import *
from urls import *
import allure
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePageScooter(BasePage):

    def __init__(self, driver):
        super().__init__(driver) 

    @allure.step('Скролл до списка вопросов')
    def scroll_question(self, index):
        element = self.find_element(questions[index])
        self.execute_js_scroll_into_view(element)
    
    @allure.step('Клик на вопрос')
    def click_question(self, index):
        element = self.wait_for_element_clickable(questions[index])
        element.click()

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, index):
        return self.find_element(answers[index]).text
    
    @allure.step('Клик на кнопку "да все привыкли"')
    def click_button_cookie_banner(self):
        self.find_element(button_cookie).click()
    
    @allure.step('Клик на логотип "Самокат"')
    def click_logo_scooter(self):
        self.find_element(scooter_logo).click()
        return self.driver.current_url
    
    @allure.step('Верификация полученного ответа с правильным')
    def verify_question_answer(self, index):
        self.click_button_cookie_banner()
        self.scroll_question(index)
        self.click_question(index)
        return self.find_element(answers[index]).text
    
    @allure.step('Клик на логотип Яндекса и проверка адреса новооткрывшейся страницы на Дзен')
    def click_logo_yandex_and_check_url(self):
        self.find_element(yandex_logo).click()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(EC.url_contains(DZEN_URL))
        return self.driver.current_url