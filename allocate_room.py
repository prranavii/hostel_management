import tkinter as tk
from tkinter import messagebox
from database import allot_room

class AllotRoomWindow:
    def __init__(self, root):
        self.add_student_window = tk.Toplevel(root)
        self.add_student_window.title("Allot Student")
        self.add_student_window.geometry("300x300")
        self.add_student_window.configure(bg="#f0f0f0")

        tk.Label(self.add_student_window, text="Phone No", bg="#f0f0f0").pack(pady=5)
        self.phone = tk.Entry(self.add_student_window)
        self.phone.pack(pady=5)

        tk.Label(self.add_student_window, text="Room", bg="#f0f0f0").pack(pady=5)
        self.room = tk.Entry(self.add_student_window)
        self.room.pack(pady=5)

        save_button = tk.Button(self.add_student_window, text="Save", command=self.save_student, bg="#4caf50", fg="white", width=10)
        save_button.pack(pady=20)

    def save_student(self):
        room = self.room.get()
        phone = self.phone.get()

        if room and phone:
            res = allot_room(phone,room)
            if res==0:
                messagebox.showwarning("Error", "No student found")
            elif res=='noroom':
                messagebox.showwarning("Error", "No room found")
            elif res=='full':
                messagebox.showwarning("Error", "Room is full")
            elif res:
                messagebox.showinfo("Success", "Student Allotted successfully")
            else:
                messagebox.showinfo("Failure", "Failed to add student")
            self.add_student_window.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required")
