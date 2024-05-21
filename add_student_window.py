import tkinter as tk
from tkinter import messagebox
from database import add_student

class AddStudentWindow:
    def __init__(self, root):
        self.add_student_window = tk.Toplevel(root)
        self.add_student_window.title("Add Student")
        self.add_student_window.geometry("300x300")
        self.add_student_window.configure(bg="#f0f0f0")

        tk.Label(self.add_student_window, text="Name", bg="#f0f0f0").pack(pady=5)
        self.name = tk.Entry(self.add_student_window)
        self.name.pack(pady=5)

        tk.Label(self.add_student_window, text="Admission No", bg="#f0f0f0").pack(pady=5)
        self.admission_no = tk.Entry(self.add_student_window)
        self.admission_no.pack(pady=5)

        tk.Label(self.add_student_window, text="Course", bg="#f0f0f0").pack(pady=5)
        self.course = tk.Entry(self.add_student_window)
        self.course.pack(pady=5)

        tk.Label(self.add_student_window, text="Phone No", bg="#f0f0f0").pack(pady=5)
        self.phone_no = tk.Entry(self.add_student_window)
        self.phone_no.pack(pady=5)

        save_button = tk.Button(self.add_student_window, text="Save", command=self.save_student, bg="#4caf50", fg="white", width=10)
        save_button.pack(pady=20)

    def save_student(self):
        name = self.name.get()
        admission_no = self.admission_no.get()
        course = self.course.get()
        phone = self.phone_no.get()

        if name and admission_no and phone and course:
            res = add_student(name, admission_no,course,phone)
            if res:
                messagebox.showinfo("Success", "Student added successfully")
            else:
                messagebox.showinfo("Failure", "Failed to add student")
            self.add_student_window.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required")
