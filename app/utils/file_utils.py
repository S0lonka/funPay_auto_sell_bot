from pathlib import Path
import logging

from app.template.env_content import config_env_lines

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
logger = logging.getLogger('file_utils')


def check_file(path: str) -> bool:
    """Проверка что файл существует
    
    Args:
        path  (str) : Путь до файла который нужно проверить.
    
    Return:
        bool
    """
    if Path(path).is_file():
        return True
    else:
        create_file(path, config_env_lines)
        logger.warning(f"Создан файл по пути: {path}")
        return False
    

def create_file(filepath: str, line_content: list[str]) -> None:
    """Создаёт и записывает файл
    Args:
        filepath     (str)       : Путь до целевого файла
        line_content (list[str]) : Массив строк которыми заполнится файл
    
    Return:
        None
    """

    with open(filepath, "w", encoding="UTF-8") as file:
        file.writelines('\n'.join(line_content))



