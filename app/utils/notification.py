from win10toast import ToastNotifier

import logging
import os

from app.config.config import NOTIFICATION_FLAG


# Настройка логгера
logging.basicConfig(
    level=logging.INFO,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - | %(levelname)s | -> %(message)s',
    handlers=[
        logging.FileHandler('funPay.log'),  # Логи в файл
        logging.StreamHandler()             # Логи в консоль
    ]
)
logger = logging.getLogger('notification')


class Notification():
    """Класс отправки уведомлений windows"""
    def __init__(self):
        self.notification_flag = NOTIFICATION_FLAG  # Флаг уведомлений из конфига
        self.toaster = ToastNotifier()              # Модель класса уведомлений
        self.icon_path = fr"{os.getcwd()}\app\img\icon\funPay.ico"                 # Путь до иконки


    def send_notification(self, title: str, msg: str, duration: int = 10):
        if NOTIFICATION_FLAG:
            try:
                self.toaster.show_toast(
                    title=title,
                    msg=msg,
                    duration=duration,        # Длительность в секундах
                    icon_path=self.icon_path, # Путь к иконке (опционально)
                    threaded=True             # Показ уведомления в другом потоке (асинхронно)
                )
            except Exception as e:
                logging.error(f"Ошибка уведомлений: {e}")
        else:
            logging.warning(f"Уведмления отключены: уведомление {title} не отправлено")