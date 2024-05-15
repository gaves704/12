from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Инициализация WebDriver
driver = webdriver.Chrome()

try:
    # Предусловие: Пользователь авторизирован на сайте и находится в выбранном разделе (sci-fi)
    driver.get("https://author.today/work/genre/sci-fi")

    # Шаг 1: Поиск книги внутри указанных элементов
    try:
        panel_bodies = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "panel-body")))
        # Перебираем все элементы panel-body
        for panel_body in panel_bodies:
            # Ищем книги внутри каждого элемента panel-body
            books = panel_body.find_elements(By.CLASS_NAME, "book-row")
            # Перебираем все найденные книги
            for book in books:
                # Находим ссылку на книгу
                book_link = book.find_element(By.TAG_NAME, "a")
                # Получаем ссылку на книгу
                book_url = book_link.get_attribute("href")
                # Открываем ссылку на книгу
                driver.get(book_url)
                # Ожидание загрузки страницы чтения книги
                WebDriverWait(driver, 10).until(EC.url_contains("/read/"))
                # Находим элемент book-action-panel
                book_action_panel = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "book-action-panel")))
                # Находим кнопку "Чтение фрагмента" внутри book-action-panel
                read_fragment_button = book_action_panel.find_element(By.CSS_SELECTOR, "a.btn.btn-block.btn-primary.btn-real-book.mt-lg")
                read_fragment_button.click()
                print(f"Книга '{book_link.text}' успешно открыта для чтения фрагмента.")
    except TimeoutException:
        raise NoSuchElementException("Книги не найдены на странице")

    print("Тест успешно выполнен: Все книги успешно открыты для чтения фрагмента.")

except NoSuchElementException as e:
    print(f"Ошибка: {e}")

except TimeoutException:
    print("Ошибка: Элемент не найден. Возможно, страница не загрузилась за отведенное время.")

finally:
    # Закрыть браузер после выполнения теста
    driver.quit()