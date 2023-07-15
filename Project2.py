import psycopg2
import random
connection=None
cur=None

# print("-> Registration    Enter 1")
# print("-> Login    Enter 2")
# choice=int(input("Enter the choice "))
# match choice:
#     case 1: 
#         Email_1=input("Enter the Email ID -> ")
#         Password_1=input("Enter the Password -> ")
#         Con_password=input("Enter the Password to confirm -> ")
#     case 2:
#         Email_2=input("Enter the Email ID -> ")
#         Password_2=input("Enter the Password -> ")

try:
    connection = psycopg2.connect(
    host = "127.0.0.1",
    port = "5432",
    database = "postgres",
    user="postgres",
    password="hunny"
    )
    cur=connection.cursor()

    # cur.execute('DROP TABLE IF EXISTS Contact')

    create_table='''CREATE TABLE IF NOT EXISTS Contact(
    id      SERIAL PRIMARY KEY,
    first_name    varchar(40) NOT NULL,
    last_name     varchar(40) NOT NULL,
    email   varchar(40),
    phone_no varchar(10)
    )'''
    cur.execute(create_table)
    while 1:
        print("What do you want to do ? \n")
        print("1  -> to view all saved contacts")
        print("2  -> to view a specific contact")
        print("3  -> to add a new contact")
        print("4  -> to delete all saved contacts")
        print("5  -> to delete a specific contact")
        print("6  -> to update an existing contact")
        print("7  -> to exit the program")

        action=int(input("Enter -> "))
        match action:
            case 1:
                cur.execute('SELECT * FROM Contact ORDER BY first_name ASC')  #Return the data and place into the cursor
                listofContact=cur.fetchall()                                 #view the return data use another mehtod fetchall()
                if listofContact==[]:
                    print("\nThere is no any Contact in the Contact list\n")
                for record in listofContact:
                    print(record) 
                    print()
            case 2:
                name=input("Enter the name of person whose contact u want to view : ")
                print()
                cur.execute('SELECT * FROM Contact WHERE first_name =%r'%(name,)) #The %r %(name,) syntax in Python is used to format a string with a variable value%r is used to represent the variable as a string, while %() is used to pass the variable value into the string1
                listofContact=cur.fetchall()
                if listofContact==[]:
                    print("\nNo one named '",name,"' is in the Contact list\n")
                for record in listofContact:
                    print(record) 
                    print()
            case 3:
                insert_into_table='INSERT INTO Contact(first_name,last_name,email,phone_no) VALUES (%s,%s,%s,%s)'
                insert_values=[input("Enter fist name -> "),input("Enter last name -> "),input("Enter Email -> "),input("Enter phone number -> ")]
                cur.execute(insert_into_table,insert_values)
                # for i in insert_values:                             #this way is use to insert row in the table 
                #     cur.execute(insert_into_table,i)
                connection.commit()
                print("\nNew Contact is Added into the Contact list Successfully.\n")
            case 4:
                cur.execute('SELECT * FROM Contact')  #Return the data and place into the cursor
                listofContact=cur.fetchall()                                 #view the return data use another mehtod fetchall()
                if listofContact==[]:
                    print("\nThere is no any Contact in the Contact list\n")
                else:
                    cur.execute('DELETE  FROM Contact')
                    connection.commit()
                    print("\nAll Saved Contact in the Contact list is deleted Successfully.\n")
            case 5:
                name=input("Enter the name of person whose contact u want to 'Delete' : ")
                print()
                cur.execute('SELECT * FROM Contact WHERE first_name =%r'%(name,))
                listofContact=cur.fetchall()
                if listofContact==[]:
                    print("\nNo one named '",name,"' is in the Contact list\n")
                elif len(listofContact)>1:
                    for record in listofContact:
                        print(record)
                    print("\nThere is more than one contact found whose name is",name,"\n")
                    idnumber=int(input("Please Specific the the id number to 'Update' that contact : "))
                    print()
                    cur.execute('DELETE FROM Contact WHERE id =%d'%(idnumber,))
                    connection.commit()
                    print("\nThe contact of ",name,"whose id number is",idnumber,"is deleted from the Contact list.\n")
                else:
                    cur.execute('DELETE FROM Contact WHERE first_name =%r'%(name,))
                    connection.commit()
                    print("\nThe contact of ",name,"is deleted from the Contact list.\n")
            case 6:
                name=input("Enter the name of person whose contact u want to 'Update' : ")
                print()
                cur.execute('SELECT * FROM Contact WHERE first_name =%r'%(name,))
                listofContact=cur.fetchall()
                if listofContact==[]:
                    print("\nNo one named '",name,"' is in the Contact list\n")
                elif len(listofContact)>1:
                    for record in listofContact:
                        print(record)
                    print("\nThere is more than one contact found whose name is",name,"\n")
                    idnumber=int(input("Please Specific the the id number to 'Update' that contact : "))
                    print()
                    while 1:
                        print("What do u want to update ?")
                        print("1  -> to update firstname")
                        print("2  -> to update lastname")
                        print("3  -> to update email")
                        print("4  -> to update phone number")
                        print("5  -> to Exit ")
                        choice=int(input("Enter ->"))
                        if choice==1:
                            firstname=input("Enter the new first_name :")
                            cur.execute('UPDATE Contact SET first_name=%r WHERE first_name=%r and id=%r'%(firstname,name,idnumber))
                        elif choice==2:
                            lastname=input("Enter the new last_name :")
                            cur.execute('UPDATE Contact SET last_name=%r WHERE first_name=%r and id=%r'%(lastname,name,idnumber))
                        elif choice==3:
                            new_email=input("Enter the new email :")
                            cur.execute('UPDATE Contact SET email=%r WHERE first_name=%r and id=%r'%(new_email,name,idnumber))
                        elif choice==4:
                            new_number=int(input("Enter the new phone_number :"))
                            cur.execute('UPDATE Contact SET phone_no=%r WHERE first_name=%r and id=%r'%(new_number,name,idnumber))
                        elif choice==5:
                            break
                        else:
                            print("\nEnter the right Choice \n")
                        connection.commit()
                        print("\nThe contact of ",name,"whose id number is",idnumber,"is Updated from the Contact list.\n")
                        break
                    
                else:
                    while 1:
                        print("What do u want to update ?")
                        print("1  -> to update firstname")
                        print("2  -> to update lastname")
                        print("3  -> to update email")
                        print("4  -> to update phone number")
                        print("5  -> to Exit ")
                        choice=int(input("Enter ->"))
                        if choice==1:
                            firstname=input("Enter the new first_name :")
                            cur.execute('UPDATE Contact SET first_name=%r WHERE first_name=%r'%(firstname,name))
                        elif choice==2:
                            lastname=input("Enter the new last_name :")
                            cur.execute('UPDATE Contact SET last_name=%r WHERE first_name=%r'%(lastname,name))
                        elif choice==3:
                            new_email=input("Enter the new email :")
                            cur.execute('UPDATE Contact SET email=%r WHERE first_name=%r'%(new_email,name))
                        elif choice==4:
                            new_number=int(input("Enter the new phone_number :"))
                            cur.execute('UPDATE Contact SET phone_no=%r WHERE first_name=%r'%(new_number,name))
                        elif choice==5:
                            break
                        else:
                            print("\nEnter the right Choice \n")
                        connection.commit()
                        print("\nThe contact of ",name,"is Updated from the Contact list.\n")
                        break
            case 7:
                print("\nThank YOU !\n")
                break
            case _:
                print("\nEnter the right Choice \n")
except Exception as error:
    print(error)
finally:
    if connection is not None:
        connection.close()
    if cur is not None:
        cur.close()
