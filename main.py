
from faker import Faker
fake = Faker()

# print(dir(fake))
for el in dir(fake):
    if el.startswith('random'):
        print(el)
        if el == "random":
            help(el)