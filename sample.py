import mysql.connector
mydb= mysql.connector.connect(host= 'localhost',user='root',password='',database='employes')
mycursor= mydb.cursor()

from secrets import choice


while True:
    print("select an option from the menu")
    print("1. add student")
    print("2.view student")
    print("3.search student")
    print("4.upadte student")
    print("5. delete student")
    print("6.exit")

    choice=int(input("enter your choice"))
    if(choice==1):
        print("student enter selected")
        name=input("enter a name")
        pin=input("enter pin")
        sql="INSERT INTO `emp`(`name`, `pin`) VALUES (%s,%s)"
        data=(name,pin)
        mycursor.execute(sql,data)
        mydb.commit()
    elif(choice==2):
        print("view student")
    elif(choice==3):
        print("search a student")
    elif(choice==4):
        print("update student")
    elif(choice==5):
        print("delet student")    
    elif(choice==6):
        break                              