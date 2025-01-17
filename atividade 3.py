faixa_do_detector =400#400nm
resolucao = '32x32' #resolucao em pixels do microscópio
angulo_incidencia = 30 #em graus
limite_de_resolucao = 0.8173 #μm 
i_max = 1.00 # valor da intensidade no ponto mais alto
i_min = 0.95 #valor da intensidade no ponto mais baixo
modelo_de_microscopio = "LSCM" #Modelo de microscopio confocal
largura_de_banda = 50 #largura de banda do comprimento de onda, em nm
abertura_circular = 50 #μm
faixa_do_diodo = 532 #nm

#1- mensagem inicial
print("Este programa tem o objetivo de receber os dados do usuário para a configuração de um microscópio confocal")

#e
faixa_do_detector2 =input("Insira a faixa do detector")
print("Houve alteração da faixa do detector?",int(faixa_do_detector) != int(faixa_do_detector2))

resolucao2 =input("Insira a resolução")
print("Houve alteração da resolução?",str(resolucao) != str(resolucao2))

limite_de_resolucao2 =input("Insira o limite de resolução")
print("Houve alteração do limite de resolução?",float(limite_de_resolucao) != float(limite_de_resolucao2))

i_max2 =input("Insira o valor da intensidade no ponto mais alto")
print("Houve alteração da intensidade no ponto mais alto?",float(i_max) != float(i_max2))

i_min2 =input("Insira o valor da intensidade no ponto mais baixo")
print("Houve alteração do valor da intensidade no ponto mais baixo?",int(i_min) != int(i_min2))

modelo_de_microscopio2 =input("Insira o modelo do microscópio")
print("Houve alteração do modelo do microscópio?",str(modelo_de_microscopio) != str(modelo_de_microscopio2))

largura_de_banda2 =input("Insira a largura de banda")
print("Houve alteração da largura de banda",float(largura_de_banda) != float(largura_de_banda2))

abertura_circular2 =input("Insira a abertura circular")
print("Houve alteração da abertura circular",int(abertura_circular) != int(abertura_circular2))

faixa_do_diodo2 =input("Insira a faixa do diodo")
print("Houve alteração da faixa do diodo?",float(faixa_do_diodo) != float(faixa_do_diodo2))

angulo_incidencia2 =input("Insira o angulo de incidencia")
print("Houve alteração do angulo de incidencia?",float(angulo_incidencia) != float(angulo_incidencia2))
#f
print("As informações digitadas pelo usuário são:")
print("Faixa do detector:", faixa_do_detector2)
print("A resolução escolhida é:", resolucao2)
print("O angulo de incidencia escolhido é:", angulo_incidencia2)
print("O limite de resolução escolhido é:", limite_de_resolucao2)
print("O valor da intensidade no ponto mais alto é:", i_max2)
print("O valor da intensidade no ponto mais baixo é:", i_min2)
print("O modelo do microscópio escolhido foi:", modelo_de_microscopio2)
print("A largura de banda escolhida é:", largura_de_banda2)
print("A abertura circular escolhida foi:", abertura_circular2)
print("A faixa do diodo escolhida foi:", faixa_do_diodo2)

#g calibração horizontal
primeira_letra = "eeeeeeeeee"
ultima_letra = "llllllllll"

print("Para realizar a calibração horizontal, pressione a primeira letra do seu nome 10 vezes e depois a ultima letra do seu nome 10 vezes")

primeira_letra_2 = input("Pressione a primeira letra do seu nome 10 vezes e depois aperte enter")
print(str(primeira_letra) == str(primeira_letra_2))
ultima_letra2 = input("Pressione a ultima letra do seu nome 10 vezes e depois aperte enter")
print(str(ultima_letra) == str(ultima_letra2))

print("Para realizar a calibração horizontal, pressione a segunda letra do seu nome 10 vezes e depois a penultima letra do seu nome 10 vezes")

segunda_letra = "zzzzzzzzzz"
penultima_letra = "eeeeeeeeee"

segunda_letra2 = input("Pressione a primeira letra do seu nome 10 vezes e depois aperte enter")
print(str(segunda_letra) == str(segunda_letra2))
penultima_letra2 = input("Pressione a ultima letra do seu nome 10 vezes e depois aperte enter")
print(str(penultima_letra) == str(penultima_letra2))

print("Calibração concluída, obrigado!")