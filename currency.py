import requests

from key import API_KEY

BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['USD', 'CAD', 'EUR', 'BRL', 'JPY']

def convert_currency(base):
    currencies = ','.join(CURRENCIES)
    url = f'{BASE_URL}&base_currency={base}&currencies={currencies}'
    try:
        response = requests.get(url)
        data = response.json()
        return data['data']
    except:
        print('Invalid currency.')
        return None

def main():
    base = input('Base currency: ').upper()
    rate = float(input('Value: '))
    
    data = convert_currency(base)
    del data[base]
    for ticker, value in data.items():
        print(f'{ticker}: {round(rate * value,2)}')

if __name__ == '__main__':
    main()