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
        """Отправка уведомления с обработкой ошибок.
    
        Args:
            title: Заголовок уведомления
            msg: Текст сообщения
            duration: Длительность ("short" или "long")
        """

        # Валидация параметров перед выполнением
        if not NOTIFICATION_FLAG:
            logging.warning(f"Уведомления отключены: '{title}' не отправлено")
            return
                
        if duration not in ("short", "long"):
            logging.error(f"Некорректная длительность: {duration}")
            return  # Проверка что уведомления включены И duration указано верно
        

        try:
            # Конструктор уведомления
            self.toast = Notification(
                app_id   = self.app_name,   # Имя приложения
                title    = title,           # Заголовок уведомления
                msg      = msg,             # Основное сообщение
                duration = duration,        # Длительность в секундах
                icon     = self.icon_path   # Путь к иконке (опционально)
            )


        except Exception as e:
            logging.error(f"Ошибка уведомлений: {e}")
            
        finally:
            self.show_notification() # отображаем уведомление




    def add_actions_notification(self,
                                label : str,
                                launch: str):
        self.toast.add_actions(
            label=label,
            launch=launch
        )




    def show_notification(self) -> None:
        self.toast.show()  #  Отображаем уведомление
        logging.info(f"Показано уведомление | {self.toast.title} |")