import tkinter as tk

root = tk.Tk()

root.title('Угадай цвет светофора')

root.geometry('350x200')

label = tk.Label(root, text="Введите цвет светофора:")
label.pack(pady=(30, 10))

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

def check_color():
    user_input = entry.get().strip()
    user_input_lower = user_input.lower()

    if user_input_lower == 'красный'
        messagebox.showinfo("Результат", "✅ Верно! Красный — стоп!")
        elif user_input_lower == "желтый":
        messagebox.showinfo("Результат", "⚠️ Верно! Желтый — внимание!")
    elif user_input_lower == "зеленый":
        messagebox.showinfo("Результат", "✅ Верно! Зеленый — можно ехать!")
    else:
        # Если введено что-то другое
        messagebox.showerror("Результат", "❌ Неверно. Попробуй еще раз!")

btn_check = tk.Button(root, text="Проверить", command=check_color)
btn_check.pack(pady=10)



root.mainloop()