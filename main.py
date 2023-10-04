from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class person():
    def __init__(self, birthday: date, name: str, race: str) -> None:      
        self._name: str = name
        self._birthday: date = birthday
        self._race: str = race

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str):
        if value != self._name:
            self._name = value

    @property
    def birthday(self) -> date:
        return self._birthday
    @birthday.setter
    def birthday (self, value:date):
        if value != self._birthday:
            self._birthday = value

    def getage(self) -> int:
        now = datetime.now()
        difference = relativedelta(now, self._birthday)
        return difference.years
    
    @property
    def race(self) -> str:
        return self._race
    @race.setter
    def race(self, value: str):
        if value != self._race:
            self._race = value

class man(person):
    @property
    def gender(self) -> str:
        return 'male'

class woman(person):
    @property
    def gender(self) -> str:
        return 'female'

mydate = date.fromisoformat('2007-12-31')
myperson = person(mydate, 'mary', 'white')
myage = myperson.getage()
print(f'{myperson.name} is {myage} years old and is {myperson.race}')

mywoman = woman(mydate, 'mary graham', 'pale')
mywomanage = mywoman.getage()
print(f'{mywoman.name} is a {mywoman.race} {mywoman.gender} because she is privileged and is {mywomanage} years old.')