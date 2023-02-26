#Serhii Vysochyn
#1

class User:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        if not '@mail.com' in self.email:
            raise ValueError('Invalid email address')

e = User('serg@mail.com')
print(e.email)

#2


class Boss:
    def __init__(self, id_:int, name:str, company:str):
        self.id_ = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)
            worker.boss = self


class Worker:
    def __init__(self, id_:int, name:str, company:str):
        self.id_ = id_
        self.name = name
        self.company = company
        self.boss = None

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def bos(self, boss):
        if isinstance(boss, Boss):
            self._boss = boss
        else:
            raise TypeError('boss must be an instance of Boss class')


b = Boss(1, "Jon", "Kruba")
w = Worker(2, 'Kum', 'asd')
print(b.workers)