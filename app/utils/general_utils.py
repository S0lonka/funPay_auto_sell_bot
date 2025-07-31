import logging
import app.config.logger_config


#!---------- LOGGING ----------

def toggle_logging(logger: logging.Logger) -> None:
    """Отключенния логгирования - переданного логгера(По заданным значениям в logger_config)
    
    Args:
        logger (Logger) : Объект класса который нужно отключить.
        enable (bool)   : Переключатьль, при False отключает логгер.

    Return:
        None
    """

    _MISSING = object()    # Уникальный объект для определения ненайденых переменных

    upper_logger_name = logger.name.upper()                                 # Получаем имя логгера и переводим в верхний регистр
    enable = getattr(app.config.logger_config, upper_logger_name, _MISSING) # Передаём модуль, имя переменной которое ищем, Если ненайдено вернёт уникальный объект

    if enable is _MISSING:
        logger.warning(f"Переменная: {upper_logger_name} - Не найдена")
    else:
        logger.disabled = not enable    # Выключаем логгер(если enable = False)


def create_logger(
        name      : str,
        file_name : str = "funPay.log",
        level     : int = logging.INFO
        ) -> logging.Logger:
    """
    Создаёт логгер

    Args:
        name      (str) : Имя создаваемого логгера.
        file_name (str) : Имя файла куда будут записываться логи.
        level     (int) : Уровень логгирования от 0 до 50 или в виде logging.WARNING.

    Returns:
        Logger : Собранный экземпляр класса.
    """

    logging.basicConfig(
        level=level,  # Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format='%(asctime)s - %(name)s - | %(levelname)s | -> %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(file_name,  mode='w'),  # Логи в файл, перезаписываем каждый запуск
            logging.StreamHandler()                        # Логи в консоль
    ])
    return logging.getLogger(name)


logger = create_logger("general_utils")
toggle_logging(logger)



