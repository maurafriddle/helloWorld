from app import app, db
from models import Student, Major, User
from werkzeug.security import generate_password_hash
import datetime as dt


with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management', \
              'Operations Management & Business Analytics', 'Supply Chain Management']
    for each_major in majors:
        print(each_major)
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Initial loading of students first_name, last_name, major_id, email, birth_date, is_honors
    students = [
        {'student_id': '1', 'first_name': 'Robert', 'last_name':'Smith', 'major_id':3, 'email': "rsmith@umd.edu",
            'birth_date': dt.datetime(2007, 6, 1), 'is_honors':1},
        {'student_id': '2', 'first_name': 'Leo', 'last_name': 'Van Munching', 'major_id':6, 'email': "lvmunch@umd.edu",
         'birth_date': dt.datetime(2008, 3, 24), 'is_honors': 0},
    ]

    for each_student in students:
        print(f'{each_student["first_name"]} {each_student["last_name"]} inserted into Student')
        a_student = Student(first_name=each_student["first_name"], last_name=each_student["last_name"],
                            major_id=each_student["major_id"], email=each_student["email"], birth_date=each_student["birth_date"],
                            is_honors=each_student["is_honors"])
        db.session.add(a_student)
        db.session.commit()


    # Initial loading of users
    users = [
        {'username': 'student', 'email': 'student@umd.edu', 'first_name':'Imma', 'last_name':'Student',
            'password': generate_password_hash('studentpw', method='pbkdf2:sha256'), 'role':'STUDENT'},
        {'username': 'manager', 'email': 'manager@umd.edu', 'first_name':'Joe', 'last_name':'King',
            'password': generate_password_hash('managerpw', method='pbkdf2:sha256'), 'role':'MANAGER'},
        {'username': 'admin', 'email': 'admin@umd.edu', 'first_name':'Crystal', 'last_name':'Ball',
            'password': generate_password_hash('adminpw', method='pbkdf2:sha256'), 'role':'ADMIN'},
        {'username': 'mfriddl1', 'email': 'mfriddl1@terpmail.umd.edu', 'first_name': 'Maura', 'last_name': 'Friddle',
            'password': generate_password_hash('mfriddl1', method='pbkdf2:sha256'), 'role':'STUDENT'}
    ]

    for each_user in users:
        print(f'{each_user["username"]} inserted into user')
        a_user = User(username=each_user["username"], email=each_user["email"], first_name=each_user["first_name"],
                      last_name=each_user["last_name"], password=each_user["password"], role=each_user["role"])
        db.session.add(a_user)
        db.session.commit()
