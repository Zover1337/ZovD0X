import pandas
import requests

def phone():
    phone = input('Введите номер телефона(РФ): +')

    result = pandas.read_csv('test_compression.csv.xz', low_memory=False)

    df = result[result['phone'] == phone]

    # print(df)

    df1 = str(df['id'])
    df1_i = df1.find('    ')
    print('Telegram ID:',df1[df1_i+4:-24])
    df2 = str(df['phone'])
    df2_i = df2.find('    ')
    print('Телефон:', df2[df2_i+4:-27])
    df3 = str(df['username'])
    df3_i = df3.find('    ')
    print('Telegram UserName:',df3[df3_i+4:-30])
    df4 = str(df['first_name'])
    df4_i = df4.find('    ')
    print('Имя:', df4[df4_i+4:-32])
    df5 = str(df['last_name'])
    df5_i = df5.find('    ')
    print('Фамилия:', df5[df5_i+4:-31])
def ip():
    user_ip = input('Введите IP: ')
    response = requests.get(f"http://ip-api.com/json/{user_ip}?lang=ru")
    if response.status_code == 404:
        print("Oops")
    result = response.json()

    record = []

    for key, value in result.items():
        record.append(value)
        print(f"[{key.title()}]: {value}")

print(''' ZovD0X TEST TOOL FREE
By. Zover, RU TOOL''')
mode = input('1 - пробив по номеру телефона\n2 - пробив по IP\n0 - стоп\nВведи нужную цифру: ')

while mode != '0':
    if mode == '1':
        phone()
    if mode == '2':
        ip()
    mode = input('1 - пробив по номеру телефона:\n2 - пробив по IP\n0 - стоп\nВведи нужную цифру: ')