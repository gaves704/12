from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера
driver = webdriver.Chrome()

try:
    # Открытие главной страницы
    driver.get("https://author.today/")

    # Ожидание загрузки шапки сайта и нахождение элемента "Обсуждение"
    wait = WebDriverWait(driver, 10)
    navbar = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "nav.navbar.topnavbar")))

    # Нахождение и клик по разделу "Обсуждение" с использованием CSS-селектора
    discussion_link = driver.find_element(By.CSS_SELECTOR, "a[href='/discussions']")
    discussion_link.click()

    # Ожидание загрузки страницы "Обсуждение"
    discussion_list = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.page-discussions")))

    # Проверка, что страница "Обсуждение" загружена
    assert "discussions" in driver.current_url

    # Нахождение и клик по кнопке "Читать дальше" для самого первого обсуждения
    read_more_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-default-sm")))
    read_more_button.click()

    # Ожидание загрузки страницы первого обсуждения
    discussion_content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".discussion-content")))

    # Проверка, что страница обсуждения загружена
    assert "discussion" in driver.current_url

    print("Тест пройден успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()