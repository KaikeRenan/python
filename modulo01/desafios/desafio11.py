# crie um código que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Digite a largura de sua parede em metros: '))
altura = float(input('Digite a altura de sua parede em metros: '))

area = largura * altura

tinta = area / 2

print(f'A área de sua parede é {area}m²\nE voce ira precisar {tinta}L de tinta para pinta-la')