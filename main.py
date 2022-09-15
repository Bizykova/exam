"""
TODO 1. Очистить и наполнить базу данных данными из класса(данные предоставлены ниже в списках)
TODO 2. Получить данные из БД и записчать их в JSON
Доп. подсказки:
1. База данных прилагается и называется bank.db
2. Классы изменять не нужно
3. Основня структура есть
"""

from MegaClass import Account
from db import *
import json


def main():
    listNames = ["Valera", "Artem", "Kolya", "Petya", "Kostya"]
    listNumbers = ["+7-903-800-00-00", "+7-908-222-80-00", "+79000002121", "89003211234", "89077077070"]
    listEmail = ["test@test.ru", "artem@gmail.com", "kolya@mail.ru", "petya@yandex.ru", "kostya@rambler.ru"]
    listBalance = [1000, 3450, 980, 1250, 398]
    sqlConnect.connect()
    sqlConnect.create_tables([AccountDb])

    account1 = Account('Valera', '+7-900-000-00-00', 'valera@mail.com', 100)
    users = AccountDb.create(account=account1.accountName, phone=str(account1.phone), email=account1.email,
                             balance=account1.balance)
    users.save()
    users = users.select()
    for records in users.tuples().iterator():
        print(records)
        for v in records:
            print(v)

    # Очистить bd
    users = users.select()
    for user in users:
        print('-----------')
        print(user.id)
        print(user.account)
        print('-----------')
        query = AccountDb.delete().where(AccountDb.id == user.id)
        query.execute()

    # наполнить базу данных данными
    index = 0
    for user in listNames:
        print(user)
        print(listNumbers[index], listEmail[index], listBalance[index])
        account = Account(user, listNumbers[index], listEmail[index], listBalance[index])
        users = AccountDb.create(account=account.accountName, phone=str(account.phone), email=account.email,
                                 balance=account.balance)
        users.save()
        index += 1

    # Получить данные из БД
    users = users.select()

    # записать их в JSON
    filePath = './accounts.json'
    data = []
    print('len:', users.__len__())
    for user in users:
        print('!----------')
        print(user.id, user.account, user.phone, user.email, user.balance)
        data.insert(0, {
            "id": user.id,
            "account": user.account,
            "phone": user.phone,
            "email": user.email,
            "balance": user.balance
        })
        print('!----------')

    print(data)
    with open(filePath, 'w') as fp:
        json.dump(data, fp)


if __name__ == '__main__':
    main()
