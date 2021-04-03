from datetime import datetime, date


def add_member(name, year_of_birth, month_of_birth, day_of_birth, role, journal):

    journal[name] = {
        'date_of_birth': date(year_of_birth, month_of_birth, day_of_birth).strftime('%d.%m.%Y'),
        'role': role
    }
    return journal


def delete_member(name, journal):
    journal.pop(name)
    return journal


def add_concert(city_name, year, month, day, contract_amount, concerts, *spending):
    concerts[city_name] = {
        'date': date(year, month, day).strftime('%d.%m.%Y'),
        'contract_amount': contract_amount,
        'spending': spending
    }
    return concerts


def calculate_concert_spending(*args):
    return sum(args)


def calculate_concert_income(city_name, concerts):
    return concerts[city_name]['contract_amount'] - sum(concerts[city_name]['spending'])


journal = {}
concerts = {}

band = {
    'journal': journal,
    'concerts': concerts
}

add_member('Peter', 2000, 8, 28, 'vocalist', band['journal'])
add_member('Mark', 2000, 8, 28, 'guitarist', band['journal'])
add_member('John', 2000, 8, 28, 'drummer', band['journal'])
print(f'Участники группы:\n{journal}')
add_concert('Bishkek', 2019, 4, 12, 1300, band['concerts'], 100, 200, 300)
add_concert('Almaty', 2018, 12, 23, 1500, band['concerts'], 200, 300, 300)
add_concert('St.Petersburg', 2018, 7, 16, 2000, band['concerts'], 150, 100, 200)
add_concert('Yekaterinburg', 2018, 3, 30, 1800, band['concerts'], 180, 200, 210)
add_concert('Moscow', 2017, 11, 25, 3000, band['concerts'], 200, 300, 340)
print(f"Концерты группы:\n{band['concerts']}")
total_amount = 0
for i in band['concerts']:
    total_amount += calculate_concert_income(i, band['concerts'])
print(f'Общая сумма заработка за концерты: {total_amount}')
