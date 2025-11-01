from base_operation import BaseOperation, Colors
import pyperclip
import json
from pathlib import Path

class GetFurries(BaseOperation):

    def execute(self):   
        data = self.getData()
        try:
            while True:
                self.printServices(data)
                
                answer = self.isAnswerValid(data)
                
                if answer:  
                    self.toClipboard(data, answer)
                    
        except KeyboardInterrupt:
            self.consoleСlear()

    def getData(self) -> list:
        with open(self.json_path, 'r', encoding='utf-8') as file:
            _data = json.load(file)
        return _data

    def printServices(self, _data: list[dict]) -> None:
        for i, dictionary in enumerate(_data):
            print(f"{i + 1}) {dictionary.get("service")}")

    def validate(self, _answer: int, _length: int) -> bool:
        return 0 < _answer < _length
    
    def isAnswerValid(self, _data: list):
        while True:
            answer = int(input())
            if self.validate(answer, len(_data) + 1):
                self.consoleСlear()
                return answer
            else:
                self.consoleСlear()
                print("Сервис не найден")
                return False


    def toClipboard(self, _data: list[dict[str, str]], _answer: int) -> None:   
        value = _data[_answer - 1].get('password')
        service = _data[_answer - 1].get('service')
        if value: 
            pyperclip.copy(value)
        print(f"Пароль для {Colors.YELLOW}{service}{Colors.END} был {Colors.GREEN}скопирован в буфер обмена.{Colors.END}")
        
