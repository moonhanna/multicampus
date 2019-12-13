import requests
from decouple import config

base = 'https://api.telegram.org'
# token = '827961019:AAEXLmziybDKWqo8bY4jqmSpLFZ2VZBvkjc'
# chat_id = '1030133925'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
text = 'hello'
url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
send_message = requests.get(url)

print(send_message)