Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import requests
import json

root =tk.Tk()
root.title('Find JSON GitHub')
mystring =tk.StringVar(root)
stroka = []
def GetValue():
    stroka.append(mystring.get())
    messagebox.showinfo('Поиск', 'Данные записаны в текстовый файл')

t1 = Label(root, text='Введите название репозитория').pack()
e1 = Entry(root, textvariable = mystring, width=50).pack()
button1 = tk.Button(root, text='Поиск',height = 1, width = 10, command=GetValue).pack()


root.mainloop()

def GetNameGitHub(spisok: []):
    global name
    for i in spisok:
        name = i
    return name

def OutputFile(file: str, result: {}):
    FileOutPut = open(file, mode='w')
    FileOutPut.write(result)
    FileOutPut.close()

json_dict = {
    'company': '',
    'created_at': '',
    'email': '',
    'id': '',
    'name': '',
    'url': ''
}

name = ''
user_name = GetNameGitHub(stroka)
url = f'https://api.github.com/users/{user_name}'
response = requests.get(url)
json_text = response.json()

for letter in json_text:
    if letter in json_dict:
        json_dict[letter] = json_text[letter]



with open('JSON_GitHub.txt', 'w') as convert_file:
    for key, value in json_dict.items():
        convert_file.write(f'{key}: {value}\n')

