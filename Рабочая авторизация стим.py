from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка для видимого режима
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Убираем headless режим
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

# Путь к вашему ChromeDriver
chrome_driver_path = 'C:/Users/User/.cache/selenium/chromedriver/win64/124.0.6367.155/chromedriver.exe'

# Запуск браузера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Переход на страницу входа
    driver.get("https://store.steampowered.com/login/")

    # Ожидание загрузки страницы и нахождение элементов логина и пароля
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text']._2eKVn6g5Yysx9JmutQe7WV")))
    password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']._2eKVn6g5Yysx9JmutQe7WV")))

    # Ввод логина и пароля
    username_input.send_keys("sulatevandrej07")
    password_input.send_keys("0p9o8i7u6yY")
    
    # Отправка формы
    password_input.send_keys(Keys.RETURN)

    # Ожидание успешного входа
    time.sleep(5)

    # Переход на страницу профиля пользователя
    driver.get("https://steamcommunity.com/profiles/76561199035908600/")

    # Ожидание загрузки страницы и нахождение элемента с именем пользователя
    persona_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "actual_persona_name")))

    # Получение текста элемента
    persona_name_text = persona_name.text
    print("Persona Name:", persona_name_text)

finally:
    # Закрытие браузера
    driver.quit()
