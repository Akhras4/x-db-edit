import mysql.connector
d=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="0000",
    database="profile",
)
mycursor=d.cursor()
mycursor.execute("ALTER TABLE xuserinfo "  
                 " ADD  Personalizedads BOOLEAN DEFAULT 0 "
                 )
