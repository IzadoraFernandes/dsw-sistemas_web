from ast import Break

class Agenda:
    
       
    def get_adcionar_contato(self):
        contato = {
            "nome" : input("Digite o nome \n"),
            "telefone" : input ("digite o numero telefonico \n"),
            "email" : input ("Digite o e-mail \n")
     
        }
        
        lista.append(contato)
        print ("o contato {} agora pertence a sua agenda ".format(contato['nome']))
       

    def get_remover(self):
        print (" Excluir um contato cadastrado")

        if len(lista) >= 0:
   
            nome = input ("Digite o nome do contato ")
   
            for i, contato in enumerate(lista):
                if contato['nome'] == nome :
                    print ("Nome: {}". format(contato['nome']))
                    print ("Telefone: {}". format(contato['telefone']))
                    print ("Email: {}". format(contato['email']))
                    del lista[i]
   
                    print ("o contato foi apagado com sucesso ")
   
                    print ("numero removido")
        else:
            print ("nao existe contato com este nome na sua agenda ")

    def get_buscar_pessoa(self):

        print (" Buscar um contato cadastrados")
        if len(lista) > 0 :
   
            nome = input ("Digite o nome do contato ")
   
            for contato in lista:
               if contato['nome'] == nome :
   
                    print ("Nome: {}". format(contato['nome']))
                    print ("Telefone: {}". format(contato['telefone']))
                    print ("Email: {}". format(contato['email']))
   
                    print ("numero total de contatos cadastrados com este nome = ", len(lista))
        else:
            print ("nao existe contato com este nome na sua agenda ")

    def get_imprimir_agenda(self):
        print (" Lista de contatos cadastrados")
        if len (lista) > 0 :
            for i, contato in enumerate(lista):
   
                print ("Contato {}: ". format(i+1))
                print ("\tNome: {}". format(contato['nome']))
                print ("\tTelefone: {}". format(contato['telefone']))
                print ("\tEmail: {}". format(contato['email']))
   
                print ("numero total de contatos cadastrados = ", len(lista))
   
    def set_sair(self):
        print ("Saindo da agenda ")
        Break

lista = []
agenda = Agenda()

while True:

    opcao = int (input ("\n Escolha a opcao desejada: \n 1= Salvar \n 2= Remover \n 3= Buscar \n 4= Sair \n"))
    if opcao ==1:
        agenda.get_adcionar_contato()
   
    if opcao == 2:
        agenda.get_remover()
   
    if opcao == 3:
        agenda.get_buscar_pessoa()
   
    if opcao == 4:
        agenda.set_sair()
