"""person."""
person = {'first_name': 'zhong', 'last_name': 'ling', 'age': '20',
          'city': 'London'}
person_2 = {'frist_name': 'zhong', 'last_name': 'qi', 'age': '25',
             'city': 'China'}
person_3 = {'frist_name': 'wang', 'last_name': 'xin', 'age': '23',
            'city': 'japan'}
people = [person, person_2, person_3]
for person in people:
    print(person)
