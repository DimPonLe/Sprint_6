from selenium.webdriver.common.by import By

questions = [(By.ID, f"accordion__heading-{i}") for i in range(0, 8)]
answers = [(By.ID, f"accordion__panel-{i}") for i in range(0, 8)]
button_lower = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
button_cookie = [By.XPATH, ".//button[@class='App_CookieButton__3cvqF']"]