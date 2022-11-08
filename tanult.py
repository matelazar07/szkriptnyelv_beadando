import random


lastnames = ['Máté','Márton','Marcell', 'János', 'Ádám', 'Ferenc', 'Dániel', 'József', 'Dávid']
firstnames = ['Lázár', 'Lakatos', 'Juhász', 'Kiss', 'Nagy', 'Fekete', 'Somogyi', 'Szalai', 'Végh']
streets = ['Ősz utca', 'Nap utca', 'Hold utca', 'Kedves utca', 'Bátor utca', 'Alma utca', 'Körte utca']
cities = ['Budapest', 'Pécs', 'Dunaújváros', 'Debrecen', 'Szombathely', 'Sárvár', 'Szeged','Békéscsaba']
phonecompany = ['20', '30', '70']



for n in range(10):
    firstname = random.choice(firstnames)
    lastname = random.choice(lastnames)
    street = random.choice(streets)
    city = random.choice(cities)
    phonenumber =f'06-{random.choice(phonecompany)}-{random.randint(1000000,9000000)}'
    streetnumber = random.randint(0,999)
    zipcode = random.randint(1000,9000)
    email = firstname.lower() + lastname.lower() + '@beadandoemail.hu'
    address = f'{zipcode}. {city}. {street}. {streetnumber}'

    print(f'\n{firstname} {lastname}\n{address}\n{phonenumber}\n{email}')