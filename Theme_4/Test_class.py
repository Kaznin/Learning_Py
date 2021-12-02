class Company:
    def __init__(self, name, director, structure):
        self.name = name
        self.director = director
        self.structure = structure

    def getInfo(self):
        return f'Компания: {self.structure} {self.name}, Директор: {self.director}'

a = Company('Тензор', 'Уваров С.В.', 'ООО')

print(a.getInfo())