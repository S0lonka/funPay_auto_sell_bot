import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

# Ошибки
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException

import keyboard
import time
import logging
import sys

# My utils
from app.config.config import ENV_DIRECTORY
from app.utils.file_utils import check_file



# Настройка логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - | %(levelname)s | -> %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('funPay.log',  mode='w'),  # Логи в файл, перезаписываем каждый запуск
        logging.StreamHandler()                        # Логи в консоль
    ]
)
logger = logging.getLogger('main')


def main():
    driver = None
    try:
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        driver = uc.Chrome(options=options)

        stealth(driver,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            use_subprocess=True
        )

        driver.get("https://funpay.com")   # Открываем страницу
        time.sleep(4)                      # Ждём 5 секунд для прогрузки страницы

        # Проверяем заголовок страницы
        assert "FunPay — биржа игровых ценностей" in driver.title
        
        logger.info("НАЧАЛО РАБОТЫ - esc | Чтобы выйти")
        click_by_login(driver)


        while True:
            if keyboard.is_pressed('esc'):
                logger.info("Завершение программы")

                driver.close()
                time.sleep(2)
                driver = None
                break







    except (InvalidSessionIdException, WebDriverException) as e:
        driver = None                   # Если окно уже недоступно перехватываем его и удаляем driver

    except Exception as e:
        logger.error(f"ГЛОБАЛЬНАЯ ошибка: {e}")
        
    finally:
        if driver:
            logger.info(f"Driver status: {driver is not None}, закрываю вкладку")
            time.sleep(1)
            driver.close()  # Закрываем драйвер здесь

        sys.exit(0)



def click_by_login(driver: uc.Chrome) -> None:
    login = driver.find_element(By.CSS_SELECTOR, "a.menu-item-login")
    login.click()

    logger.info("Нажал на кнопку login")
    


if __name__ == "__main__":
    if check_file(fr"{ENV_DIRECTORY}\env.env"):
        main()