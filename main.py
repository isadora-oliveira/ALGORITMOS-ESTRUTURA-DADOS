from Lista import Lista
from Veiculo import Veiculo 
from Fabricante import Fabricante 


lista = Lista()
listaFabricantes = []

menu = '''
****    MENU    **** 
1 - Cadastrar Veículo
2 - Excluir Veículo
3 - Listar Veículos
4 - Sair

'''

while True:
    print(menu)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nomeFabricante = input("Informe o nome do Fabricante: ")
        anoFundacaoFab = int(input("Informe o Ano de Fundação do Fabricante: "))
        fabricante = Fabricante(nomeFabricante, anoFundacaoFab)
        listaFabricantes.append(fabricante)

        modeloVeiculo = input("Informe o modelo do veículo: ")
        anoVeiculo = int(input("Informe o ano do Veículo: "))
        veiculo = Veiculo(fabricante, modeloVeiculo, anoVeiculo)

        lista.add(veiculo)    
        print("Veiculo cadastrado com sucesso!!\n")
        continue
    elif opcao == "2":
        lista.excluir()
        continue
    elif opcao == "3":
        lista.imprimir()
        continue
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
        continue

