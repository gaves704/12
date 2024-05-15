from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

# Инициализация веб-драйвера
driver = webdriver.Chrome()

try:
    # Открытие главной страницы
    driver.get("https://author.today/")

    # Ожидание загрузки шапки сайта и нахождение элемента "Обсуждение"
    wait = WebDriverWait(driver, 10)
    navbar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "nav.navbar.topnavbar")))

    # Нахождение и клик по разделу "Каталог"
    catalog_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Книги")
    catalog_link.click()

    # Ожидание загрузки страницы "Каталог"
    catalog_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.page-catalog")))

    # Нахождение и клик по разделу "Фантастика"
    fantasy_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Фантастика")
    fantasy_link.click()

    # Ожидание загрузки страницы "Фантастика"
    fantasy_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.page-genre")))

    print("Тест пройден успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()