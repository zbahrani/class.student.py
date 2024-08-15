from decimal import Decimal


my_leason = input("please enter your leasons:  ")
my_leason = list(my_leason.split(","))
my_degre = input("please enter your degre: ")
my_degre = list(my_degre.split(","))
myDict = dict(zip(my_leason, my_degre))
my_list = list(myDict.values())
size = len(my_list)
avrage = sum(Decimal(i) for i in my_list)/size
avrage = float(avrage)

if len(my_leason)!= len(my_degre) :
   raise Exception("Sorry the entries are incorrect")

class student:
    count = 0
    def __init__(self, name, term, myDict, avrage):
        self.avrage = avrage
        self.myDict = myDict
        self.name = name
        self.term = term
    def get_name(self):
        print("name is %s" % self.name)
    def get_term(self):
        print("term is %i" % self.term)
    def get_avrage(self):
        print("avrage is %f" % self.avrage)
    def get_info(self):
        print("name is %s and term is %i and myDict is %s and avrage is %f"
              % (self.name, self.term,self.myDict, self.avrage))

zeinab = student("zeinab", 9, myDict, avrage)
zeinab.get_name()
zeinab.get_info()
zeinab.get_avrage()

