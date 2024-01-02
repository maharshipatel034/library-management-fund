import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="12345")
c=db.cursor()
c.execute("Create database if not exists library")
c.execute("Use library")
c.execute("Create table if not exists member(mem_code varchar(10) primary key,mem_name varchar(20),mobile varchar(20),dom date,address varchar(20))")
print("Table Created")
def insert_member():
    try:
        mid=input("Enter member_id : ")
        mname=input("Enter member Name : ")
        mob=input("Enter mobile number : ")
        date=input("Enter daye of membership : ")
        add=input("Enter address : ")
        q1="Insert into member values('"+mid+"','"+mname+"','"+mob+"','"+date+"','"+add+"')"
        c.execute(q1,)
        db.commit()
        print("Data inserted Successfully")
    except:
        print("error")
    
def delete():
    try:
        iid=input("enter member id to be deleted")
        c.execute("delete from member where mem_code='"+iid+"'")
        db.commit()
    except:
        print("error")
def search():
    try:
        ch=int(input("enter 1.search through mobile number/n2.search through name"))
        if ch==1:
            mobi=input("enter mobile number to be searched :")
            m="%"+mobi+"%"
            c.execute("select * from member where mobile like '"+m+"'")
            for i in c:
                print(i)
        if ch==2:
            nam=input("enter name to be searched:")
            n="%"+nam+"%"
            c.execute("select * from member where mem_name like '"+n+"'")
            for i in c:
                print(i)
    except:
        print("eroor")
def display():
    c.execute("select * from member")
    for i in c:
        print(i)
