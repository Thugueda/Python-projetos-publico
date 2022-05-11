import socket
import sys
from termcolor import colored

print(colored('BEM VINDO ', 'green'))
print(colored('PORTSCAN EM PY (1.2)', 'red'))

 

print(colored('''

  ________  _________  __
 /_  __/ / / / ____/ |/ /
  / / / /_/ / / __ |   / 
 / / / __  / /_/ //   |  
/_/ /_/ /_/\____//_/|_|   
                         
                                 
 ''', 'blue'))

print(colored('Feito por APOLO \n USE COM A VONTADE  \n TAMO JUNTO ', 'green'))
print('loading............')

#s = ('bancocn.com')
s = (input('site:  '))
portas = [21, 23, 80, 443, 8080, 5555, 22, 3434, 5454, 5334,
          53, 3333, 66, 1080, 3306, 445, 135, 3303, 26, 502, 8443, 9585, ]

print(colored('RESULTADO:', 'blue'))

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.4)

    codigo = cliente.connect_ex((s, porta))
    if codigo == 0:
        print(porta, "OPEN")
