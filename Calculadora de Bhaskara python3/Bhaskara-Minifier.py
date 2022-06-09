L='aperte para reiniciar........'
M='x = – ({}) - √{}\n             2·{}'
N='blue'
O='on_white'
P='clear'
Q='cls'
J='green'
K=int
I='cyan'
F='=-=-'
G=input
A=print
import os as H
H.system('pip install termcolor ')
H.system('pip install time')
H.system(Q)
H.system(P)
from termcolor import colored as C
import time
A(C('Obrigado por testar esse script','red',O))
time.sleep(2)
T=0
while T!=5:
	H.system(Q);H.system(P);A(C('\n      ██████╗ ██╗  ██╗ █████╗ ███████╗██╗  ██╗ █████╗ ██████╗  █████╗\n      ██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗\n      ██████╔╝███████║███████║███████╗█████╔╝ ███████║██████╔╝███████║\n      ██╔══██╗██╔══██║██╔══██║╚════██║██╔═██╗ ██╔══██║██╔══██╗██╔══██║\n      ██████╔╝██║  ██║██║  ██║███████║██║  ██╗██║  ██║██║  ██║██║  ██║\n      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝\n      ',I));A(C('Criado por Thugueda,\nInstagram -> xx_thu.gueda_xx',N,O));A('');D=K(G('Valor de A:   '));E=K(G('Valor de B:   '));R=K(G('Valor de C:   '));A('');B=E**2-4*D*R;A(C('Δ = {}² - 4 x {} x {} = {}'.format(E,D,R,B),N));A(C('Δ = {} '.format(B),I));A(C(F*10,J))
	if B==0:A(C(M.format(E,B,D),I));U=(-E-B**0.5)/(2*D);A('A solução e de  [{:.0f}]'.format(U));A(C(F*10,J));S=G(L)
	if B>0:V=(-E+B**0.5)/(2*D);A(C('x = + ({}) - √{}\n             2·{}'.format(E,B,D),I));A(F*10);W=(-E-B**0.5)/(2*D);A(C(M.format(E,B,D),I));A(F*10);A('Resolução = [{:.0f}/{:.0f}]= '.format(V,W));A(F*10);S=G(L)
	if B<0:A('Delta negativo\nA conta acaba aqui!\nResultado = {:.0f}'.format(B));A(C(F*10,J));S=G('aperte qualquer coisa para dar restart........')