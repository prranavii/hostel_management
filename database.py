import mysql.connector

conn=mysql.connector.connect(host="localhost",user="root",password="root",database="hostel_management")

cursor=conn.cursor()


def add_student(name,admission_no, course,phone, room_no=0):
    try:
        insert_query= "INSERT INTO students (name,room_no,admission_no,course,phone) VALUES(%s,%s,%s,%s,%s)"
        student_data=(name,room_no,admission_no,course,phone)
        cursor.execute(insert_query,student_data)
 
        conn.commit()

        return True
    except mysql.connector.Error as e:
        print("Error ", e)  
        return False

def add_room(room_no,no_of_students,ac):
    try:
        insert_query= "INSERT INTO room (room_no,no_of_students,ac) VALUES (%s,%s,%s)"
        room_data=(room_no,no_of_students,ac)
        cursor.execute(insert_query,room_data)

        conn.commit()

        return True
    except mysql.connector.Error as e:
        print("error",e)
        return False
    
def view_students(name=None,phone=None,):
    try:
        set_query=""
        if name is not None:
            set_query = f"SELECT * FROM students WHERE name={name}"
        elif phone is not None:
            set_query = f"SELECT * FROM phones WHERE phone={phone}"
        else:
            set_query = "SELECT * FROM students"
        
        cursor.execute(set_query)

        students=cursor.fetchall()
        return students
    
    except mysql.connector.Error as e:
        print("error",e)
        return False

def allot_room(phone_no,room_no):
    try:
        update_query=f"update students set room_no={room_no} where phone= {phone_no}"
        
        cursor.execute(update_query)
        conn.commit()

        if cursor.rowcount() == 0:
            return 0
        else: 
            return True
    
    except mysql.connector.Error as e:
        print("error",e)
        return False

