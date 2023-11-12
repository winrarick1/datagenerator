# created by winrarick1

import random

print('! THIS PROGRAM GENERATES RANDOM AND FAKE DATA !\n')

if __name__ == '__main__':
    mac_values = ['ee', 'd2', '0d', 'f4', '23', 'df', 'ed', '99', '1f', 'b7', 'b8', 'a1', '1a', '6a', '34']
    names = ['Pavel Batrudinov', 'Matvey Dunaev', 'Yaroslav Rogov', 'Maria Kolesnikova', 'Adelina Chubina', 'Liliya Muhametshina', 'Miron Bondarenko', 'Svetlana Romanishina']
    mac = None
    ip = ""
    email_names = ['veganboy31', 'qwertjohn321', 'ethanduck', 'lovemetoo1209', 'domashniy12345', 'noothingg09']
    email_services = ['gmail.com', 'mail.ru', 'proton.me', 'vk.com', 'github.com']
    operators = ['Tele2', 'Beeline', 'MTS', 'MegaPhone', 'Letai', 'Yota', 'SberMobile', 'TinkoffMobile', 'WiFire', 'Rostelekom', 'SkyLink']
    city = ['Kazan', 'EKB', 'Saint_Petersburg', 'Moscow', 'Vladimir', 'Rostov', 'Petergof']

while True:
    print("'Start' or 'Exit':", end=" ")
    question = input()
    if question == 'Start' or question == 'start':
        ip = f'{random.randint(100, 300)}.{random.randint(100, 300)}.0.{random.randint(0, 9)}'
        mac = ""
        for i in range(8):
            if i < 7:
                mac = f"{mac}{mac_values[random.randint(0, len(mac_values)-1)]}:"
            else:
                mac = f"{mac}{mac_values[random.randint(0, len(mac_values)-1)]}"
        print(f"""
IPv4: {ip}
MAC: {mac}
City: {city[random.randint(0, len(city) - 1)]}
Email: {email_names[random.randint(0, len(email_names) - 1)]}@{email_services[random.randint(0, len(email_services) - 1)]}
Number: +7960{random.randint(1000000, 9999999)}
Operator: {operators[random.randint(0, len(operators) - 1)]}
Age: {random.randint(7, 53)}
Name: {names[random.randint(0, len(names)-1)]}
              """)
    elif question == "exit" or question == "Exit":
        break
    else:
        pass
