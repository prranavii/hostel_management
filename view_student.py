import tkinter as tk
from tkinter import messagebox
from database import  view_students  # Assuming get_student_details is defined

class ViewStudentWindow:
    def __init__(self, root):
        self.add_student_window = tk.Toplevel(root)
        self.add_student_window.title("View Student Details")
        self.add_student_window.geometry("300x300")
        self.add_student_window.configure(bg="#f0f0f0")

        tk.Label(self.add_student_window, text="Name", bg="#f0f0f0").pack(pady=5)
        self.name = tk.Entry(self.add_student_window)
        self.name.pack(pady=5)
        tk.Label(self.add_student_window, text="Phone No", bg="#f0f0f0").pack(pady=5)
        self.phone_no = tk.Entry(self.add_student_window)
        self.phone_no.pack(pady=5)

        show_button = tk.Button(self.add_student_window, text="Show", command=self.show_student, bg="#4caf50", fg="white", width=10)
        show_button.pack(pady=20)

    def show_student(self):
        name = self.name.get()
        phone = self.phone_no.get()

        if name or phone:
            student_details = view_students(name, phone)
            if student_details:
                self.display_student_details(student_details)
            else:
                messagebox.showinfo("No Record", "No student found with the given details")
        else:
            messagebox.showwarning("Input Error", "Any one field is required")

    def display_student_details(self, student_details):
        details_window = tk.Toplevel(self.add_student_window)
        details_window.title("Student Details")
        details_window.geometry("300x300")
        details_window.configure(bg="#f0f0f0")

        tk.Label(details_window, text="Student Details", bg="#f0f0f0", font=('Arial', 14)).pack(pady=10)

        for key, value in student_details.items():
            tk.Label(details_window, text=f"{key}: {value}", bg="#f0f0f0").pack(pady=5)
        
