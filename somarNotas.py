
while True:
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    # Soma as duas notas
    soma = nota1 + nota2

    # Verifica se a soma é menor que 20
    if soma < 20:
        print("A soma das notas é menor que 20. Por favor, tente novamente.\n")
    else:
        # Se a soma for maior ou igual a 20, sai do loop
        
        break

# Exibe o resultado
print("A soma das notas é:", soma)
