import random
import tkinter as tk
from tkinter import messagebox

# Функція для перевірки введеного користувачем числа
def check_number():
    try:
        user_input = int(entry.get())
        if user_input == stored_number + random_number:
            messagebox.showinfo("Результат", "Число введено правильно!")
        else:
            messagebox.showerror("Результат", "Число введено неправильно.")
    except ValueError:
        messagebox.showerror("Помилка", "Неправильний формат введеного числа.")

# Створення вікна
window = tk.Tk()
window.title("Перевірка числа")

# Зчитування числа з файлу (якщо існує)
try:
    with open('number.txt:only', 'r') as file:
        stored_number = int(file.read())
except FileNotFoundError:
    messagebox.showerror("Помилка", "Файл 'number.txt' не знайдено.")
    stored_number = None
except ValueError:
    messagebox.showerror("Помилка", "Неправильний формат числа у файлі.")
    stored_number = None

if stored_number is not None:
    # Генерування рандомного числа
    random_number = random.randint(1, 100)

    # Вивід графічного інтерфейсу
    label_random = tk.Label(window, text=f"Згенероване рандомне число: {random_number}")
    label_random.pack()

    label_instruction = tk.Label(window, text="Введіть число, яке повинно бути рівним сумі чисел:")
    label_instruction.pack()

    entry = tk.Entry(window)
    entry.pack()

    check_button = tk.Button(window, text="Перевірити", command=check_number)
    check_button.pack()

# Запуск головного циклу tkinter
window.mainloop()
