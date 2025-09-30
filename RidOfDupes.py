SaiomDict = {'id1':
              {'Name': 'Saiom', 'Age': 11, 'Country': 'India'},
            'id2':
             {'Name': 'Jason', 'Age': 11, 'Country': 'USA'},
             'id3':
             {'Name': 'Charles', 'Age': 11, 'Country': 'UK'},
             'id4':
             {'Name': ' Mendes', 'Age': 11, 'Country': 'Australia'},
            'id5':
            {'Name': 'Saiom', 'Age': 11, 'Country': 'India'},
             }
result = {}

for key in SaiomDict.values():
    if key not in result.values():
        result[len(result) + 1] = key

print(result)