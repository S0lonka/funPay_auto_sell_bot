# Notification (Уведомления)
Пример использования
```python
from app.utils.notification import Funpay_notification

FN = (Funpay_notification()
    .send_notification("hi", "how are you", duration="short")
    .add_actions("go", "https://funpay.com/")
    .show())
```
