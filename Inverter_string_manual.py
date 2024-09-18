# Solicitando a string do usuário a ser invertida
string = input("Digite a string a ser invertida: ")

# Inverter a string manualmente
string_invertida = ""
for char in string:
    string_invertida = char + string_invertida

print("String original:", string)
print("String invertida:", string_invertida)
