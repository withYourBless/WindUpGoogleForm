import requests
from random import choice

GoogleURL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLScJEctyVhvUNjLGs11Cc93G4roU3FOqe4XpjZdV4ff82Da2DA'

urlResponse = GoogleURL + '/formResponse'
urlReferer = GoogleURL + '/viewform'

years = ['17', '18', '22', '24']
living = 'Да'
studying = ['БГУ', 'ИГУ', 'Школа', 'Лицей', 'Гимназия']
animals = ['Лев', 'Амурский тигр', 'Бобеир']
century = ['16', '15', '18']
founder = ['Александр 3', 'Ермак', 'Павел 1']
why = 'река'
fire = 1879
buildings = ['Администрация города', 'Мэрия', 'Храм у иерусалимского кладбища']
inform = 'Новости'
project = 'Нет'
Kamov = ['архитетектор', 'художник', 'инженер']

for i in range(3000):
    year = choice(years)
    study = choice(studying)
    animal = choice(animals)
    cent = choice(century)
    found = choice(founder)
    build = choice(buildings)
    kamov = choice(Kamov)

    form_data = {'entry.1979342767': year,
                 'entry.1151631299': living,
                 'entry.193567592': study,
                 'entry.361339768': animal,
                 'entry.1206333946': cent,
                 'entry.271206857': found,
                 'entry.756678854': why,
                 'entry.553637017': fire,
                 'entry.166864368': build,
                 'entry.1250216492': inform,
                 'entry.1940053900': project,
                 'entry.902638155': kamov}

    user_agent = {'Referer': urlReferer,
                  'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15"}
    r = requests.post(urlResponse, data=form_data, headers=user_agent)
    print(r, i)
