import pytest
import allure
from pages.order_page import HomePageScooter
from data.users import *

class TestOrderPage:
    @allure.title('Проверка верхней кнопки "Заказать"')
    @allure.description('На странице "Самокат" нажимаем на кнопку "Заказать", заполняем поля ввода и проверяем, что выпало окошко "Заказ оформлен" с двумя наборами данных')
    @pytest.mark.parametrize("name,last_name,address,phone,comment,date", TEST_DATA)
    def test_top_button_order_accepted_order(self, browser, name, last_name, address, phone, comment, date):
        page = HomePageScooter(browser)
        text = page.order_scooter_on_last_station(name=name, last_name=last_name, address=address, phone=phone, comment=comment, date=date)
        assert "Заказ оформлен" in text
    
    @allure.title('Проверка нижней кнопки "Заказать"')
    @allure.description('На странице "Самокат" нажимаем на кнопку "Заказать", заполняем поля ввода и проверяем, что выпало окошко "Заказ оформлен с двумя наборами данных"')
    @pytest.mark.parametrize("name,last_name,address,phone,comment,date", TEST_DATA)
    def test_lower_button_order_accepted_order(self, browser, name, last_name, address, phone, comment, date):
        page = HomePageScooter(browser)
        text = page.order_scooter_on_first_station(name=name, last_name=last_name, address=address, phone=phone, comment=comment, date=date)
        assert "Заказ оформлен" in text