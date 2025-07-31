def str_to_bool(value: str | None) -> bool:
    """Перевод из строки в булевое значение
    
    Args:
        value (str | None) : Строка которую нужно преобразовать в bool.
        
    Returns:
        bool : Проверяет на true, в остальных случаях возвращает False."""
    
    if value is None:
        return False
    
    if isinstance(value, str):
        value = value.strip().lower()
        if value in ('true', '1', 'on', 'yes'):
            return True
        else:
            return False
    else:
        return False
