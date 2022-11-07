import requests


response = requests.get('https://udo.derby.ac.uk/campusm/home#menu')


print(response.cookies)