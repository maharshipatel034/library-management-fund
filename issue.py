from datetime import date
import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="12345")
c=db.cursor()
c.execute("Use library")
c.execute("create table if not exists issue(bcode varchar(20),mcode varchar(30),doi date,dor date)")
print("Table Created")

def issuebook():
    bno=input("enter book code to issue:")
    mno=input("enter member code:")
    doi=input("enter issue date:")
    qry="insert into issue(bcode,mcode,doi) values('"+bno+"','"+mno+"','"+doi+"')"
    c.execute(qry)
    db.commit()
    print("record inserted")

def returnbook():
    bno=input("enter book code to return book:")
    mno=input("enter member code who is returing book:")
    rd=date.today()
    qry="update issue set dor='"+rd+"' where bcode='"+bno+"' and mcode='"+mno+"' "
    c.execute(qry)
    db.commit()
    print("*******book retured successfully*****")

def showallissuebook():
    qry="select b.bookcode,m.mem_code,doi,dor from member m, bookrecord b,issue i where m.mem_code=i.mcode and b.bookcode=i.bcode"
    c.execute(qry)

    for i in c:
        print(i)

    print("****successfull*********")
    
