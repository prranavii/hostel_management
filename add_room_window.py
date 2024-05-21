import tkinter as tk
from tkinter import messagebox
from database import add_room

class AddStudentWindow:
    def __init__(self, root):
        self.add_student_window = tk.Toplevel(root)
        self.add_student_window.title("Add Student")
        self.add_student_window.geometry("300x300")
        self.add_student_window.configure(bg="#f0f0f0")

        tk.Label(self.add_student_window, text="Room No", bg="#f0f0f0").pack(pady=5)
        self.room = tk.Entry(self.add_student_window)
        self.room.pack(pady=5)
        tk.Label(self.add_student_window, text="Occupancy", bg="#f0f0f0").pack(pady=5)
        self.occupancy = tk.Entry(self.add_student_window)
        self.occupancy.pack(pady=5)
        tk.Label(self.add_student_window, text="AC", bg="#f0f0f0").pack(pady=5)
        self.ac = tk.Entry(self.add_student_window)
        self.ac.pack(pady=5)

        save_button = tk.Button(self.add_student_window, text="Save", command=self.save_student, bg="#4caf50", fg="white", width=10)
        save_button.pack(pady=20)

    def save_student(self):
        room = self.room.get()
        ac = self.ac.get()
        occupancy = self.occupancy.get()
       

        if room and ac and occupancy:
            res = add_room(room,occupancy,ac)
            if res:
                messagebox.showinfo("Success", "Room added successfully")
            else:
                messagebox.showinfo("Failure", "Failed to add Room")
            self.add_student_window.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required")
