import curses
import time
import keyboard
import random

class Building: #класс здания

    def __init__ (self):
        self.cost = 0
        self.happiness_mod = 0
        self.education_mod = 0
        self.ecology_mod = 0
        self.population_mod = 0
        self.x = []
        self.y = []
        self.code = 0

    def returnStats (self):
        pass

    def randomEffect (self):
        pass

    def build (self, city, code):
        city.balance -= self.cost #бюджет
        city.population += self.population_mod #население
        city.happiness += self.happiness_mod #радость
        city.education += self.education_mod #образование
        city.ecology += self.ecology_mod #экология
        city.build_numbers[code] += 1 #количество зданий

        self.x.append (random.randint (1,38))
        self.y.append (random.randint (1,22))

class Flats (Building):
    def __init__ (self):
        super().__init__ ()
        self.cost = 100000
        self.population_mod = 1000
        self.code = 0

class Factory (Building):
    def __init__ (self):
        super().__init__ ()
        self.cost = 500000
        self.ecology_mod = -1
        self.happiness_mod = -5
        self.code = 1

class Theatre (Building):
    def __init__ (self):
        super().__init__ ()
        self.cost = 50000
        self.happiness_mod = 1
        self.code = 2

class School (Building):
    def __init__ (self):
        super().__init__ ()
        self.cost = 100000
        self.education_mod = 1
        self.happiness_mod = 5
        self.code = 3

class Hospital (Building):
    def __init__ (self):
        super().__init__ ()
        self.cost = 500000
        self.happiness_mod = 10
        self.code = 4

class Station (Building):
    def __init__ (self):
        super().__init__ ()
        self.cost = 100000
        self.happiness_mod = 3
        self.code = 5


class City: #класс города

    def __init__ (self):
        self.builds = []

    def __iter__(self):
        return CollectorIterator(self.builds)

    def addBuilding (self, house):
        self.builds.append (house)


