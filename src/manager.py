import os
from tables import Table
from commands import Commands

def roll_question(self):
    tables = self.tables
    print("Insert the page you want to roll")
    id = 0
    for i in tables:
        print("ID: {0} {1}".format(id, i.name))
        id += 1
    
    id = ask_int("Id:")
    print(tables[int(id)].roll())
    input("enter to continue....")
    os.system('cls||clear')
    pass

def ask_int(question):
        try:
            return int(input(question))
        except ValueError:
            print("Invalid input")
            return ask_int(question)
            pass

def ask(question, commands : list[str]):
        a = input(question)
        if a in commands:
            return a
        
        print("Error: invalid response")
        return ask(question, commands)

class Manager:
    
    tables : list[Table] = []
    command_list : Commands 

    def __init__(self, tables : list[Table] = []):
        self.command_list = Commands()
        self.command_list.add_func(roll_question, "Roll items")
        self.tables = tables
        pass

    def start(self):
        while(True):
            self.process()
    
    def ask_func(self, start : int = 0):
        print("Select your task")
        id = 0
        for i in self.command_list.commands.keys():
            if id > 9:
                break
            print("ID: {0} {1} ".format(id, i))
            id += 1
        

        
        id = ask_int("id: ")
        os.system('cls||clear')
        name = self.command_list.get_command_name(id+start)
        func = self.command_list.get(name)
        return func

        pass


    def process(self):
        print("-----------------")
        fnc = self.ask_func(0)
        fnc(self)

        pass

    
    pass