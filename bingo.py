import tkinter as tk
import random

root = tk.Tk() #ウィンドウの部品を作る
root.title("bingo!")
root.geometry("500x460")
root["bg"]="white"
BG = ('white')
FNT = ("Times New Roman",100)
FN = ("Times New Roman",25)

numbers = list(range(1,76))#75個の数字が入った箱
random.shuffle(numbers)#混ぜる

def sai():
		random.shuffle(numbers)
		poped_num = numbers.pop(0)#１つ削除
		la['text'] = poped_num#削除する数字を表示
		la2['text'] = numbers#残りの数字リストの表示

def reset():
		numbers.clear()
		numbers.extend(list(range(1,76)))
		random.shuffle(numbers)

def shuffle():
		random.shuffle(numbers)

c0 = tk.Canvas(root, bg = '#0B8EE3', width = 50, height = 20)
id = c0.create_text(20, 20,fill = 'white')
c0.pack(fill = tk.BOTH, expand = True)

def change_size(event):
    w = c0.winfo_width()
    h = c0.winfo_height()
    c0.coords(id, 20, 20, w - 20, h - 20)

# バインディングの設定
root.bind('<Configure>', change_size)

la = tk.Label(text="◆", font=FNT, bg=BG, fg="black")
la.pack(expand=True, fill=tk.BOTH)

la2 = tk.Label(text="残り", font=FN, bg=BG, fg="#0B8EE3",wraplength=350)
la2.pack(expand=True, fill=tk.BOTH)

c2 = tk.Canvas(root, bg = '#0B8EE3', width = 50, height = 20)
c2.pack(fill = tk.BOTH, expand = True)

bu1 = tk.Button(text="Bingo", bg=BG, command=sai)
bu1.pack(expand=True, fill=tk.BOTH)

bu2 = tk.Button(text="リセット", bg=BG, command=reset)
bu2.pack(expand=True, fill=tk.BOTH)

bu3 = tk.Button(text="シャッフル", bg=BG, command=shuffle)
bu3.pack(expand=True, fill=tk.BOTH)

root.mainloop()