from ast import Break


class Elevador:
   
    def __init__(self ,capacidade, andares,  sair, subir, descer):

        self.num_pessoas=0
        self.andar_inicial = 0
        self.capacidade = capacidade
        self.andares = andares
        self.sair = sair
        self.subir = 0
        self.descer = descer
       
       
    def get_entrar_pessoas(self):

        if self.num_pessoas < self.capacidade:
            self.num_pessoas += 1
               
            print ("Uma pessoa acabou de entrar \n Total de pessoas no elevador ", self.num_pessoas)

        else:
            print ("limite atingido ")

   
    def get_sair_pessoa(self):
        if self.num_pessoas > 0 and self.andar_inicial >0:
            self.num_pessoas -= 1
            print (" \n Uma pessoa acabou de sair \n ")

   
    def get_subir_andar (self):

        if self.andar_inicial >=0 and self.andar_inicial < 3:
            self.andar_inicial +=1
            print ("voce agora esta no andar {} ".format (self.andar_inicial))

        else:
            print ("nao e possivel subir mais um andar ")
               
    def get_descer_andar(self):
           
        if self.andar_inicial > 0 :
            self.andar_inicial -=1
            print  ("voce esta no andar {} " . format (self.andar_inicial))

        else:
            print ("não é possível descer ")

    def set_encerrar(self):
        print ("Você está encerrando o sistema do elevador ")
        Break


capacidade = 5
andares = 3
elevador = Elevador (capacidade, andares, "", "", "")

while True:

    opcao = int (input ("Escolha a opcao desejada: \n 1= entrar \n 2= sair \n 3= descer \n 4= subir \n"))
    if opcao ==1:
        elevador.get_entrar_pessoas()
   
    if opcao == 2:
        elevador.get_sair_pessoa()
   
    if opcao == 3:
        elevador.get_descer_andar()
   
    if opcao == 4:
        elevador.get_subir_andar()

    if opcao == 5 :
        elevador.set_encerrar()
