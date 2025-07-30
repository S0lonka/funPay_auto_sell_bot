from winotify import Notification

from typing import Self

import logging
import os

from app.config.config import SHOW_NOTIFICATION


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

logger = logging.getLogger('notification')



class Funpay_notification:
    """Класс отправки уведомлений windows"""
    def __init__(self):
        self.app_name = "FunPay AUTO"                                # Имя приложения
        self.show_notification = SHOW_NOTIFICATION                   # Флаг уведомлений из конфига
        self.icon_path = fr"{os.getcwd()}\app\img\icon\funPay.ico"   # Путь до иконки


    def send_notification(self, 
                        title     : str, 
                        msg       : str, 
                        duration  : str  = "short",
                        important : bool = False
                        ) -> Self:
        """Конструктор уведомления.
    
        Args:
            title     (str)  : Заголовок уведомления.
            msg       (str)  : Текст сообщения.
            duration  (str)  : Длительность ("short" или "long").
            important (bool) : True чтобы собрать уведомление даже если они отключены.
        
        Returns:
            self : Объект класса для его дальнейшего использования
        """

        
        # Если это не важное уведомление(которое срабатывает даже при отключённых уведомлениях) И
        if (not important) and (not SHOW_NOTIFICATION):   # Состояние уведомления ON / OFF (True / False)
            logger.warning(f"Уведомления отключены: '{title}' не собрано для отправки.")
            self.toast = None   # явно кказываем уведомление не собранным
            return self
                
        if duration not in ("short", "long"):
            logger.warning(f"Некорректная длительность: {duration} - автоматически изменено на > short.")
            duration = "short"
        

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
            logger.error(f"Ошибка уведомлений: {e}.")
            
        finally:
            return self




    def add_actions(self,
                    label : str,
                    launch: str
                    ) -> Self | None:
        """Добавление действия(кнопки) к уведомлению

        Args:
            label  (str) : Текст кноки
            launch (str) : Ссылка кнопки (также можно использовать file:///)

        Returns:
            self : Объект класса для его дальнейшего использования
        """
        if hasattr(self, 'toast') and self.toast is not None: 
            try:
                self.toast.add_actions(
                    label=label,
                    launch=launch
                )
            
            except Exception as e:
                logger.error(f"Ошибка уведомлений(add_actions): {e}")
            
            finally:
                return self

            
    def _skip(self) -> "Self":
        """Заглушка для пропуска последующих вызовов (например, .show())."""
        logger.info("сработала заглушка")
        return self

    def show(self) -> None:
        """Отображает собранное уведомление
        
        Return:
            None
        """
        if hasattr(self, 'toast') and self.toast is not None:  # Проверка что toast принадлежит классу и != None
            self.toast.show()  #  Отображаем уведомление
            logger.info(f"Показано уведомление | {self.toast.title} |")

        