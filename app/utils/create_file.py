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