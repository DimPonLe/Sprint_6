from selenium.webdriver.common.by import By

# Окошко "Для кого самокат"
name_input = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]
last_name_input = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]
address_input = [By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]
station_metro = [By.CLASS_NAME, "select-search__input"]
first_station_metro = [By.XPATH, ".//div[@class='select-search__select']/ul/li[1]"]
last_station_metro = [By.XPATH, ".//div[@class='select-search__select']/ul/li[last]"]
number_phone_input = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]
button_next = [By.XPATH, ".//button[text()='Далее']"]

# Окошко "Про аренду"
date_input = [By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"]
time_rent = [By.CLASS_NAME, "Dropdown-control"]
first_time_rent = [By.XPATH, ".//div[@class='Dropdown-option'][1]"]
last_time_rent = [By.XPATH, ".//div[@class='Dropdown-option'][7]"]
color_black_pearl = [By.ID, "black"]
color_grey_hopelessness = [By.ID, "grey"]
comment_input = [By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']"]
button_order = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

# Окошко "Хотите оформить заказ?"
button_yes = [By.XPATH, ".//button[text()='Да']"]

# Окошко "Заказ оформлен" с номером заказа
header_order_accept = [By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ']"]