contacts = {
    'number':5,
    'students':
    [
        {'name':'Marjorie Headlam', 'age': 56, 'city':'Flower Mound', 'email':"marjorienorm@verizon.net"},
        {'name':'Norman Headlam', 'age': 55,  'city':'Flower Mound', 'email':"norman.headlam@outlook.com"},
        {'name':'Chloe Headlam', 'age': 21,  'city':'Flower Mound', 'email':'chloeheadlam121@gmail.com'},
        {'name':'Harrison Headlam', 'age': 20,  'city':'Flower Mound', 'email':"harryheadlam@verizon.net"},
        {'name':'Camille Headlam', 'age': 16,  'city':'Flower Mound', 'email':"camilleheadlam@hotmail.com"}
    ]
}

for student in contacts['students']:
    print(student["email"])
