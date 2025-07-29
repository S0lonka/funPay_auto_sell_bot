from winotify import Notification

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



class Funpay_notification():
    """Класс отправки уведомлений windows"""
    def __init__(self):
        self.app_name = "FunPay AUTO"                                # Имя приложения
        self.notification_flag = NOTIFICATION_FLAG                   # Флаг уведомлений из конфига
        self.icon_path = fr"{os.getcwd()}\app\img\icon\funPay.ico"   # Путь до иконки


    def send_notification(self, 
                          title    : str, 
                          msg      : str, 
                          duration : str = "short"
                          ) -> None:
        
        if NOTIFICATION_FLAG and duration in ["short", "long"]:
            try:
                self.toast = Notification(
                    app_id   = self.app_name,   # Имя приложения
                    title    = title,           # Заголовок уведомления
                    msg      = msg,             # Основное сообщение
                    duration = duration,        # Длительность в секундах
                    icon     = self.icon_path   # Путь к иконке (опционально)
                )

                self.show_notification()
                
            except Exception as e:
                logging.error(f"Ошибка уведомлений: {e}")
        else:
            logging.warning(f"Уведмления отключены: уведомление {title} не отправлено")


    def show_notification(self) -> None:
        self.toast.show()  #  Отображаем уведомление