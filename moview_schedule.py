current_movies = {
    'The Grinch':'11:00am',
    'Iron Man X':'1:00pm',
    'Avengers Age of Norm': '6:00pmn',
    'Crappy Love Story...On Hallmark': '10:00pm',
    'Trump - The Movie':'10:30pm'
}


print("We're showing the following movies:")
for key in current_movies:
    print(key)
    
movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime == None:
    print('Requested movie, ', movie, ', is not playing at this theater!', sep='')
else:
    print( movie, 'is playing at', showtime)
