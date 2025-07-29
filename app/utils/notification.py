from winotify import Notification

from typing import Self

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



class Funpay_notification:
    """Класс отправки уведомлений windows"""
    def __init__(self):
        self.app_name = "FunPay AUTO"                                # Имя приложения
        self.notification_flag = NOTIFICATION_FLAG                   # Флаг уведомлений из конфига
        self.icon_path = fr"{os.getcwd()}\app\img\icon\funPay.ico"   # Путь до иконки


    def send_notification(self, 
                        title    : str, 
                        msg      : str, 
                        duration : str = "short"
                        ) -> Self:
        """Отправка уведомления с обработкой ошибок.
    
        Args:
            title    (str) : Заголовок уведомления
            msg      (str) : Текст сообщения
            duration (str) : Длительность ("short" или "long")
        
        Return:
            self : Объект класса для его дальнейшего использования
        """

        # Валидация параметров перед выполнением
        if not NOTIFICATION_FLAG:
            logger.warning(f"Уведомления отключены: '{title}' не отправлено")
            return self
                
        if duration not in ("short", "long"):
            logger.error(f"Некорректная длительность: {duration}")
            return self  # Проверка что уведомления включены И duration указано верно
        

        try:
            # Конструктор уведомления
            self.toast = Notification(
                app_id   = self.app_name,   # Имя приложения
                title    = title,           # Заголовок уведомления
                msg      = msg,             # Основное сообщение
                duration = duration,        # Длительность в секундах
                icon     = self.icon_path   # Путь к иконке (опционально)
            )

            return self
        
        except Exception as e:
            logger.error(f"Ошибка уведомлений: {e}")
            return self
            




    def add_actions(self,
                    label : str,
                    launch: str
                    ) -> Self:
        """Добавление действия(кнопки) к уведомлению

        Args:
            label  (str) : Текст кноки
            launch (str) : Ссылка кнопки (также можно использовать file:///)

        Return:
            self : Объект класса для его дальнейшего использования
        """
        try:
            self.toast.add_actions(
                label=label,
                launch=launch
            )
            return self
        
        except Exception as e:
            logger.error(f"Ошибка уведомлений(add_actions): {e}")
            return self
            

    def show(self) -> None:
        """Отображает собранное уведомление"""
        self.toast.show()  #  Отображаем уведомление
        logger.info(f"Показано уведомление | {self.toast.title} |")
        