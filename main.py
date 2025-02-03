import tkinter as tk
from tkinter import messagebox
import SarpTechCrypto as stc

window = tk.Tk()
window.title("CryptoNotes")
window.wm_minsize(width=500, height=700)

image = tk.PhotoImage(file="eth.png")
img_lbl = tk.Label(window, image=image)
img_lbl.pack(pady=20)

title_lbl = tk.Label(window, text="CryptoNotes", font=("Arial", 24))

note_title_lbl = tk.Label(window, text="Title")
note_title_lbl.pack()

note_title_entry = tk.Entry(window, width=30)
note_title_entry.pack()

note_content_lbl = tk.Label(window, text="Content")
note_content_lbl.pack()

note_content_entry = tk.Text(window)
note_content_entry.pack()

note_key_password_lbl = tk.Label(window, text="Master Key")
note_key_password_lbl.pack()

note_key_password_entry = tk.Entry(window, width=30)
note_key_password_entry.pack()

## ENCRYPTING

def crypt_note():
    message = note_content_entry.get("1.0", tk.END)
    master_key = note_key_password_entry.get()
    encrypted_message = stc.encrypt(message, master_key)

    with open("mysecret.txt", "a") as file:
        file.write(f"{note_title_entry.get()}\n")
        file.write(encrypted_message.strip())
        tk.messagebox.showinfo("Success", "Note saved successfully!")

def save_note():
    # Base64 formatına çevir

    if note_content_entry.get("1.0", tk.END) == "" or note_key_password_entry.get() == "" or note_title_entry.get() == "" :
        tk.messagebox.showerror("Error", "Please fill all fields!")
    else:
        crypt_note()

encrypt_btn = tk.Button(window, text="Save & Encrypt", command=save_note, font=("Arial", 12))
encrypt_btn.pack()

## DECRYPTING

def get_note():
    if note_content_entry.get("1.0", tk.END) == "" or note_key_password_entry.get() == "" :
        tk.messagebox.showerror("Error", "Please fill all fields!")
    else:
        decrypt_note()

def decrypt_note():
    message = note_content_entry.get("1.0", tk.END)
    master_key = note_key_password_entry.get()

    c = False
    with open("mysecret.txt", "r") as file:
        c = message.strip() in file.read().strip()

    if c == True:
        decrypted_msg = stc.decrypt(message, master_key)
        note_content_entry.delete("1.0", tk.END)
        note_content_entry.insert("1.0", decrypted_msg)
    else:
        tk.messagebox.showerror("Error", "There is no message with that content!")

decrypt_btn = tk.Button(window, text="Decrypt",command=get_note, font=("Arial", 12))
decrypt_btn.pack()
window.mainloop()