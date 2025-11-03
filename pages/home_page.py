from locators.home_page_locators import *
from locators.base_page_locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urls import *
import allure

class HomePageScooter:

    def __init__(self, driver):
        self.driver = driver 

    @allure.step('Скролл до списка вопросов')
    def scroll_question(self, index):
        element = self.driver.find_element(*questions[index])
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Клик на вопрос')
    def click_question(self, index):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(questions[index]))
        element.click()

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, index):
        return self.driver.find_element(*answers[index]).text
    
    @allure.step('Клик на кнопку "да все привыкли"')
    def click_button_cookie_banner(self):
        self.driver.find_element(*button_cookie).click()
    
    @allure.step('Клик на логотип "Самокат"')
    def click_logo_scooter(self):
        self.driver.find_element(*scooter_logo).click()
        return self.driver.current_url
    
    @allure.step('Верификация полученного ответа с правильным')
    def verify_question_answer(self, index):
        self.click_button_cookie_banner()
        self.scroll_question(index)
        self.click_question(index)
        return self.driver.find_element(*answers[index]).text
    
    @allure.step('Клик на логотип Яндекса и проверка адреса новооткрывшейся страницы на Дзен')
    def click_logo_yandex_and_check_url(self):
        self.driver.find_element(*yandex_logo).click()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        WebDriverWait(self.driver, 10).until(EC.url_contains(DZEN_URL))
        return self.driver.current_url