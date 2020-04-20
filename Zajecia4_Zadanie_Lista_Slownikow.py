import random

# Listy zawierające dane do losowania
gender = ['m', 'f']
female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
surnames = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
countries = ['Poland', 'United Kingdom', 'Germany', 'France', 'Other']

currentyear = 2020

person_list = []

#generujemy dane dla 10 osób, 5 kobiet, 5 mężczyzn
for i in range(1,10):
    if i < 5:
        random_firstname = random.choice(female_fnames)
    else:
        random_firstname = random.choice(male_fnames)

    random_surname = random.choice(surnames)
    random_age = random.randint(5, 45)
    random_country = random.choice(countries)
    email = random_firstname.lower() + "." + random_surname.lower() + "@example.com"

    if random_age < 18:
        adult = False
    else:
        adult = True

    dic = {
        'firstname': random_firstname,
        'lastname': random_surname,
        'email': email,
        'age': random_age,
        'country': random_country,
        'adult': adult
         }

    person_list.append(dic)

    print(f"Hi! I\'m {random_firstname} {random_surname}. I come from {random_country} and I was born in {currentyear - random_age}")