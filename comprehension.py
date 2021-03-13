from pprint import pprint as pp
import os
import glob

country_to_capitals = { 'United Kingdon' : 'London',
                        'Brazil' : 'Brisilia',
                        'Morocco' : 'Rabat',
                        'Sweden' : 'Stockholm'
}


def invert_dictionary():
    capital_to_country = { capital : country for country, capital in country_to_capitals.items()}

    pp(capital_to_country)

def the_last_only():
    words = ['Hi', 'Hello', 'Headlam', 'horn', 'Foxtrot', 'fox', 'Hotel']
    pp({x[0] : x for x in words})
    

def filesize():
    file_sizes = {os.path.realpath(p) : os.stat(p).st_size for p in glob.glob('*.py')}

    pp(file_sizes)



invert_dictionary()
the_last_only()
filesize()