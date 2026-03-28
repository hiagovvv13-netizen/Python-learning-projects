while True:
    user = input('Username: ').strip().lower()
    password = input('Password: ').strip()
    if user == 'hiago' and password == '12345':
        break
    else:
        print('Username Or Password is incorret')
print('1 - Cláudio')
print('2 - Exit')
choice = input('Select Options: ')
if choice == '1':
    print('Name - Cláudio\nAge - 30 years\nStatus - Wanted')
elif choice == '2':
    print('Closed')
else:
    print('Option Invalid')  
    