def 用戶():
    print('ingresa el numero de usuario que quiere')
    n = int(input())
    usersVowels = []
    usersConsonats = []
    usuario = ['Pedro','Lucas','Aris','Ana','Emana']

    if n == int and n > 0 and n <= 10:
        print('cargando')
        for i in range(len(usuario)):
            for j in range(len(usuario[i])):
                if usuario[i][0] == 'A' or usuario[i][0] == 'E' or usuario[i][0] == 'I' or usuario[i][0] == 'O' or usuario[i][0] == 'U':
                    usersVowels.append(usuario[i])
                else:               
                    usersConsonats.append(usuario[i])
    else:
        return('valor incorrecto')

print(用戶())