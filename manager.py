import pymysql as msc

server_connection = msc.connect(
    host="localhost", user="root", passwd="ca11fr0mbr0therh00d", database="main"
)

cursor = server_connection.cursor()


print(
    """
+-------------------------------------------------+
|                L O G I N     A S                |
+-------------------------------------------------+
| 1. | Administrator                              |
+-------------------------------------------------+
| 2. | User                                       |
+-------------------------------------------------+
| 3. | EXIT                                       |
+-------------------------------------------------+
"""
)
ch = input("Enter your choice [ 1 - 2 - 3 ] :")

if ch == "1":
    password = input("Enter the administrator password :")

    if password == "ca11fr0mbr0therh00d":
        print(
            """
<=================================================>
| 1. | Display all information about users        |
+-------------------------------------------------+
| 2. | Remove a user                              |
+-------------------------------------------------+
| 3. | Destroy application                        |
+-------------------------------------------------+
| 4. | EXIT                                       |
<=================================================>
"""
        )
        admin = input("[ 1 - 2 - 3 - 4 ] -->")

        if admin == "1":
            cursor.execute("SELECT * FROM MANAGER ;")
            data = cursor.fetchall()

            for i in data:
                print("+-------------------------------------------------+")
                print("| ID            |", i[0])
                print("| Name          |", i[1])
                print("| Email         |", i[2])
                print("| Password      |", i[3])
                print("| Contact       |", i[4])
                print("| Recovery word |", i[5])
                print("+-------------------------------------------------+")
                exit = input("Press return to exit")

        elif admin == "2":
            id = input("Enter the ID of the person to remove :")
            print("<=================================================>")
            print("|     P E R S O N   T O   B E   R E M O V E D     |")
            print("<=================================================>")
            cursor.execute("SELECT * FROM MANAGER WHERE ID = '{}' ;".format(id))
            data = cursor.fetchall()

            for i in data:
                print("+-------------------------------------------------+")
                print("| ID            |", i[0])
                print("| Name          |", i[1])
                print("| Email         |", i[2])
                print("| Password      |", i[3])
                print("| Contact       |", i[4])
                print("| Recovery word |", i[5])
                print("+-------------------------------------------------+")
            cursor.execute("DELETE FROM MANAGER WHERE ID = '{}' ;".format(id))
            server_connection.commit()
            print("<=================================================>")
            print("|    P  E  R  S  O  N      R  E  M  O  V  E  D    |")
            print("<=================================================>")
            exit = input("Press return to exit")

        elif admin == "3":
            choice = input("Are you sure you want to destroy the appilcation [y/n] :")

            if choice == "Y" or choice == "y":
                pswd = input("Enter password to confirm your identity :")

                if pswd == "ca11fr0mbr0therh00d":
                    cursor.execute("DROP TABLE MANAGER;")
                    server_connection.commit()
                    exit = input("Press return to exit")

                else:
                    print("<=================================================>")
                    print("|      I N C O R R E C T     P A S S W O R D      |")
                    print("+-------------------------------------------------+")
                    print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
                    print("<=================================================>")
                    exit = input("Press return to exit")

        elif admin == "4":
            print("<=================================================>")
            print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
            print("<=================================================>")
            exit = input("Press return to exit")

        else:
            print("<=================================================>")
            print("|   I  N  V  A  L  I  D     C  O  M  M  A  N  D   |")
            print("+-------------------------------------------------+")
            print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
            print("<=================================================>")
            exit = input("Press return to exit")

    else:
        print("+-------------------------------------------------+")
        print("|      I N C O R R E C T     P A S S W O R D      |")
        print("+-------------------------------------------------+")
        print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
        print("+-------------------------------------------------+")
        exit = input("Press return to exit")

