import requests

resposta = requests.get('https://web.whatsapp.com/')

print(f'status_code:{resposta.status_code}')
print(f'Header: {resposta.headers}')
print()
print(f'Content: {resposta.content}')