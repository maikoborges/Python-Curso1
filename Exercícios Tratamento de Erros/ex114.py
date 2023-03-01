from urllib import request

try:
    request.urlopen('https://www.uol.com.br/')
except:
    print('\033[31mNão conseguir acessar o site pudim!\033[m')
else:
    print('\033[32mConseguir acessar o site pudim!\033[m')