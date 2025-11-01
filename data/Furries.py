import os
from SetFurries import SetFurries
from GetFurries import GetFurries

class Manager:
    def __init__(self) -> None:
        self.operations = {
            "1": SetFurries(),
            "2": GetFurries(),
        }
        
    def consoleСlear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def showMenu(self) -> None:
        print("1) Генерация пароля")
        print("2) Получить пароль")
        print("0) Выход")
        
    def run(self):
        try:
            while True:
                self.showMenu()
                
                choice = input()
                
                self.consoleСlear()
                
                if choice == '0':
                    quit()
                
                if choice in self.operations:
                    operation = self.operations[choice]
                    operation.execute()
                else:
                    print("Неверный выбор")
        except KeyboardInterrupt:
            self.consoleСlear()