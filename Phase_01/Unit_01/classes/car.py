from typing import List
from dataclasses import dataclass


class CarError(RuntimeError):
    ...

@dataclass
class Car:
    def __init__(self, manufacturer: str, model: str, mileage: int) -> None:
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = mileage

        self._door_opened = False
        self._engine_started = False

    def __str__(self) -> str:
        return f'{self.manufacturer} - {self.model}'
    
    def open_door(self) -> None:
        self.door_opened = True

    def close_door(self) -> None:
        self.door_opened = False

    def start_engine(self) -> None:
        self.engine_started = True

    def drive(self) -> None:
        if self.door_opened:
            raise CarError('You have to close the door first')

        if not self.engine_started:
            raise CarError('You have to start the engine in order to drive')
        
        print(f'{self} is driving')


ford_focus = Car('Ford', 'Focus', 233234)
ford_focus.open_door()
ford_focus.close_door()

ford_focus._engine_started = True
# ford_focus.start_engine()

try:
    ford_focus.drive()
except RuntimeError as e:
    print(f'Error: {e}')
