excelente = 0
bom = 0
ruim = 0

for i in range(1,51):
    print(f"\n--entrevistado {i} ---")
    nome = input("digite o nome:")
    idade = int(input("digite a idade:"))

    print("opinião sobre o atendimento:")
    print("1 - Excelente")
    print("2 - bom")
    print("3 - ruim")

    opinião = int(input("digite a opinião:(1,2,3)"))

    if opinião == 1:
        excelente += 1
    elif opinião == 2:
        bom += 1
    elif opinião == 3:
        ruim += 1
    else:
        print("opinião inválida")

print("\n--- resultado da pesquisa ---")
print(f"Total de respostas EXCELENTE: {excelente}")
print(f"Total de respostas BOM: {bom}")
print(f"Total de respostas RUIM: {ruim}")