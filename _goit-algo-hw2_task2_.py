from collections import deque


def is_palindrome(s) :
    # Видаляємо пробіли та переводимо всі символи у нижній регістр
    s = s.replace(" ", "").lower()

    # Створюємо двосторонню чергу та додаємо всі символи рядка до неї
    char_queue = deque(s)

    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1 :
        if char_queue.popleft() != char_queue.pop() :
            return False

    # Якщо всі символи збігаються, то рядок є паліндромом
    return True


# Приклад використання
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))  # True
