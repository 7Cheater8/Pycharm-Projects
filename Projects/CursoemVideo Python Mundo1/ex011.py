#Faça  um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma are de cm2
altura = float(input('Altura da sua parede?'))
largura = float(input('largura da sua parede?'))
area = altura * largura
print('Sua parede tem a dimensao de {}x{} a sua área é de {}m².'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, voce precisará de {}l de tinta.'.format(tinta))

#nao consegui fazer