class Vault:
    def __init__(self, galleans=0, sickles=0, knuts=0):
        self.galleans = galleans
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"{self.galleans} Galleans, {self.sickles} Sickles, {self.knuts} Knuts"
    def __add__(self, other):
        galleans = self.galleans + other.galleans
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleans, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)        

weasley = Vault(25, 50, 100)
print(weasley)


total = potter + weasley
print(total)