# potencia

a = pow(4,3)
print(a)

# raiz quadrada

b = 81**(1/2)
print(b)

# raiz cubica

c = 127**(1/3)
print(c)

################################

d = 'oi' + 'olá'
print(d)

e = 'oi'*5
print(e)

f = '='*20
print(f)

################################

nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer {nome:20}!')
print(f'Prazer em te conhecer {nome:>20}!')
print(f'Prazer em te conhecer {nome:<20}!')
print(f'Prazer em te conhecer {nome:^20}!')
print(f'Prazer em te conhecer {nome:=^20}!')

################################

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
su = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print(f'A Soma é {s}, \na Subtraçao é {su}, \na Multiplicaçao é {m}, a Divisao é {d:.3f}', end=' >>>')
print(f' a Divisao inteira é {di} e a Potencia é {e}')