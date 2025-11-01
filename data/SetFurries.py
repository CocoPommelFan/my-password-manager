import pyperclip
from base_operation import BaseOperation, Colors
import json
from pathlib import Path
import random
import string

class SetFurries(BaseOperation):
    def execute(self):
        try:
            while True:
                ln = self.getMaxLength()
                
                if ln == 66026703679:
                    return
                
                service = self.getService()
                
                unique_chars = self.getUniqueChars()
                psw = self.genPass(unique_chars, ln)
                
                data = self.genData(service, psw)
                self.setData(data)
                
                self.printResult(psw, service)
                
        except KeyboardInterrupt:
            self.consoleСlear()

    
        
    def getAllCharacters(self) -> str:
        all_char = string.ascii_letters + string.digits + string.punctuation
        return all_char

    def getMaxLength(self) -> int:
        while True:
            print("Длина пароля: ", end='')
            try:
                ln = input()
                return int(ln)
            except Exception as e:
                if e == "KeyboardInterrupt":
                    return 66026703679
                print(f"{Colors.RED}Неверные данные{Colors.END}")

    def getService(self) -> str:
        print("Cервис: ", end='')
        _service = input()
        return _service

    def getUniqueChars(self) -> list:
        secure = random.SystemRandom()
        return [
            secure.choice(string.ascii_lowercase),    # строчная буква
            secure.choice(string.ascii_uppercase),    # заглавная буква  
            secure.choice(string.digits),             # цифра
            secure.choice(string.punctuation)         # спецсимвол
        ]
        
    def isExist(self) -> bool:
        if Path(self.json_path).exists():
            return True
        else:  
            return False
        
    def addList(self) -> None:
        with open(self.json_path, "w", encoding="utf-8") as file:
            json.dump([], file) 
        return

    def isEmpty(self) -> bool:
        if Path(self.json_path).stat().st_size == 0:
            return True
        else:
            return False
                
    def createFile(self) -> None:
        with open(self.json_path, "w", encoding="utf-8") as file:
            json.dump([], file) 
            return 
        
    def getData(self) -> list:
        if not self.isExist():
            self.createFile()
        if self.isEmpty():
            self.addList()

        with open(self.json_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def setData(self, data: dict) -> None:
        new_data = self.getData()
        new_data.append(data)
        
        with open(self.json_path, "w", encoding="utf-8") as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)
        return
    
    def genPass(self, unique_char: list, ln: int) -> str:
        secure = random.SystemRandom()
        all_char = self.getAllCharacters()
        unique_char += [secure.choice(all_char) for _ in range(ln - 4)]
        secure.shuffle(unique_char)
        return ''.join(unique_char)

    def genData(self, service: str, password: str) -> dict:
        data = {
                "service": service,
                "password": password
            }
        return data

    def printResult(self, psw: str, service: str) -> None:
        self.consoleСlear()
        print(f"Пароль {Colors.YELLOW}{psw}{Colors.END} для сервиса {Colors.YELLOW}{service}{Colors.END} был {Colors.GREEN}добавлен{Colors.END} и {Colors.GREEN}скопирован в буфер обмена.{Colors.END}")
        pyperclip.copy(psw)
        
        
