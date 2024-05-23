import mysql.connector

# Establish database connection
conn = mysql.connector.connect(host="localhost", user="root", password="root", database="hostel_management")
cursor = conn.cursor()

def add_student(name, admission_no, course, phone, room_no=0):
    try:
        insert_query = "INSERT INTO students (name, room_no, admission_no, course, phone) VALUES (%s, %s, %s, %s, %s)"
        student_data = (name, room_no, admission_no, course, phone)
        cursor.execute(insert_query, student_data)
 
        conn.commit()
        return True
    except mysql.connector.Error as e:
        print("Error: ", e)  
        return False

def add_room(room_no, no_of_students, ac):
    try:
        insert_query = "INSERT INTO room (room_no, no_of_students, ac) VALUES (%s, %s, %s)"
        room_data = (room_no, no_of_students, ac)
        cursor.execute(insert_query, room_data)

        conn.commit()
        return True
    except mysql.connector.Error as e:
        print("Error: ", e)
        return False
    
def view_students(name=None, phone=None, room_no=None):
    try:
        print('name:', name, 'phone:', phone, 'room_no:', room_no)
        if name:
            set_query = f"SELECT * FROM students WHERE name = '{name}'"
        elif phone:
            set_query = f"SELECT * FROM students WHERE phone = '{phone}'"
        else:
            set_query = "SELECT * FROM students"
        print('set_query:', set_query)
        cursor.execute(set_query)
        students = cursor.fetchall()
        return students
    
    except mysql.connector.Error as e:
        print("Error: ", e)
        return False

def allot_room(phone_no, room_no):
    try:
        ifroom = view_rooms(room_no)
        if ifroom == 'noroom':
            return 'noroom'

        student = view_students(room_no=room_no)
        
        # Convert ifroom[1] to an integer before comparison
        max_capacity = int(ifroom[1])

        if len(student) >= max_capacity:
            return 'full'
        
        update_query = f"UPDATE students SET room_no = {room_no} WHERE phone = '{phone_no}'"
        cursor.execute(update_query)
        conn.commit()

        if cursor.rowcount == 0:
            return 'noroom'
        else: 
            return True
    
    except mysql.connector.Error as e:
        print("Error: ", e)
        return False

def view_rooms(room_no=None):
    try:
        data = []
        if room_no:
            set_query = f"SELECT * FROM room WHERE room_no = {room_no}"
            cursor.execute(set_query)
            room = cursor.fetchone()  # Use fetchone() as only one room is expected
            if not room:
                return 'noroom' 
            students_query = f"SELECT name, admission_no, course, phone FROM students WHERE room_no = {room_no}"
            cursor.execute(students_query)
            students = cursor.fetchall()
            data = [room[0], room[1], room[2], students]
        else:
            set_query = "SELECT * FROM room"
            cursor.execute(set_query)
            rooms = cursor.fetchall()
            data = rooms
        return data
    except mysql.connector.Error as e:
        print("Error: ", e)
        return False

    
def deallot_room(phone_no):
    try:
        ifroom = view_students(phone=phone_no)
        if len(ifroom) == 0:
            return 'nostudent'
        update_query = f"UPDATE students SET room_no = 0 WHERE phone = '{phone_no}'"
        cursor.execute(update_query)
        conn.commit()

        if cursor.rowcount == 0:
            return False
        else: 
            return True
    
    except mysql.connector.Error as e:
        print("Error: ", e)
        return False

