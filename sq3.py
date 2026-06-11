import sqlite3
con=sqlite3.connect("std.db")
c=con.cursor()
c.execute("""
                CREATE TABLE IF NOT EXISTS student(
                id INTEGER PRIMARY KEY,
                name TEXT,
                course TEXT
            );
""")
c.execute("""
                CREATE TABLE IF NOT EXISTS marks(
                marki INTEGER PRIMARY KEY,
                id INTEGER,
                subject TEXT,
                mark INTEGER,
                FOREIGN KEY(id) REFERENCES student(id)
            );
""")
con.commit()

while True:
    print("\nSTUDENT GRADING SYSTEM\n")
    print("1.Add Student")
    print("2.View Students")
    print("3.Add Marks")
    print("4.View Marks")
    print("5.Update Marks")
    print("6.Delete Student")
    print("7.Calculate Grade")
    print("8.Exit")
    a=int(input("Enter Choice: "))

    if a==1:
        id=int(input("Enter Student id : "))
        name=input("Enter Name : ")
        course=input("Enter Course : ")
        c.execute(
                        "INSERT INTO student VALUES(?,?,?)",
                (id, name, course)
                 )
        con.commit()
        print("Student Added")
    elif a==2:
        c.execute("SELECT * FROM student")
        b=c.fetchall()
        for i in b:
            print(i)
    elif a==3:
        marki=int(input("Enter Mark id : "))
        id=int(input("Enter Student id : "))
        subject=input("Enter Subject : ")
        mark=int(input("Enter Mark : "))
        c.execute(
            "INSERT INTO marks VALUES(?,?,?,?)",
            (marki, id, subject, mark)
        )
        con.commit()
        print("Marks Added")
    elif a==4:
        c.execute("""
        SELECT student.name,
               marks.subject,
               marks.mark
        FROM student
        JOIN marks
        ON student.id=marks.id
        """)
        b=c.fetchall()
        for i in b:
            print(i)
    elif a==5:
        x=int(input("Enter Mark id : "))
        y=int(input("Enter New Mark : "))
        c.execute(
            "UPDATE marks SET mark=? WHERE marki=?",
            (y, x)
        )
        con.commit()
        print("Updated")
    elif a==6:
        id=int(input("Enter Student id : "))
        c.execute("DELETE FROM marks WHERE id=?",(id,))
        c.execute("DELETE FROM student WHERE id=?",(id,))
        con.commit()
        print("Deleted")
    elif a==7:
        id=int(input("Enter Student id : "))
        c.execute(
            "SELECT AVG(mark) FROM marks WHERE id=?",
            (id,)
        )
        x=c.fetchone()
        avg=x[0]
        if avg==None:
            print("No Marks Found")
        elif avg>=90:
            print("A+")
        elif avg>=80:
            print("B+")
        elif avg>=70:
            print("C+")
        elif avg>=60:
            print("D+")
        else:
            print("Fail")
    elif a==8:
        break
    else:
        print("INVALID CHOICE")
