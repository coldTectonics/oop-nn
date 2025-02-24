class Ship:

    def __init__ (self, name, ship_type, pilot, engineer):
        
        self.name = name
        self.ship_type = ship_type
        self.pilot = pilot
        self.engineer = engineer

        self.hull = 100
        self.max_hull = 100
        self.weapons = []

    def add_weapon (self, weapon):

        self.weapons.append (weapon)

    def attack (self):

        self.pilot.attack ()
        for weapon in self.weapons:            
            print(f"{self.name} атакует с помощью {weapon.name} (урон {weapon.damage})")
            weapon.attack ()

    def repair (self):

        print(f"{self.name} был отремонтирован инженером {self.engineer.name} до полной прочности.")
        self.engineer.repair ()


class Crewmate:

    def __init__ (self, name):

        self.name = name


class Pilot (Crewmate):

    def __init__(self, name):

        super().__init__(name)

    def attack (self):
        
        pass


class Engineer (Crewmate):

    def __init__(self, name):

        super().__init__(name)

    def repair (self):

        pass


class Weapon:

    def __init__ (self, name, damage):

        self.name = name
        self.damage = damage

    def attack (self):
        
        pass


class Fleet:

    def __init__ (self):

        self.ships = []

    def add_ship (self, ship):

        self.ships.append (ship)

    def attack_all (self):

        print("Флот атакует!")
        for ship in self.ships:
            ship.attack ()

    def repair_all (self):

        print("\nФлот выполняет ремонт!")
        for ship in self.ships:
            ship.repair ()

if __name__ == '__main__': 

    laser = Weapon("Laser Cannon", 50)
    missile = Weapon("Missile Launcher", 100)

    pilot = Pilot("John Doe")
    engineer = Engineer("Jane Smith")

    ship1 = Ship("USS Enterprise", "battlecruiser", pilot, engineer)
    ship2 = Ship("Falcon", "frigate", Pilot("Han Solo"), Engineer("Chewbacca"))

    ship1.add_weapon(laser)
    ship2.add_weapon(missile)

    fleet = Fleet()
    fleet.add_ship(ship1)
    fleet.add_ship(ship2)

    fleet.attack_all()
    fleet.repair_all()
