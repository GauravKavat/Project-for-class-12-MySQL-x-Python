import pymysql as msc

server_connection = msc.connect(
    host="localhost", user="root", passwd="ca11fr0mbr0therh00d"
)

cursor = server_connection.cursor()

cursor.execute("CREATE DATABASE MAIN;")

cursor.execute(
    "CREATE TABLE MANAGER(ID VARCHAR(240), Name CHAR(240), email VARCHAR(240), psd varcahr(240), contact_info varchar(240), bck_up_wrd char(5));"
)

server_connection.commit()

cursor.close()
