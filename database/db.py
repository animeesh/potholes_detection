import sqlite3
import constants

session = {}




def login_validatlilon(eml, pwd):
    email = eml
    password = pwd
    try:
        conn = sqlite3.connect(constants.DB_USER_PATH)
        print(constants.CONNECTION_SUCCESFUL)
        cursor = conn.cursor()
    except:
        print(constants.CONNECTION_FAIL)
    try:
        cursor.execute("""SELECT * FROM user WHERE email = '{}' AND password = '{}'""".format(email, password))
        users = cursor.fetchall()

    except:
        print(constants.QUERY_ERROR)
    conn.commit()
    conn.close()

    print(session)

    if len(users) == 1:
        return users
    else:
        return 0


def uniq_email(eml):
    email_unq = eml
    try:
        conn = sqlite3.connect(constants.DB_USER_PATH)
        print(constants.CONNECTION_SUCCESFUL)
        cursor1 = conn.cursor()
    except:
        print(constants.CONNECTION_FAIL)
    try:
        cursor1.execute("""SELECT * FROM user WHERE email = '{}'""".format(email_unq))
        users = cursor1.fetchall()
        conn.commit()
        conn.close()
        if len(users) == 1:
            print('match found')
            return 1
        else:
            print('no match found')
            return 0
    except:
        print(constants.QUERY_ERROR)


def register_user(users_name, eml, pwd):
    email = eml
    password = pwd
    name = users_name
    try:
        # conn = constants.DB_USER_PATH
        conn = sqlite3.connect(constants.DB_USER_PATH)

        print(constants.CONNECTION_SUCCESFUL)
        cursor2 = conn.cursor()
    except:
        print(constants.CONNECTION_FAIL)
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor2.execute(
            """INSERT INTO user (name,email,password)VALUES( '{}','{}','{}')""".format(name, email, password))
        print("user added succesful")
        conn.commit()
        conn.close()

    except:
        print(constants.QUERY_ERROR)


def savei(email, filename, filepath, lat, lon, num_pot):
    my_email = email
    my_filename = filename
    my_filepath = filepath
    my_lat = lat
    my_lon = lon
    num_pothole = num_pot

    try:
        conn4 = sqlite3.connect(constants.DB_USER_PATH)
        # cursor = conn.cursor()
        print(constants.CONNECTION_SUCCESFUL)
        # cursor = conn.cursor()
    except:
        print("An exception occurred")
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor4 = conn4.cursor()
    except:
        print(constants.CONNECTION_FAIL)

    try:
        cursor4.execute(
            """INSERT INTO image(email,filename,filepath,lat,lon,count)VALUES('{}','{}','{}',{},{},{})""".format(
                my_email, my_filename, my_filepath, my_lat, my_lon, num_pothole))
        print("pohole data stored succesfull")
        conn4.commit()
        conn4.close()

    except:
        print(constants.QUERY_ERROR)


def admshow():
    try:
        conn5 = sqlite3.connect(constants.DB_USER_PATH)
        print(constants.CONNECTION_SUCCESFUL)
        cursor5 = conn5.cursor()
    except:
        print(constants.CONNECTION_FAIL)
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor5.execute("""SELECT email,lat,lon,count FROM image""")

    except:
        print(constants.QUERY_ERROR)
    users_image = cursor5.fetchall()
    total_complaint = len(users_image)
    conn5.commit()
    conn5.close()
    return users_image, total_complaint


def view_previous(email):
    email_id = email
    try:
        conn6 = sqlite3.connect(constants.DB_USER_PATH)
        print(constants.CONNECTION_SUCCESFUL)
        cursor6 = conn6.cursor()
    except:
        print(constants.CONNECTION_FAIL)
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor6.execute("""SELECT email,lat,lon,count FROM image WHERE email='{}'""".format(email_id))
        users_image = cursor6.fetchall()
    except:
        print(constants.QUERY_ERROR)
    conn6.commit()
    conn6.close()
    return users_image[::-1]


def view_recent(email):
    email_id = email
    try:
        conn9 = sqlite3.connect(constants.DB_USER_PATH)
        print(constants.CONNECTION_SUCCESFUL)
        cursor9 = conn9.cursor()
    except:
        print(constants.CONNECTION_FAIL)
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor9.execute("""SELECT email,lat,lon,count FROM image WHERE email='{}'""".format(email_id))
        users_image = cursor9.fetchall()
        users_recent = users_image[(len(users_image) - 1)]
    except:
        print(constants.QUERY_ERROR)
    conn9.commit()
    conn9.close()
    return users_recent


def user_info_basic(u_email):
    try:
        conn7 = sqlite3.connect(constants.DB_USER_PATH)
        print(constants.CONNECTION_SUCCESFUL)
        cursor7 = conn7.cursor()
    except:
        print(constants.CONNECTION_FAIL)
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor7.execute("""SELECT name FROM user WHERE email='{}'""".format(u_email))
        users_name = cursor7.fetchall()
    # print('sadsad')
    # print(users_name[0][0])
    except:
        print(constants.QUERY_ERROR)
    conn7.commit()
    conn7.close()
    return users_name[0][0]


def user_complaint_basic(u_email):
    try:
        conn8 = sqlite3.connect(constants.DB_USER_PATH)
        print(constants.CONNECTION_SUCCESFUL)
        cursor8 = conn8.cursor()
    except:
        print(constants.CONNECTION_FAIL)
        # conn = sqlite3.connect('C:\Users\yash\PycharmProjects\pothole\database\user_datbase.db')
    try:
        cursor8.execute("""SELECT filename FROM image WHERE email='{}'""".format(u_email))
        temp_ar = cursor8.fetchall()
        count = len(temp_ar)


    except:
        print(constants.QUERY_ERROR)
    conn8.commit()
    conn8.close()
    return count