elif ch == "2":

    while True:
        print(
            """
+-------------------------------------------------+
| 1. | Add user                                   |
+-------------------------------------------------+
| 2. | Update user                                |
+-------------------------------------------------+
| 3. | Find information                           |
+-------------------------------------------------+
| 4. | Display all users                          |
+-------------------------------------------------+
| 5. | EXIT                                       |
+-------------------------------------------------+
"""
        )

        ch = input("[ 1 - 2 - 3 - 4 - 5 ] --> ")

        if ch == "1":
            id = input("Enter a unique username :")
            name = input("Enter your name :")
            email = input("Enter your email :")
            psd = input("Enter your password :")
            contact_info = input("Enter your contact information :")
            bck_up_word = input(
                "Enter a 4 letter word [ This will be used for recovery later ] :"
            )

            cursor.execute(
                "INSERT INTO MANAGER VALUES( '{}' , '{}' , '{}' , '{}' , '{}' , '{}' ) ; ".format(
                    id, name, email, psd, contact_info, bck_up_word
                )
            )

            server_connection.commit()
            exit = input("Press return to exit")

        elif ch == "2":
            print(
                """
+-------------------------------------------------+
|  E N T E R  T H E  F I E L D  T O  U P D A T E  |
+-------------------------------------------------+
| 1. | Name                                       |
+-------------------------------------------------+
| 2. | Password                                   |
+-------------------------------------------------+
| 3. | EXIT                                       |
+-------------------------------------------------+
"""
            )
            updt = input("[ 1 - 2 - 3 ] --> ")
            if updt == "1":
                print(
                    """
+-------------------------------------------------+
| ENTER  THE  FIELD  YOU  REMEMBER  FROM  ACCOUNT |
+-------------------------------------------------+
| 1. | ID                                         |
+-------------------------------------------------+
| 2. | Email                                      |
+-------------------------------------------------+
| 3. | EXIT                                       |
+-------------------------------------------------+
"""
                )
                rmbr = input("[ 1 - 2 - 3 ] -->")

                if rmbr == "1":
                    id = input("Enter the ID of the person to update :")
                    name = input("Enter the new name :")
                    cursor.execute(
                        "UPDATE MANAGER SET NAME = '{}' WHERE ID = '{}' ;".format(
                            name, id
                        )
                    )
                    server_connection.commit()
                    exit = input("Press return to exit")

                elif rmbr == "2":
                    email = input("Enter the email of the person to update")
                    name = input("Enter the new name :")
                    cursor.execute(
                        "UPDATE MANAGER SET NAME = '{}' WHERE EMAIL = '{}' ;".format(
                            name, email
                        )
                    )
                    server_connection.commit()
                    exit = input("Press return to exit")

                elif updt == "3":
                    print("+-------------------------------------------------+")
                    print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
                    print("+-------------------------------------------------+")
                    exit = input("Press return to exit")
                    break

                else:
                    print("+-------------------------------------------------+")
                    print("|   I  N  V  A  L  I  D     C  O  M  M  A  N  D   |")
                    print("+-------------------------------------------------+")
                    exit = input("Press return to exit")
                    break

            elif updt == "2":
                print(
                    """
+-------------------------------------------------+
| ENTER  THE  FIELD  YOU  REMEMBER  FROM  ACCOUNT |
+-------------------------------------------------+
| 1. | ID                                         |
+-------------------------------------------------+
| 2. | Email                                      |
+-------------------------------------------------+
| 3. | EXIT                                       |
+-------------------------------------------------+
"""
                )
                rmbr = input("[ 1 - 2 - 3 ] -->")
                if rmbr == "1":
                    id = input("Enter the ID of the person to update :")
                    pswd = input("Enter the new password :")
                    cursor.execute(
                        "UPDATE MANAGER SET PASSWORD = '{}' WHERE ID = '{}' ;".format(
                            pswd, id
                        )
                    )
                    server_connection.commit()
                    exit = input("Press return to exit")

                elif rmbr == "2":
                    email = input("Enter the email of the person to update")
                    pswd = input("Enter the new name :")
                    cursor.execute(
                        "UPDATE MANAGER SET PASSWORD = '{}' WHERE EMAIL = '{}' ;".format(
                            pswd, email
                        )
                    )
                    server_connection.commit()
                    exit = input("Press return to exit")

                elif updt == "3":
                    print("+-------------------------------------------------+")
                    print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
                    print("+-------------------------------------------------+")
                    exit = input("Press return to exit")
                    break

                else:
                    print("+-------------------------------------------------+")
                    print("|   I  N  V  A  L  I  D     C  O  M  M  A  N  D   |")
                    print("+-------------------------------------------------+")
                    exit = input("Press return to exit")
                    break

            elif updt == "3":
                print("+-------------------------------------------------+")
                print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
                print("+-------------------------------------------------+")
                exit = input("Press return to exit")
                break

            else:
                print("+-------------------------------------------------+")
                print("|   I  N  V  A  L  I  D     C  O  M  M  A  N  D   |")
                print("+-------------------------------------------------+")
                exit = input("Press return to exit")
                break

        elif ch == "3":
            print(
                """
+-------------------------------------------------+
| ENTER  THE  FIELD  YOU  REMEMBER  FROM  ACCOUNT |
+-------------------------------------------------+
| 1. | ID                                         |
+-------------------------------------------------+
| 2. | Email                                      |
+-------------------------------------------------+
| 3. | EXIT                                       |
+-------------------------------------------------+
"""
            )
            find = input("[ 1 - 2 - 3 ] -->")

            if find == "1":
                id = input("Enter the ID of the person to find :")
                cursor.execute("SELECT * FROM MANAGER WHERE ID = '{}' ;".format(id))
                data = cursor.fetchall()

                for i in data:
                    print("+-------------------------------------------------+")
                    print("| ID            |", i[0])
                    print("| Name          |", i[1])
                    print("| Email         |", i[2])
                    print("| Password      |", i[3])
                    print("| Contact       |", i[4])
                    print("+-------------------------------------------------+")
                    exit = input("Press return to exit")

            elif find == "2":
                email = input("Enter the email [ case sensitive ] :")
                cursor.execute(
                    "SELECT * FROM MANAGER WHERE EMAIL = '{}' ;".format(email)
                )
                data = cursor.fetchall()
                exit = input("Press return to exit")

                for i in data:
                    print("+-------------------------------------------------+")
                    print("| ID            |", i[0])
                    print("| Name          |", i[1])
                    print("| Email         |", i[2])
                    print("| Password      |", i[3])
                    print("| Contact       |", i[4])
                    print("+-------------------------------------------------+")
                    exit = input("Press return to exit")

            elif find == "3":
                print("+-------------------------------------------------+")
                print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
                print("+-------------------------------------------------+")
                exit = input("Press return to exit")
                break

            else:
                print("+-------------------------------------------------+")
                print("|   I  N  V  A  L  I  D     C  O  M  M  A  N  D   |")
                print("+-------------------------------------------------+")
                exit = input("Press return to exit")

        elif ch == "4":
            print(
                """
+-------------------------------------------------+
|    choose   what   information   to   display   |
+-------------------------------------------------+
| 1. | Name                                       |
+-------------------------------------------------+
| 2. | Email                                      |
+-------------------------------------------------+
| 3. | Both Name and Email                        |
+-------------------------------------------------+
| 4. | EXIT                                       |
+-------------------------------------------------+
"""
            )
            choose = input(" [ 1 - 2 - 3 ] --> ")

            if choose == "1":
                cursor.execute("SELECT * FROM MANAGER ;")
                data = cursor.fetchall()

                for i in data:
                    print("+-------------------------------------------------+")
                    print("| Name     |", i[1])
                    print("+-------------------------------------------------+")
                    exit = input("Press return to exit")

            elif choose == "2":
                cursor.execute("SELECT * FROM MANAGER ;")
                data = cursor.fetchall()

                for i in data:
                    print("+-------------------------------------------------+")
                    print("| Email    |", i[2])
                    print("+-------------------------------------------------+")
                    exit = input("Press return to exit")

            elif choose == "3":
                cursor.execute("SELECT * FROM MANAGER ;")
                data = cursor.fetchall()

                for i in data:
                    print("+-------------------------------------------------+")
                    print("| Name     |", i[1])
                    print("| Email    |", i[2])
                    print("+-------------------------------------------------+")
                    exit = input("Press return to exit")

            elif choose == "4":
                print("+-------------------------------------------------+")
                print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
                print("+-------------------------------------------------+")
                exit = input("Press return to exit")
                break

            else:
                print("+-------------------------------------------------+")
                print("|   I  N  V  A  L  I  D     C  O  M  M  A  N  D   |")
                print("+-------------------------------------------------+")
                exit = input("Press return to exit")
                break

        elif ch == "5":
            print("+-------------------------------------------------+")
            print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
            print("+-------------------------------------------------+")
            exit = input("Press return to exit")
            break

        else:
            print("+-------------------------------------------------+")
            print("|   I  N  V  A  L  I  D     C  O  M  M  A  N  D   |")
            print("+-------------------------------------------------+")
            exit = input("Press return to exit")
            break

elif ch == "3":
    print("+-------------------------------------------------+")
    print("|  T E R M I N A T I N G   A P P L I C A T I O N  |")
    print("+-------------------------------------------------+")
    exit = input("Press return to exit")

else:
    print("+-------------------------------------------------+")
    print("|   I  N  V  A  L  I  D     C  O  M  M  A  N  D   |")
    print("+-------------------------------------------------+")
    exit = input("Press return to exit")

server_connection.close()
