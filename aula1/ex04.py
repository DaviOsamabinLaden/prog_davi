pares = []

for numero in range(1, 21):
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
print(len(pares))

# Saída:
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# 10