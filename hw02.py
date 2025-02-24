class Artifact:
    
    def __init__ (self, name, age, origin, rarity):
        self.name = name
        self.age = age
        self.origin = origin
        self.rarity = rarity

class ArtifactCollector:

    def __init__ (self):
        self.art_collection = []

    def __iter__(self):
        return CollectorIterator(self.art_collection)

    def __reversed__(self):
        temp = self.art_collection
        return reversed(temp)

    def add_artifact (self, artifact):
        self.art_collection.append (artifact)

    def sort_by_age(self): #сортировка пузырьком
        temp = self.art_collection
        for n in range(len(temp) - 1, 0, -1):
            swapped = False  
            for i in range(n):
                if temp[i].age > temp[i + 1].age:
                    temp[i], temp[i + 1] = temp[i + 1], temp[i]
                    swapped = True
            if not swapped:
                return temp

    def filter_by_origin(self, origin):
        temp = []
        for i in range(len(self.art_collection)):
            if self.art_collection[i].origin == origin:
                temp.append (self.art_collection[i]) 
        return temp

    def filter_by_rarity(self, rarity):
        temp = []
        for i in range(len(self.art_collection)):
            if self.art_collection[i].rarity == rarity:
                temp.append (self.art_collection[i]) 
        return temp

    def find_oldest (self):
        temp = []
        for i in range (len (self.art_collection)):
            temp.append (self.art_collection[i].age)
        temp = max (temp)

        for i in range (len (self.art_collection)):
            if self.art_collection[i].age == temp:
                return self.art_collection[i]

    def find_by_name (self, name):
        for i in range(len(self.art_collection)):
            if self.art_collection[i].name == name:
                return self.art_collection[i]

class CollectorIterator:

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




if __name__ == '__main__':

    mask = Artifact("Golden Mask", 3000, "Egypt", "legendary")
    vase = Artifact("Ancient Vase", 2000, "Greece", "rare")
    statue = Artifact("Stone Statue", 1500, "Aztec", "common")
    amulet = Artifact("Amulet of Anubis", 5000, "Egypt", "legendary")

    collector = ArtifactCollector()
    collector.add_artifact(mask)
    collector.add_artifact(vase)
    collector.add_artifact(statue)
    collector.add_artifact(amulet)

    print("Все артефакты:")
    for artifact in collector:
        print(artifact.name)

    print("\nАртефакты по возрасту:")
    collector.sort_by_age()
    for artifact in collector:
        print(f"{artifact.name}: {artifact.age} лет")
    
    print("\nАртефакты из Египта:")
    for artifact in collector.filter_by_origin("Egypt"):
        print(artifact.name)
    
    print("\nЛегендарные артефакты:")
    for artifact in collector.filter_by_rarity("legendary"):
        print(artifact.name)
    
    oldest = collector.find_oldest()
    print(f"\nСамый древний артефакт: {oldest.name} ({oldest.age} лет)")
    
    artifact = collector.find_by_name("Ancient Vase")
    if artifact:
        print(f"\nАртефакт найден: {artifact.name}, {artifact.age} лет, {artifact.origin}")
    else:
        print("\nАртефакт не найден")
    
    print("\nАртефакты в обратном порядке:")
    for artifact in reversed(collector):
        print(artifact.name)
