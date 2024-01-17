class TodoList:
    toDoItem = []

    def addItem(self, name):
        self.toDoItem.append(name)

    def removeItems(self, index):
        try:
            del self.toDoItem[index]
        except:
            print("invalid index")

    def viewAllItem(self):
        print("***************Start**************")
        for item in self.toDoItem:
            print(item)
        print("***************End**************")


option = 1
todo = TodoList()
while option != 4:
    option = int(input("Enter options 1:Add 2:Delete 3:View 4:Exit"))
    if option == 1:
        todoName = input("Enter the todod item")
        todo.addItem(todoName)
    elif option == 2:
        index = int(input("Enter index to delete"))
        todo.removeItems(index)
    elif option == 3:
        todo.viewAllItem()
    else:
        break