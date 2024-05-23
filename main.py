
# main_app.py
import tkinter as tk
from tkinter import messagebox
from add_student_window import AddStudentWindow
from view_student import ViewStudentWindow
from allocate_room import AllotRoomWindow
from view_room import ViewRoomWindow
from deallot_room_window import DeallotRoomWindow
from add_room_window import AddRoomWindow
class MainApp:
    def __init__( self, root):
        self.root = root
        self.root.title("Hostel Management System")
        self.root.geometry("500x500")
        self.root.configure(bg="#f0f0f0")
        self.students = []
        title_label = tk.Label(self.root, text="Hostel Management System", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333333")
        title_label.pack(pady=20)

        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        button_options = [
            ("Add Student", self.add_student),
            ("View Students", self.view_students),
            ("Add Room", self.add_room),
            ("View Rooms", self.view_rooms),
            ("Allocate Room", self.allocate_room),
            ("Deallocate Room", self.deallocate_room),
            ("Exit", self.exit_app)
        ]

        for (text, command) in button_options:
            button = tk.Button(button_frame, text=text, command=command, font=("Helvetica", 12), bg="#4caf50", fg="white", activebackground="#45a049", activeforeground="white", width=20, height=2)
            button.pack(pady=5)

    def add_student(self):
        AddStudentWindow(self.root)

    def view_students(self):
        ViewStudentWindow(self.root)
        
    def add_room(self):
        AddRoomWindow(self.root)

    def view_rooms(self):
        ViewRoomWindow(self.root)

    def allocate_room(self):
       AllotRoomWindow(self.root)
    def deallocate_room(self):
        DeallotRoomWindow(self.root)

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
