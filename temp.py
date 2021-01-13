dic = {}

dic['steps'] = 'Ola, sou o step.'
dic['battery'] = 'Ola, sou o battery.'
dic['heart'] = 'Ola, sou o heart.'

for queue, msg in dic.items():
        print(queue)
        print(' :: ')
        print(queue, msg)
        print('\n')

