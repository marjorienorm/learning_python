import requests

response = requests.get( 'http://api.open-notify.org/astros.json')
json = response.json()

# print(json)

# Print dictionary of astronauts currently in space
# for person in json['people']:
#    print( person)

# Print name of astronaut currently in space
print('The people currently in space are:')
for person in json['people']:
    print( person['name'], "on the", person['craft'])
