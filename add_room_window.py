import tkinter as tk
from tkinter import messagebox
from database import add_room

class AddRoomWindow:
    def __init__(self, root):
        self.add_room_window = tk.Toplevel(root)
        self.add_room_window.title("Add Room")
        self.add_room_window.geometry("300x300")
        self.add_room_window.configure(bg="#f0f0f0")

        tk.Label(self.add_room_window, text="Room No", bg="#f0f0f0").pack(pady=5)
        self.room_no = tk.Entry(self.add_room_window)
        self.room_no.pack(pady=5)
        tk.Label(self.add_room_window, text="No of Students", bg="#f0f0f0").pack(pady=5)
        self.no_of_students = tk.Entry(self.add_room_window)
        self.no_of_students.pack(pady=5)
        self.ac = tk.IntVar()
        ac = tk.Radiobutton(self.add_room_window, text="AC", variable=self.ac, value=1, bg="#f0f0f0")
        ac.pack(pady=5)
        non_ac = tk.Radiobutton(self.add_room_window, text="Non AC", variable=self.ac, value=0, bg="#f0f0f0")
        non_ac.pack(pady=5)

        save_button = tk.Button(self.add_room_window, text="Save", command=self.save_room, bg="#4caf50", fg="white", width=10)
        save_button.pack(pady=20)
    
    def save_room(self):
        room_no = self.room_no.get()
        no_of_students = self.no_of_students.get()
        ac = self.ac.get()  # Get the value of the IntVar

        # Convert the value of ac to boolean (0 -> False, 1 -> True)
        ac_bool = bool(ac)

        if room_no and no_of_students:
            res = add_room(room_no, no_of_students, ac_bool)  # Pass the boolean value
            if res:
                messagebox.showinfo("Success", "Room added successfully")
                self.add_room_window.destroy()
            else:
                messagebox.showinfo("Failure", "Failed to add room")
        else:
            messagebox.showwarning("Input Error", "All fields are required")
