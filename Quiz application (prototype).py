import random
import mysql.connector as my 
from datetime import datetime


con = my.connect(host="localhost", user="root", passwd="")  
cur = con.cursor()


cur.execute("CREATE DATABASE IF NOT EXISTS quiz")
cur.execute("USE quiz")  

sql_create = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    contact VARCHAR(15),
    name VARCHAR(100) NOT NULL,
    year VARCHAR(10),
    enroll VARCHAR(20) UNIQUE,
    username VARCHAR(50) UNIQUE NOT NULL,
    branch VARCHAR(50),
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
cur.execute(sql_create)
con.commit()

stud={}
is_login =False
score_history = []
is_register=False
current_user = None
def load_users():
    global stud
    cur.execute("SELECT username, password, email, contact, name, year, enroll, branch FROM students")
    for row in cur.fetchall():
        username = row[0]
        stud[username] = {
            "username": username, "password": row[1], "email": row[2],
            "contact": row[3], "name": row[4], "year": row[5],
            "enroll": row[6], "branch": row[7]
        }


load_users()
def score_record(enroll, category, marks, total_marks):
    now = datetime.now()
    dt_str = now.strftime('%Y-%m-%d %H:%M:%S')
    score_history.append({
        'enroll': enroll,
        'category': category,
        'marks': marks,
        'total_marks': total_marks,
        'datetime': dt_str
    })
    sql_create1 = """
    CREATE TABLE IF NOT EXISTS score_records (
        id INT AUTO_INCREMENT PRIMARY KEY,
        enroll VARCHAR(20) ,
        category VARCHAR(50) NOT NULL,
        marks VARCHAR(50),
        total_marks VARCHAR(255) NOT NULL,
        datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    sql17= """
INSERT INTO score_records (
     enroll,category,marks,total_marks,datetime
) VALUES (%s, %s, %s, %s, %s )
"""
    val7=(enroll,category,marks,total_marks,dt_str)
    cur.execute(sql_create1)
    cur.execute(sql17,val7)
    con.commit()
def load_scores():
    global score_history
    score_history = []  
    cur.execute("""
        SELECT enroll, category, marks, total_marks, datetime 
        FROM score_records 
        ORDER BY datetime DESC
    """)
    for row in cur.fetchall():
        score_history.append({
            'enroll': row[0],
            'category': row[1],
            'marks': row[2],
            'total_marks': row[3],
            'datetime': str(row[4])  
        })
def show_scores():
    print("\n--- Quiz Score Records ---")
    print("Enrollment\tCategory\tScore\tDate & Time")
    for rec in score_history:
        print(f"{rec['enroll']}\t{rec['category']}\t{rec['marks']}/{rec['total_marks']}\t{rec['datetime']}")
    print("         ")
que1=[
        {
            "question": "What is a data structure?",
            "options": [
                "Programming language",
                "Database Design",
                "Storage and Data Organization Technique",
                "Collection of algorithms"
            ],
            "answer": "C"
        },
        {
            "question": "The insertion operation in the stack is known as:",
            "options": ["Add", "Push", "Insert", "Interpolate"],
            "answer": "B"
        },
        {
            "question": "A queue follows which principle?",
            "options": ["LIFO", "FIFO", "Linear tree", "Ordered array"],
            "answer": "B"
        },
        {
            "question": "Which data structure do we use for testing a palindrome?",
            "options": ["Heap", "Tree", "Priority queue", "Stack"],
            "answer": "D"
        },
        {
            "question": "What is the time complexity for accessing an element in an array?",
            "options": ["O(n)", "O(log n)", "O(1)", "O(n log n)"],
            "answer": "C"
        }
    ]
que3 = [
    {
        "question": "What does DBMS stand for?",
        "options": [
            "Database Management Software",
            "Database Maintenance System",
            "Database Management System",
            "Database Manipulation Software"
        ],
        "answer": "C"
    },
    {
        "question": "Which of the following is an example of a DBMS?",
        "options": [
            "MySQL",
            "MongoDB",
            "Oracle",
            "All of the above"
        ],
        "answer": "D"
    },
    {
        "question": "What is the primary key in a database?",
        "options": [
            "A unique identifier for a table row",
            "A key that encrypts data",
            "A key that allows duplicate values",
            "A foreign key reference"
        ],
        "answer": "A"
    },
    {
        "question": "Which SQL statement is used to insert a new record?",
        "options": [
            "SELECT",
            "UPDATE",
            "INSERT INTO",
            "DELETE"
        ],
        "answer": "C"
    },
    {
        "question": "Which of the following is NOT a characteristic of a DBMS?",
        "options": [
            "Data redundancy",
            "Data integrity",
            "Data security",
            "Data independence"
        ],
        "answer": "A"
    }
]

que2 = [
    {
        "question": "What is the output of the following code? print(type(10))",
        "options": [
            "<class 'int'>",
            "<class 'str'>",
            "<class 'float'>",
            "<class 'list'>"
        ],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": [
            "func",
            "define",
            "def",
            "function"
        ],
        "answer": "C"
    },
    {
        "question": "How do you insert comments in Python code?",
        "options": [
            "// comment",
            "<!-- comment -->",
            "# comment",
            "/* comment */"
        ],
        "answer": "C"
    },
    {
        "question": "Which collection type is ordered, changeable, and allows duplicates?",
        "options": [
            "Set",
            "Tuple",
            "List",
            "Dictionary"
        ],
        "answer": "C"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [
            ".pyth",
            ".pt",
            ".py",
            ".pyt"
        ],
        "answer": "C"
    }
]
    
def register():
    global is_register, is_login
    email=input("Enter email:")
    contact=input("Enter contact:")
    name=input("Enter name:")
    year=input("Enter year:")
    enroll=input("Enter enroll:")
    username=input("Enter username:")
    branch=input("Enter branch:")
    password=input("Enter password:")
    
  

    sql13= """
