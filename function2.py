x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


x[1][0] = 15
print(x)

students[0]['last_name'] = "Bryant"
print(students)
sports_directory['soccer'][0] = 'Andres'
print( sports_directory['soccer'])

z[0]['y'] = 30
print(z)


def iteratedictionary(someList):
    for aDict in someList:
        print(
            f"first_name - {aDict['first_name']}, last_name - {aDict['last_name']}")

    iteratedictionary(students2)

students2 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
                        
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        a = some_list[i].get(key_name)
        print(a)

iterateDictionary2('first_name', students2)




dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo_list):
    for key in dojo_list:
        list_length = len(dojo_list[key])
        print(list_length, key)
        for i in range (len(dojo_list[key])):
            print(dojo_list[key][i])
printInfo(dojo)
