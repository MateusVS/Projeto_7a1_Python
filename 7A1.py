import random	
pct = [] #pacote de figurinhas para abrir
x = 0
album = [] #album de figurinhas
repetidas = []
aux = []
def pacote():
    for _ in range(5):
     pct.append(random.randint(1, 681))
    print (pct)
    y=0
    while y <= 0 or y >= 5:
        print('Deseja colar as figurinhas no album: ')
        print('[1] - Sim')
        print('[2] - Nao')
        y=int(input())
        if y == 1:	
            for a in range (0,5):
                if a in album:
                    repetidas.append(pct[a])
                    print('Figrurinha movida para pilha de repetidas')
                else:
                    album.append(pct[a])
                    album.sort()	
            print('Figrurinhas coladas com sucesso')
            del pct[0:5]
def exibe():
  if album == []:
        print('Seu album ainda esta vazio')
  else:
        print(album)
def verifica():
    ver = int(input('Qual figurinha deseja verificar: '))
    if ver in album:
        print ('A figurinha ja foi colada no album')
    else:
        print ('Voce ainda nao possui essa figurinha')
def cola():
    figura = int(input('Informe qual figurinha deseja colar: '))
    if figura >0 and figura < 682:
        if figura in album:
            repetidas.append(figura)
            print('Figrurinha movida para pilha de repetidas')
        else:
            album.append(figura)
            album.sort()
            print ('Figurinha colada com sucesso')
    else:
    	print('Essa figurinha nao existe')
def troca():
	trocara = int(input('Informe o numero da figurinha que sera trocada: '))
	if trocara in repetidas:
	    nova = int(input('Informe o numero da nova figurinha: '))
	    if nova in album:
	    	print("Essa figurinha tambem e repetida, troque por outra")
	    else:
	    	repetidas.remove(trocara)
	    	album.append(nova)
	    	print("Nova figurinha foi adicionada")
	else:
		print('Voce nao possui essa figurinha na pilha de repetidas')
def repet():
	if repetidas == []:
		print('Voce nao possui figurinhas repetidas')
	else:
		print(repetidas)
def falta():
    h=[]
    for z in range (1,681):
        h.append(z)
        if z in album:
            h.remove(z)
    print (h)
def gera_album():
    arquivo = open("eu_tenho.txt","w")
    aux = str(album)
    arquivo.write(aux)
    arquivo.close()
def gera_repet():
    arquivo = open("repetidas.txt","w")
    aux = str(repetidas)
    arquivo.write(aux)
    arquivo.close()
def gera_falta():
    o=[]
    for t in range(1, 681):
        if not t in album:
            o.append(t)
    arquivo = open("faltam.txt","w")
    aux = str(o)
    arquivo.write(aux)
    arquivo.close()
def pega_album():
    arquivo = open("eu_tenho.txt","r")
    teste = arquivo.readlines()
    x = 0

    while x < len(teste):
        if teste[x] == "\n":
            local = teste.index(teste[x])
            teste.pop(local)
        else:
            teste[x] = teste[x].split(' ')
            x += 1
    arquivo.close()	
    print(teste)
   # album.append(int(aux))
while True:
      print("====ALBUM COPA====")
      print("[01] - Abrir pacote de figurinhas")
      print("[02] - Exibir album")
      print("[03] - Colar figurinha individual")
      print("[04] - Checar se ja possui figurinha")
      print("[05] - Trocar figurinhas repetidas")
      print("[06] - Ver pilha de figurinhas repetidas")
      print("[07] - Verificar quais figurinhas faltam")
      print("[08] - Gerar arquivos contendo figurinhas")
      print("[09] - Gerar arquivos contendo repetidas")
      print("[10] - Gerar arquivos contendo faltantes")    
      print("[00] - Sair")
      x=int(input('Selecione uma das opcoes: '))
      
      if x == 1:
          pacote()
      elif x == 2:
          exibe()
      elif x == 3: 
          cola()
      elif x == 4:
          verifica()
      elif x == 5:
      	  troca()
      elif x == 6:
      	  repet()
      elif x == 7:
      	  falta()
      elif x == 8:
      	  gera_album()
      elif x == 9:
          gera_repet()
      elif x == 10:
          gera_falta()		
      elif x == 11:
      	   pega_album()
      elif x == 0:
          break