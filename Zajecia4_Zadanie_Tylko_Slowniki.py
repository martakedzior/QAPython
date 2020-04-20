import random

# Listy zawierające dane do losowania
gender = ['m', 'f']
female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
surnames = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
countries = ['Poland', 'United Kingdom', 'Germany', 'France', 'Other']

#szkielet zagnieżdzonego słownika
person = {
    1: {
    'firstname': 'Kate',
    'lastname': 'Yu',
    'email': 'kate.yu@example.com',
    'age': 23,
    'country': 'Poland',
    'adult': True
    },
    2: {
    'firstname': 'Random',
    'lastname': 'Random',
    'email': 'Random',
    'age': 23,
    'country': 'Random',
    'adult': True
    },
    3: {
        'firstname': 'Random',
        'lastname': 'Random',
        'email': 'Random',
        'age': 23,
        'country': 'Random',
        'adult': True
    },
    4: {
        'firstname': 'Random',
        'lastname': 'Random',
        'email': 'Random',
        'age': 23,
        'country': 'Random',
        'adult': True
    },
    5: {
        'firstname': 'Random',
        'lastname': 'Random',
        'email': 'Random',
        'age': 23,
        'country': 'Random',
        'adult': True
    },
}

counter = 1

#generujemy dane dla 5 osób
while counter < 6:

    random_gender = random.choice(gender)
    if random_gender == "f":
        random_female_firstname = random.choice(female_fnames)
        person[counter]['firstname'] = random_female_firstname

    else:
        random_male_firstname = random.choice(male_fnames)
        person[counter]['firstname'] = random_male_firstname

    random_surname = random.choice(surnames)
    person[counter]['lastname'] = random_surname

    person[counter]['email'] = person[counter].get('firstname').lower() + '.' + person[counter].get('lastname').lower() + '@example.com'

    random_age = random.randint(5, 45)
    person[counter]['age'] = random_age
    if random_age < 18:
        person[counter]['adult'] = False
    else:
        person[counter]['adult'] = True

    random_country = random.choice(countries)
    person[counter]['country'] = random_country
    print(f"Hi! I\'m {person[counter].get('firstname')} {person[counter].get('lastname')}. I come from {person[counter].get('country')} and I was born in {2020 - person[counter].get('age')}")
    counter = counter + 1






