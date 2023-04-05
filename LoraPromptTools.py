#MadeByBao
#免费软件，请勿倒卖
import tkinter as tk
from tkinter import filedialog

def browse_dir():
    dir_path = filedialog.askdirectory()
    if dir_path:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, dir_path)

def generate_txt_files():
    dir_path = directory_entry.get()
    text_content = text_entry.get("1.0", tk.END)
    for filename in os.listdir(dir_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            file_path = os.path.join(dir_path, filename)
            with open(os.path.splitext(file_path)[0] + ".txt", "w") as f:
                f.write(text_content)

root = tk.Tk()
root.title("Lora专用Prompt生成器")
root.geometry("300x280")
root.resizable(False, False)

watermark_label = tk.Label(root, text="Made by 包小猩，免费软件，禁止商用",fg="#808080")
watermark_label.pack(side="top", fill="x", pady=5)

directory_label = tk.Label(root, text="选择图片目录:", font=("Arial", 9))
directory_label.pack(side="top", padx=3, pady=3, anchor="w")

directory_frame = tk.Frame(root)
directory_frame.pack(side="top", padx=5, pady=5, fill="x")

directory_entry = tk.Entry(directory_frame, width=25, font=("Arial", 12))
directory_entry.pack(side="left", padx=3, pady=3, fill="x", expand=True)

browse_button = tk.Button(directory_frame,width=10, text="...", font=("Arial", 9), command=browse_dir)
browse_button.pack(side="right", padx=3, pady=3)

text_label = tk.Label(root, text="输入Prompt内容(关键词逗号隔开):", font=("Arial", 9))
text_label.pack(side="top", padx=5, pady=5, anchor="w")
text_entry = tk.Text(root, width=30, height=4, font=("Arial", 12))
text_entry.pack(side="top", padx=5, pady=5)

generate_button = tk.Button(root, text="生成",width=30, font=("Arial", 12), command=generate_txt_files, bg="#c3c3c3")
generate_button.pack(side="top", padx=5, pady=10)

root.mainloop()