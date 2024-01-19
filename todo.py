import json
class TodoList:
    toDoItem = []

    def addItem(self, name):
        self.toDoItem.append(name)
        self.writeToJson()

    def removeItems(self, index):
        try:
            del self.toDoItem[index]
            self.writeToJson()
        except:
            print("invalid index")

    def viewAllItem(self):
        print("***************Start**************")
        for item in self.readFromJson():
            print(item)
        print("***************End**************")
    def writeToJson(self):
        file_path = "example_list.json"
        with open(file_path, "w") as json_file:
            json.dump(self.toDoItem, json_file, indent=2)
            
    def readFromJson(self):
        file_path_read = "example_list.json"
        with open(file_path_read, "r") as json_file:
            loaded_data = json.load(json_file)
            self.toDoItem = loaded_data
            return loaded_data


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