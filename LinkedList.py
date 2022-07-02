class LinkedList:
    class Node:
        def __init__(self,data):
            self.data = data
            self.link = None
    def __init__(self):
        self.head = None
    def traversingLL(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            while temp is not None:
                if temp.link is not None:
                    print(temp.data,end = "-->")
                else:
                    print(temp.data)
                temp = temp.link
    def insertAtBegining(self,data):
        newNode = self.Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.link = self.head
            self.head = newNode
    def insertAtEnd(self,data):
        newNode = self.Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.link is not None:
                temp = temp.link
            temp.link = newNode
    def insertAtAnyPosition(self,pos,data):
        newNode = self.Node(data)
        temp = self.head
        while temp and pos !=1:
            temp = temp.link
            pos -= 1
        newNode.link = temp.link
        temp.link = newNode
    def deleteAtBegining(self):
        if self.head is None:
            print("Deletion is not possible ")
        else:
            print("Deleted node is : ",self.head.data)
            self.head = self.head.link
    def deleteAtEnd(self):
        if self.head is None:
            print("Deletion is not possible ")
        else:
            temp = self.head
            while temp.link.link:
                temp = temp.link
            print("Deleted node is ",temp.link.data)
            temp.link = None
    def deleteAtAnyPosition(self,pos):
        temp = self.head
        while temp and pos!=1:
            temp = temp.link
            pos -=1
        print("Deleted Node is : ",temp.link.data)
        temp.link = temp.link.link

    def count(self):
        temp = self.head
        c = 0
        while temp:
            c += 1
            temp = temp.link
        return c


def main():
    inp = True
    obj = LinkedList()
    while inp ==True:
        print("Press 1 to insert at begining\n"
        "Press 2 to insert at ending\n"
        "Press 3 to insert at any position\n"
        "Press 4 to delete at begining\n"
        "press 5 to delete at end\n"
        "press 6 to delete at any position\n"
        "press 7 to display\n"
        "Press any other number to exit")
        try:
            n = int(input("Enter your choice : "))
            if n==1:
                d = int(input("Enter the data : "))
                obj.insertAtBegining(d)
            elif n==2:
                d = int(input("Enter the data : "))
                obj.insertAtEnd(d)
            elif n==3:
                d = int(input("Enter the data : "))
                print("Position should not be greater than ",obj.count())
                p = int(input("Enter the position : "))
                while p>obj.count():
                    print("Position should not be greater than ",obj.count())
                    p = int(input("Enter the position : "))
                    
                if p == 0:
                    obj.insertAtBegining(d)
                else:
                    obj.insertAtAnyPosition(p,d)
            elif n==4:
                obj.deleteAtBegining()
            elif n==5:
                obj.deleteAtEnd()
            elif n==6:
                print("Position should not be greater than ",obj.count()-1)
                p = int(input("Enter the position : "))
                while p>obj.count()-1 or p < 0:
                    print("Position should not be greater than ",obj.count()-1)
                    p = int(input("Enter the position : "))
                if p == 0:
                    obj.deleteAtEnd()
                else:
                    obj.deleteAtAnyPosition(p)
            elif n==7:
                obj.traversingLL()
            else:
                inp = False
        except:
            print("Input Error")



if __name__ == "__main__":
    main()