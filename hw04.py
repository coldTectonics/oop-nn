import pickle

class Client:

    def __init__ (self, name, number):

        self._name = None
        self.name = name
        self._number = None
        self.number = number
        self.pets = []

    def addPet (self, name, age):

        self.pets.append (Pet (name, age))

    @property
    def name (self):  # Геттер
        return self._name

    @property
    def number (self):  # Геттер
        return self._number

    @name.setter
    def name (self, new_name):  # Сеттер с проверкой
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть строкой")
        if not new_name.strip():  # Проверяем, не пустая ли строка
            raise ValueError("Имя не может быть пустым")
        if not new_name.isalpha():  # Проверяем, содержит ли только буквы
            raise ValueError("Имя должно содержать только буквы")

        self._name = new_name  

    @number.setter
    def number (self, new_number):  # Сеттер с проверкой
        if not isinstance(new_number, int):
            raise TypeError("номер...")

        self._number = new_number 


class Pet:

    def __init__ (self, name, age):

        self._name = None
        self.name = name
        self._age = None
        self.age = age
        self.current_visit = 0
        self.visits = {}

    @property
    def name (self):  # Геттер
        return self._name

    @property
    def age (self):  # Геттер
        return self._number

    @name.setter
    def name (self, new_name):  # Сеттер с проверкой
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть строкой")
        if not new_name.strip():  # Проверяем, не пустая ли строка
            raise ValueError("Имя не может быть пустым")
        if not new_name.isalpha():  # Проверяем, содержит ли только буквы
            raise ValueError("Имя должно содержать только буквы")

        self._name = new_name  

    @age.setter
    def age (self, new_age):  # Сеттер с проверкой
        if not isinstance(new_age, int):
            raise TypeError("возраст...")

        self._age = new_age 


