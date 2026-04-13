import tkinter as tk
from tkinter import messagebox

def check_palindrome():
    text = entry.get()
    
    # remove soace and converts to lowercase
    clean_text = text.replace(" ", "").lower()
    
    if clean_text == clean_text[::-1]:
        messagebox.showinfo("Result", f"'{text}' is a palindrome ✅")   # For emoji and more  i pressed window +(.)
    else:
        messagebox.showinfo("Result", f"'{text}' is not a palindrome ❌")
        
#GUI window
root=tk.Tk()
root.title("Palindrome Checker")
root.geometry("350x200")

#label 
tk.Label(root,text="Enter a string",font=("Arial",14)).pack(pady=10)

#Entry 
entry=tk.Entry(root,width=30)
entry.pack(pady=5)

#Button 
tk.Button(root,text="Check",command =check_palindrome).pack(pady=10)

root.mainloop()