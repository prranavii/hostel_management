import tkinter as tk
from tkinter import messagebox
from database import view_rooms

class ViewRoomWindow:
    def __init__(self, root):
        self.view_room_window = tk.Toplevel(root)
        self.view_room_window.title("View Room Details")
        self.view_room_window.geometry("300x300")
        self.view_room_window.configure(bg="#f0f0f0")

        tk.Label(self.view_room_window, text="Room No", bg="#f0f0f0").pack(pady=5)
        self.room_no = tk.Entry(self.view_room_window)
        self.room_no.pack(pady=5)

        show_button = tk.Button(self.view_room_window, text="Show", command=self.show_room, bg="#4caf50", fg="white", width=10)
        show_button.pack(pady=20)

    def show_room(self):
        room_no = self.room_no.get()

        if room_no:
            room_details = view_rooms(room_no)
            if room_details == 'noroom':
                messagebox.showwarning("Error", "No room found")
            elif room_details:
                self.display_room_details(room_details)
            else:
                messagebox.showinfo("No Record", "No room found with the given details")
        else:
            messagebox.showwarning("Input Error", "Room number is required")

    def display_room_details(self, room_details):
        details_window = tk.Toplevel(self.view_room_window)
        details_window.title("Room Details")
        details_window.geometry("400x300")
        details_window.configure(bg="#f0f0f0")

        tk.Label(details_window, text="Room Details", bg="#f0f0f0", font=('Arial', 14)).pack(pady=10)

        # Display room details
        tk.Label(details_window, text=f"Room No: {room_details[0]}", bg="#f0f0f0").pack(pady=5)
        tk.Label(details_window, text=f"No of Students: {room_details[1]}", bg="#f0f0f0").pack(pady=5)
        tk.Label(details_window, text=f"AC: {'Yes' if room_details[2] else 'No'}", bg="#f0f0f0").pack(pady=5)

        # Display student details
        if len(room_details) > 3:
            tk.Label(details_window, text="Students in Room:", bg="#f0f0f0", font=('Arial', 12)).pack(pady=5)
            for student in room_details[3]:
                tk.Label(details_window, text=f"Name: {student[0]}, Admission No: {student[1]}, Course: {student[2]}, Phone: {student[3]}", bg="#f0f0f0").pack(pady=2)


        