class Interface:

    def __init__ (self):
        self.clients = []
        self.input_data = [0, 0, 0, 0, 0] #0 - имя клиента, 1 - телефон, 2 - количество питомцев, 3 - имя питомца, 4 - возраст
        self.prog_state = 0

    def mainScreen (self):

        print ('\n\nДобавить клиента: 1') #v
        print ('Найти клиента по имени: 2') #v
        print ('Найти клиента по номеру: 22') #v
        print ( 'Посмотреть записи о приёмах: 3') #v
        print ( 'Проверить запись: 4') #v
        print ( 'Записать на новый приём: 5') #v
        print ( 'Отметить приём проведённым: 6') #v
        print ( 'Внести комментарий: 7') #v

        print ( '0 чтобы выйти из программы')

        self.prog_state = input ('\nВведите команду\n')

    def registerClient (self):

        self.input_data[0] = input ('\nВведите имя клиента\n')
        self.input_data[1] = int(input ('\nВведите телефон клиента\n'))

        self.clients.append (Client (self.input_data[0], self.input_data[1]))

        self.input_data[2] = int(input ('\nВведите число питомцев\n'))
        if self.input_data[2] > 0:
            for i in range (self.input_data[2]):
                self.input_data[3] = input ('\nВведите имя питомца\n')
                self.input_data[4] = int(input ('\nВведите возраст\n'))

                self.clients[-1].addPet (self.input_data[3], self.input_data[4])

        print (f'добавлен клиент {self.clients[-1].name}')
        for i in range (self.input_data[2]):
            print (f'добавлен питомец {self.clients[-1].pets[i].name}')

        self.input_data = [0, 0, 0, 0, 0]

    def searchByName (self, name):

        for person in self.clients:
            if person.name == name:
                print (f'{person.name} найден в базе. Телефон: {person.number}')
            else:
                print ('Не найдено')

    def searchByNumber (self, number):

        for person in self.clients:
            if person.number == number:
                print (f'{person.number} найден в базе. Клиент: {person.name}')
            else:
                print ('Не найдено')

    def listAppointments (self, client_name, pet_name):

        for person in self.clients:
            if person.name == client_name:

                for pet in person.pets:
                    if pet.name == pet_name:
                        print ('Список приёмов:', pet.visits)
                    else:
                        print ('Хозяин или питомец не найден')

    def writeAppointment (self, client_name, pet_name):

        for person in self.clients:
            if person.name == client_name:

                for pet in person.pets:
                    if pet.name == pet_name:
                        if pet.current_visit != 0:
                            pet.visits[pet.current_visit] = ''
                            print ('Приём добавлен в историю')
                            pet.current_visit = 0
                    else:
                        print ('Хозяин или питомец не найден')

    def newAppointment  (self, visit, client_name, pet_name):

        for person in self.clients:
            if person.name == client_name:

                for pet in person.pets:
                    if pet.name == pet_name:
                        pet.current_visit = visit
                        print ('Клиент записан')
                    else:
                        print ('Хозяин или питомец не найден')

    def currentAppointment  (self, client_name, pet_name):

        for person in self.clients:
            if person.name == client_name:

                for pet in person.pets:
                    if pet.name == pet_name:
                        print ('Следующий приём:', pet.current_visit)
                    else:
                        print ('Хозяин или питомец не найден')

    def addComment (self, visit, comment, client_name, pet_name):

        for person in self.clients:
            if person.name == client_name:

                for pet in person.pets:
                    if pet.name == pet_name:
                        pet.visits[visit] = comment
                        print ('Комментарий добавлен')
                    else:
                        print ('Хозяин или питомец не найден')

    def saveDB (self, db):

        with open('db.pickle', 'wb') as handle:
            pickle.dump(db, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def loadDB (self):

        with open('db.pickle', 'rb') as handle:
            b = pickle.load(handle)
        return b

if __name__ == '__main__': 

    interface = Interface ()
    interface.clients = interface.loadDB ()

    while True:
        interface.mainScreen ()
        if interface.prog_state == '1':
            interface.registerClient ()

        if interface.prog_state == '2':
            interface.input_data [0] = input ('\nВведите имя клиента\n')
            interface.searchByName (interface.input_data [0])

        if interface.prog_state == '22':
            interface.input_data[1] = int(input ('\nВведите телефон клиента\n'))
            interface.searchByNumber (interface.input_data [1])

        if interface.prog_state == '3':
            interface.input_data [0] = input ('\nВведите имя клиента\n')
            interface.input_data [3] = input ('\nВведите имя питомца\n')
            interface.listAppointments (interface.input_data [0], interface.input_data [3])

        if interface.prog_state == '4':
            interface.input_data [0] = input ('\nВведите имя клиента\n')
            interface.input_data [3] = input ('\nВведите имя питомца\n')
            interface.currentAppointment (interface.input_data [0], interface.input_data [3])

        if interface.prog_state == '5':
            interface.input_data [0] = input ('\nВведите имя клиента\n')
            interface.input_data [3] = input ('\nВведите имя питомца\n')
            interface.input_data [2] = input ('\nВведите дату\n')
            interface.newAppointment (interface.input_data [2], interface.input_data [0], interface.input_data [3])

        if interface.prog_state == '6':
            interface.input_data [0] = input ('\nВведите имя клиента\n')
            interface.input_data [3] = input ('\nВведите имя питомца\n')
            interface.writeAppointment (interface.input_data [0], interface.input_data [3])

        if interface.prog_state == '7':
            interface.input_data [0] = input ('\nВведите имя клиента\n')
            interface.input_data [3] = input ('\nВведите имя питомца\n')
            interface.input_data [2] = input ('\nВведите дату посещения\n')
            interface.input_data [4] = input ('\nВведите комментарий\n')
            interface.addComment (interface.input_data [2], interface.input_data [4], interface.input_data [0], interface.input_data [3])

        if interface.prog_state == '0':
            interface.saveDB (interface.clients) 
            break

        interface.input_data = [0, 0, 0, 0, 0]
