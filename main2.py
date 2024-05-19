import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import requests

def sort_words():
    words = input_area.get("1.0", "end-1c").split()
    if len(words) == 0:
        messagebox.showerror('Ошибка', 'Введите данные для сортировки!')
    else:
        sorted_words = sorted(words)
        output_area.delete(1.0, "end")
        for word in sorted_words:
            output_area.insert("end", word + '\n')

def check_update():
    try:
        response = requests.get('https://raw.githubusercontent.com/Chinchoppa7/rep2/main/version.txt')
        if version == response.text:
            messagebox.showinfo("Обновление ПО", "Программа не требует обновления")
            return
        else:
            user_input = messagebox.askquestion("Обновление ПО", "Обнаружено обновление. Хотите обновить программу?")
            if user_input == "yes":
                download_update()
    except requests.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось проверить обновления: {e}")

def download_update():
    try:
        response = requests.get('https://raw.githubusercontent.com/Chinchoppa7/rep2/main/main.py')
        with open('main.py', 'wb') as f:
            f.write(response.content)
        messagebox.showinfo("Обновление ПО", "Программа успешно обновлена. Перезапустите приложение.")
    except requests.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось загрузить обновление: {e}")

root = tk.Tk()
root.title("Сортировка слов")
root['bg']='#363535'
version = 'Версия - 4.0'
input_area = scrolledtext.ScrolledText(root, width=30, font=('Arial, 14'), height=10,
bg='#262626', fg='white', selectbackground='#ebb45b', wrap=tk.WORD)
input_area.grid(row=1, column=0, padx=10, pady=10)

sort_button = tk.Button(root, text="Сортировать", font=('Arial, 14'),relief='ridge',bd=0, bg='#ed980e',fg='white',activeforeground='white',activebackground='#ffb53d',  command=sort_words)
sort_button.grid(row=2, column=0, padx=10, pady=10)

output_area = scrolledtext.ScrolledText(root, width=30,font=('Arial, 14'),height=10, bg='#262626',fg='white',selectbackground='#ebb45b', wrap=tk.WORD)
output_area.grid(row=3, column=0, padx=10, pady=10)

updateButton = tk.Button(root, text="Обновить", font=('Arial, 14'),relief='ridge',bd=0, bg='#ed980e',fg='white',activeforeground='white',activebackground='#ffb53d',  command=check_update)
updateButton.grid(row=0,column=0, sticky='w')

versionLabel = tk.Label(root, text=version, font=('Arial, 12'), bg='#363535',fg='white')
versionLabel.grid(row=0,column=0, sticky='e')
root.mainloop()