INSERT INTO students (
    email, contact, name, year, enroll, username, branch, password
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
    val=( email, contact, name, year, enroll, username, branch, password)
    
    cur.execute(sql13,val)
    con.commit()

    

    
    
    if username in stud:
        print(" Username already exists. Please try another.\n")
    else:
        stud[username] = {
            "email": email,
            "contact": contact,
            "name": name,
            "year": year,
            "branch": branch,
            "enroll": enroll,
            "username": username,
            "password": password
        }
        load_users()
        is_register = True
        print(" Registration successful!\n")
        print(" ")
        print(" ")
def login():
    global is_register, is_login,current_user
    username=input("Enter username:")
    password=input("Enter password:")
    if username in stud and stud[username]["password"] ==password:
        print(f"Login successful .....  {username}")
        is_login =True
        current_user =username
        print(" ")
        print(" ")
    else:
        print(" Invalid username or password ")

def dsa(): 
     global que1
     score=0
     random.shuffle(que1) 
     for  i ,que in enumerate(que1,1):
       print(f"{i} {que['question']}")
       for ix,op in zip(['A)','B)','C)','D)'],que['options']):
               print(f"{ix} {op}")
       answerr=input(" A) , B) , C) , D):").strip().upper()
       if answerr not in('A','B','C','D'):
              print("invalid option")
              print(" ")
              print(" ")
       if answerr ==que['answer'] :
                 print("correct")
                 score+=1
                 print(" ")
                 print(" ")
       else:
                     print(f"Wrong! Correct answer is {que['answer']}")
     enroll = stud[current_user]['enroll'] if current_user and current_user in stud else "N/A"
     score_record(enroll, 'DSA', score, len(que1))
     print(" ")
     print(" ")

def dbms():
   global que3
   score=0
   random.shuffle(que3) 
   for i ,que in enumerate(que3,1):
       print(f"{i} {que['question']}")
       for ix,op in zip(['A)','B)','C)','D)'],que['options']) :
               print(f"{ix}. {op}")
       answerr=input(" A) , B) , C) , D):").strip().upper()
       if answerr not in('A','B','C','D'):
           print("invalid option")
           print(" ")
           print(" ")
       if answerr ==que['answer'] :
               print("correct")
               score+=1
               print(" ")
               print(" ")
       else:
               print(f"Wrong! Correct answer is {que['answer']}")
   enroll = stud[current_user]['enroll'] if current_user and current_user in stud else "N/A"
   score_record(enroll, 'DBMS', score, len(que3))
def python():
    global que2
    score=0
    random.shuffle(que2) 
    for i ,que in enumerate(que2,1):
        print(f"{i} {que['question']}")
        for ix,op in zip(['A)','B)','C)','D)'],que['options']) :
            print(f"{ix}. {op}")
        answerr=input(" A) , B) , C) , D):").strip().upper()
        if answerr not in('A','B','C','D'):
            print("invalid option")
            print(" ")
            print(" ")
        if answerr ==que['answer'] :
            print("correct")
            score+=1
            print(" ")
            print(" ")
        else:
            print(f"Wrong! Correct answer is {que['answer']}")
    enroll = stud[current_user]['enroll'] if current_user and current_user in stud else "N/A"
    score_record(enroll, 'PYTHON', score, len(que2))
    print(" ")
    print(" ")
    
def profile():
    
    if current_user in stud:
        user = stud[current_user]
        print(f"Name: {user.get('name', '')}")
        print(f"Contact: {user.get('contact', '')}")
        print(f"Email: {user.get('email', '')}")
        print(f"Year: {user.get('year', '')}")
        print(f"Branch: {user.get('branch', '')}")
        print(f"Enroll: {user.get('enroll', '')}")
        print(f"Username: {user.get('username', '')}")
    else:
       print("No profile found. Please login.")
def update_profile():
    global stud, is_login, current_user

    if not is_login or current_user is None:
        print("You need to login first!")
        return

    
    valid_fields = ['name', 'contact', 'email', 'year', 'branch', 'password', 'username']

    print("Fields you can update: " + ", ".join(valid_fields))
    field = input("Enter field to update: ").lower()

    if field not in valid_fields:
        print("Invalid field!")
        return

    new_value = input(f"Enter new value for {field}: ")

    
    if field == 'username':
        if new_value in stud:
            print("Username already exists, please try another.")
            return
        
        stud[new_value] = stud.pop(current_user)
        stud[new_value]['username'] = new_value
        sql = "UPDATE students SET username = %s WHERE username = %s"
        cur.execute(sql, (new_value, current_user))
        con.commit()
        current_user = new_value
        print("Username updated successfully!")
        load_users()
        return

    
    stud[current_user][field] = new_value

    
    sql = f"UPDATE students SET {field} = %s WHERE username = %s"
    cur.execute(sql, (new_value, current_user))
    con.commit()

    print(f"{field.capitalize()} updated successfully!")
def logout(): 
    global is_register, is_login,current_user
    if is_login==True :
        print(f"User {stud[current_user]['name']} logged out successfully.") 
        is_login=False
        current_user = None
    else:
        print("No user is currently logged in.\n")
def main():
    while True:
        print("===== Quiz System =====")
        print("1. Register")
        print("2. Login") 
        print("3. Quiz")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            if not is_login:
                print("Please login first!")
                continue
                
            print("1. Login")
            print("2. Attempt quiz")
            print("3. View scores")
            print("4. Logout")
            print("5. Update profile")
            print("6. Profile")
            
            try:
                o = int(input("Enter choice (1-6): "))
                if o == 1:
                    login()
                elif o == 2:
                    print("1) DSA  2) DBMS  3) PYTHON")
                    k = int(input("Enter category: "))
                    if k == 1:
                        dsa()
                    elif k == 2:
                        dbms()
                    elif k == 3:
                        python()
                    else:
                        print("Wrong choice")
                elif o == 3:
                    load_scores()  
                    show_scores()
                elif o == 4:
                    logout()
                elif o == 5:
                    update_profile()
                elif o == 6:
                    profile()
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Enter a valid number!")
                
        elif choice == "4":
            print("Exiting system. Goodbye!")
            con.close()  
            break
        else:
            print("Invalid choice! Try again.\n")
main()
