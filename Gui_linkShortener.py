import tkinter as tk
import pyshorteners
import pyperclip

def shorten_url():
    long_url = url_entry.get()
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url)
    result_label.config(text=f"Short URL: {short_url}")
    copy_button.config(state=tk.NORMAL)

def copy_to_clipboard():
    short_url = result_label.cget("text").split(": ")[1]
    pyperclip.copy(short_url)

# Create the main window
root = tk.Tk()
root.title("URL Shortener")

# Create and place the widgets
tk.Label(root, text="Enter the long URL:").pack(pady=10)

url_entry = tk.Entry(root, width=100, font=('Arial', 11), bg='lightyellow', bd=2, relief='solid')
url_entry.pack(pady=5)

shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
shorten_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=10)

# Run the application
root.mainloop()