class Game: #основной класс игры

    def __init__ (self):

       self.balance = 1000000 #бюджет
       self.income = 0 #доходы
       self.population = 0 #население
       self.happiness = 0 #радость
       self.education = 0 #образование
       self.ecology = 0 #экология

       self.build_number = 0 #количество зданий
       self.score = 0 #счёт игры
       self.day = 1 #счётчик дня
       self.month = 1 #счётчик месяца

       self.current = 0 #счётчик секунд с начала игры
       self.start = time.time()

       self.state = 0 #состояние игры
       self.build_numbers = [0, 0, 0, 0, 0, 0]

    def countTime (self): #счётчик внутриигрового времени
        self.current = round(time.time() - self.start, 0)

        if self.current != 0:
            self.day = int(self.current)

            if self.current == 30:
                self.start = time.time ()
                self.month += 1
                

    def mainScreen (self): #заглавный экран

        screen.erase ()
        screen.border('|', '|', '-', '-', '+', '+', '+', '+')


        game.countTime ()

        screen.addstr (1, 2, ('Месяц: ' + str(self.month) + ' День: ' + str(self.day)), curses.A_STANDOUT)
        screen.addstr (3, 2, ('Счёт: ' + str (self.score)))
        screen.addstr (4, 2, ('Бюджет: ' + str (self.balance)))

        screen.addstr (6, 2, 'Меню строительства: F')
        screen.addstr (7, 2, 'Список строений: G')
        screen.addstr (8, 2, 'Показатели города: H')

        screen.addstr (10, 2, '''
       _____________
      /            /|   
     /____________/ |   
    |            |  |   
    |   █ █ █    | █|   
    |   █ █ █    | /    
    |____________|/     ''')


        screen.addstr (22, 2, 'ESC чтобы выйти из игры')
        screen.border()
        self.drawMap ()
        self.countScore ()

        key = stdscr.getch() #определяем нажатие
        if key == 102: #f
            self.state = 1
        if key == 103: #g
            self.state = 2
        if key == 104: #h
            self.state = 3

        if key == 27: #esc
            self.state = 5

        screen.refresh ()

    def buildingScreen (self, city): #экран строительства

        screen.erase ()
        screen.border()
        self.drawMap ()
        self.countScore ()

        game.countTime ()

        screen.addstr (1, 2, ('Месяц: ' + str(self.month) + ' День: ' + str(self.day)), curses.A_STANDOUT)
        screen.addstr (3, 2, ('Бюджет: ' + str (self.balance)))
        screen.addstr (5, 2, ('1: ЖИЛЬЁ'))
        screen.addstr (6, 2, ('2: ЗАВОД'))
        screen.addstr (7, 2, ('3: ТЕАТР'))
        screen.addstr (8, 2, ('4: ШКОЛА'))
        screen.addstr (9, 2, ('5: БОЛЬНИЦА'))
        screen.addstr (10, 2, ('6: СТАНЦИЯ МЕТРО'))

        screen.addstr (22, 2, 'ESC чтобы вернуться')

        key = stdscr.getch() #определяем нажатие
        if key == 27: #esc
            self.state = 0

        if key == 49: #1
            flats.build (self, flats.code)

        if key == 50: #2 
            factory.build (self, factory.code)

        if key == 51: #3
            theatre.build (self, theatre.code)

        if key == 52: #4
            school.build (self, school.code)

        if key == 53: #5
            hospital.build (self, hospital.code)

        if key == 54: #6
            station.build (self, station.code)


        screen.refresh ()

    def listScreen (self, city): #список строений

        screen.erase ()
        screen.border()
        self.drawMap ()
        self.countScore ()

        game.countTime ()

        screen.addstr (1, 2, ('Месяц: ' + str(self.month) + ' День: ' + str(self.day)), curses.A_STANDOUT)
        screen.addstr (3, 2, ('# Жилые дома: ' + str (self.build_numbers[0])))
        screen.addstr (4, 2, ('% Фабрики: ' + str (self.build_numbers[1])))
        screen.addstr (5, 2, ('@ Развлечения: ' + str (self.build_numbers[2])))
        screen.addstr (6, 2, ('& Школы: ' + str (self.build_numbers[3])))
        screen.addstr (7, 2, ('№ Больницы: ' + str (self.build_numbers[4])))
        screen.addstr (8, 2, ('= Транспорт: ' + str (self.build_numbers[5])))

        screen.addstr (22, 2, 'ESC чтобы вернуться')

        key = stdscr.getch() #определяем нажатие
        if key == 27: #esc
            self.state = 0

        screen.refresh ()

    def statsScreen (self): #игровая статистика

        screen.erase ()
        screen.border()
        self.drawMap ()
        self.countScore ()

        game.countTime ()

        screen.addstr (1, 2, ('Месяц: ' + str(self.month) + ' День: ' + str(self.day)), curses.A_STANDOUT)
        screen.addstr (3, 2, ('Счёт: ' + str (self.score)))
        screen.addstr (4, 2, ('Бюджет: ' + str (self.balance)))
        screen.addstr (6, 2, ('Население: ' + str (self.population)))
        screen.addstr (7, 2, ('Счастье: ' + str (self.happiness)))
        screen.addstr (8, 2, ('Образование: ' + str (self.education)))
        screen.addstr (9, 2, ('Экология: ' + str (self.ecology)))

        screen.addstr (22, 2, 'ESC чтобы вернуться')

        key = stdscr.getch() #определяем нажатие
        if key == 27:
            self.state = 0

        screen.refresh ()

    def drawMap (self):
        box1.box()

        if self.build_numbers[0] > 0:
            for i in range (0, self.build_numbers[0]):
                box1.addstr (flats.y[i],flats.x[i], '#')

        if self.build_numbers[1] > 0:
            for i in range (0, self.build_numbers[1]):
                box1.addstr (factory.y[i],factory.x[i], '%')

        if self.build_numbers[2] > 0:
            for i in range (0, self.build_numbers[2]):
                box1.addstr (theatre.y[i],theatre.x[i], '@')

        if self.build_numbers[3] > 0:
            for i in range (0, self.build_numbers[3]):
                box1.addstr (school.y[i],school.x[i], '&')

        if self.build_numbers[4] > 0:
            for i in range (0, self.build_numbers[4]):
                box1.addstr (hospital.y[i],flats.x[i], '№')

        if self.build_numbers[5] > 0:
            for i in range (0, self.build_numbers[5]):
                box1.addstr (station.y[i],station.x[i], '=')

    def countScore (self):
        self.score = int(self.ecology + self.happiness + self.education*10 + self.population / 1000 + self.month * 10)


class CollectorIterator: #итератор

    def __init__(self, some_objects):
        self.some_objects = some_objects
        self.current = 0

    def to_start(self):
        self.current = 0

    def to_current(self, val):
        if val >= len(self.some_objects) or val < 0:
            print("Неверное значение")
        else:
            self.current = val

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < len(self.some_objects):
            result = self.some_objects[self.current]
            self.current += 1
            return result
        raise StopIteration


if __name__ == '__main__': #тело программы

    stdscr = curses.initscr()
    stdscr.nodelay(True)
    screen = curses.initscr ()
    curses.curs_set(False)
    box1 = screen.subwin(0, 0, 0, 40)
    game = Game ()
    city = City ()

    #инициализация строений
    flats = Flats ()
    factory = Factory ()
    theatre = Theatre ()
    school = School ()
    hospital = Hospital ()
    station = Station ()

    #в коллекцию добавляем
    city.addBuilding (flats)
    city.addBuilding (factory)
    city.addBuilding (theatre)
    city.addBuilding (school)
    city.addBuilding (hospital)
    city.addBuilding (station)

    while True: #основной цикл игры

        while game.state == 0:
            game.mainScreen ()

        #if game.state == 1:
            
        while game.state == 1:
            game.buildingScreen (city)

        while game.state == 2:
            game.listScreen (city)

        while game.state == 3:
            game.statsScreen ()

        if game.state == 5:
            curses.endwin()
            break
