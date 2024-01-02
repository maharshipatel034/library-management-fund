import menu
while True:
        print("\n*********** main menu managment*********")
        print("\n1. member")
        print("\n2.book")
        print("\n3.issue")
        print("\n4 return to main menu")
        ch=int(input("enter your choice:"))
        if ch==1:
            menu.menumember()
        elif ch==2:
            menu.menubook()
        elif ch==3:
            menu.menuissue()
        elif ch==4:
            break
        else:
            print("wrong choice")
            x=input("eneter any thing")

