def adcionar_contato(lista):
    contato = {
        "nome" : input("Digite o nome \n"),
        "telefone" : input ("digite o numero telefonico \n"),
        "email" : input ("Digite o e-mail \n")
 
    }
   
    lista.append(contato)
    print ("o contato {} agora pertence a sua agenda ".format(contato['nome']))

def excluir_contato(lista,contato):
    print (" Excluir um contato cadastrado")

    if len(lista) >= 0 :

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

def buscar_contato(lista, contato):

    print (" Buscar um contato cadastrados")
    if len(lista) > 0 :

        nome = input ("Digite o nome do contato ")

        for contato in lista:
           if contato['nome'] == nome :

                print ("Nome: {}". format(contato['nome']))
                print ("Telefone: {}". format(contato['telefone']))
                print ("Email: {}". format(contato['email']))

        print ("numero total de contatos cadastrados = ", len(lista))
    else:
        print ("nao existe contato com este nome na sua agenda ")

def alterar_contato(lista, contato, nome):
    print (" Alterar contatos cadastrados")
    if len (lista) > 0 :
        nome = input ("Digite o nome do contato ")
        for i, contato in enumerate(lista):

            print ("Contato {}: ". format(i+1))
            print ("\tNome: {}". format(contato['nome']))
            print ("\tTelefone: {}". format(contato['telefone']))
            print ("\tEmail: {}". format(contato['email']))

        print ("numero total de contatos cadastrados = ", len(lista))

def mostar_lista(lista):
    print (" Lista de contatos cadastrados")
    if len (lista) > 0 :
        for i, contato in enumerate(lista):

            print ("Contato {}: ". format(i+1))
            print ("\tNome: {}". format(contato['nome']))
            print ("\tTelefone: {}". format(contato['telefone']))
            print ("\tEmail: {}". format(contato['email']))

        print ("numero total de contatos cadastrados = ", len(lista))


def agenda ():
   
    lista = []
    while True:
        print ("\n BEM VINDO(A) A AGENDA TELEFONICA: \n 1 = Adicionar um novo contato\n 2 = excluir um contato ")
        print (" 3 = Buscar um novo contato\n 4= Alterar contato \n 5 = Mostrar lista de contatos\n 6 = Sair da agenda ")
        opcao = int (input (" Digite a opcao desejada: "))

        if opcao == 1:
            adcionar_contato(lista)

        elif opcao == 2:
            excluir_contato(lista, 'contato')

        elif opcao == 3:
            buscar_contato(lista,'contato')

        elif opcao == 4:
            alterar_contato(lista)

        elif opcao == 5:
            mostar_lista(lista)

        elif opcao == 6:
            print ("Saindo da agenda ")
            break

        else :
            print ("ERRO!!! digite uma opcao de 1 - 6")

agenda()
