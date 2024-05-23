import tkinter as tk
from tkinter import messagebox
from database import deallot_room

class DeallotRoomWindow:
    def __init__(self, root):
        self.deallot_room_window = tk.Toplevel(root)
        self.deallot_room_window.title("Deallot Room")
        self.deallot_room_window.geometry("300x300")
        self.deallot_room_window.configure(bg="#f0f0f0")

        tk.Label(self.deallot_room_window, text="Phone No", bg="#f0f0f0").pack(pady=5)
        self.phone = tk.Entry(self.deallot_room_window)
        self.phone.pack(pady=5)

        save_button = tk.Button(self.deallot_room_window, text="Save", command=self.deallot_room, bg="#4caf50", fg="white", width=10)
        save_button.pack(pady=20)

    def deallot_room(self):
        phone = self.phone.get()

        if phone:
            res = deallot_room(phone)
            if res=='nostudent':
                messagebox.showwarning("Error", "No student found")
            elif res:
                messagebox.showinfo("Success", "Student Dealloted successfully")
            else:
                messagebox.showinfo("Failure", "Failed to deallot student")
            self.deallot_room_window.destroy()
        else:
            messagebox.showwarning("Input Error", "Phone number is required")