birthdays = {'Trevor':'May 1', 'Eva':'Sep 19', 'John':'Jan 21'}

while True:
    name=input("Enter a name: (blank to quit)")
    if name =='':
        break

    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('I do not have birthday information for '+ name)
        print('What is their birthday?')
        bday=input('Enter birth date: ')
        birthdays[name]=bday
        print('Birthday database updated')