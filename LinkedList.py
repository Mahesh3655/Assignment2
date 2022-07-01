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

def main():
    inp = True
    obj = LinkedList()
    while inp ==True:
        print("Press 1 to insert at begin\n"
        "Press 2 to insert at ending\n"
        "Press 3 to insert at any position\n"
        "Press 4 to display\n"
        "Press any other number to exit")
        n = int(input("Enter your choice : "))
        if n==1:
            d = int(input("Enter the data : "))
            obj.insertAtBegining(d)
        elif n==2:
            d = int(input("Enter the data : "))
            obj.insertAtEnd(d)
        elif n==3:
            d = int(input("Enter the data : "))
            p = int(input("Enter the position : "))
            obj.insertAtAnyPosition(d,p)
        elif n==4:
            obj.traversingLL()
        else:
            inp = False



if __name__ == "__main__":
    main()

