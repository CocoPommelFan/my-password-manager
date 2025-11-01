from abc import ABC, abstractmethod
import os
from pathlib import Path

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

class BaseOperation(ABC):
    
    script_path = Path(__file__).parent
    json_path = script_path / "furries.json"
    
    @abstractmethod
    def execute(self):
        pass
    
    def consoleСlear(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
    