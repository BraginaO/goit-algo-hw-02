import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації нових заявок
def generate_request():
    try:
        # Генеруємо унікальний номер заявки
        request_number = random.randint(1, 1000)
        # Додаємо заявку до черги
        request_queue.put(request_number)
        print("Заявка {} створена".format(request_number))
    except Exception as e:
        print("Помилка при генерації заявки:", e)

# Функція для обробки заявок
def process_request():
    try:
        if not request_queue.empty():
            # Видаляємо заявку з черги
            request_number = request_queue.get()
            print("Заявка {} оброблена".format(request_number))
        else:
            print("Черга порожня")
    except Exception as e:
        print("Помилка при обробці заявки:", e)

# Головний цикл програми
while True:
    try:
        # Генеруємо нові заявки
        generate_request()
        # Обробляємо заявки
        process_request()
        # Затримка для імітації часу обробки
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nПрограма завершує роботу за допомогою клавіш Ctrl+C.")
        break

