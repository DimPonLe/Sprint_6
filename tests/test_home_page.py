import pytest
import allure
from urls import *
from pages.home_page import HomePageScooter
from data.expected_answers import EXPECTED_ANSWERS

class TestHomePage:
    @allure.title('Проверка, что при нажатии на стрелочку открывается соответствующий текст')
    @allure.description('На странице ищем список вопросов, нажимаем на каждый из них и сравниваем ответы')
    @pytest.mark.parametrize("index, expected_answer", enumerate(EXPECTED_ANSWERS))
    def test_verify_all_questions(self, browser, index, expected_answer):
        page = HomePageScooter(browser)
        actual_answer = page.verify_question_answer(index)
        assert actual_answer == expected_answer
    
    @allure.title('Проверка, что при нажатии на логотип "Самокат" попадаешь на главную страницу')
    @allure.description('На домашней странице "Самокат" нажимает на логотип')
    def test_click_logo_scooter_page_scooter(self, browser):
        page = HomePageScooter(browser)
        current_url = page.click_logo_scooter()
        assert current_url == HOME_URL

    @allure.title('Проверка, что при нажатии на логотип Яндекса появляется новая страница Дзена')
    @allure.description('На домашней странице "Самокат" нажимаем на логотип Яндекса и проверяем адрес новой страницы')
    def test_click_logo_yandex_page_dzen(self, browser):
        page = HomePageScooter(browser)
        current_url = page.click_logo_yandex_and_check_url()
        assert DZEN_URL in current_url