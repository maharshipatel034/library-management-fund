import member
import issue
import book
def menumember():
    while True:
        print("\n*********** member record managment*********")
        print("\n1.add member")
        print("\n2.display member record")
        print("\n3.search")
        print("\n4.delete")
        print("\n5 return to main menu")
        ch=int(input("enter your choice:"))
        if ch==1:
            member.insert_member()
        elif ch==2:
            member.display()
        elif ch==3:
            member.search()
        elif ch==4:
            member.delete()
        elif ch==5:
            break
        else:
            print("wrong choice")
            x=input("eneter any thing")

def menubook():
    while True:
        print("\n*********** book record managment*********")
        print("\n1.add book")
        print("\n2.display book record")
        print("\n3.search")
        print("\n4.delete")
        print("\n5 edit book")
        print("\n6. return to book menu")
        ch=int(input("enter your choice:"))
        if ch==1:
            book.insert_book()
        elif ch==2:
            book.display_book()
        elif ch==3:
            book.search_book()
        elif ch==4:
            book.delete_book()
        elif ch==5:
            book.edit_book
        elif ch==6:
            break
        else:
            print("wrong choice")
            x=input("eneter any thing")

def menuissue():
    while True:
        print("\n*********** member record managment*********")
        print("\n1.issue book")
        print("\n2.return book")
        print("\n3.dispaly issue books")
        print("\n4 return to main menu")
        ch=int(input("enter your choice:"))
        if ch==1:
            issue.issuebook()
        elif ch==2:
            issue.returnbook()
        elif ch==3:
            issue.showallissuebook()
        elif ch==4:
            break
        else:
            print("wrong choice")
            x=input("eneter any thing")
            
        
