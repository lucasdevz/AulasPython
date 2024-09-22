def ler_numeros(qtd):
    numeros = []
    for i in range(qtd):
        num = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(num)
    return numeros

def contar_pares_impares(numeros):
    pares = sum(1 for n in numeros if n % 2 == 0)
    impares = sum(1 for n in numeros if n % 2 != 0)
    return pares, impares

def contar_positivos_negativos(numeros):
    positivos = sum(1 for n in numeros if n > 0)
    negativos = sum(1 for n in numeros if n < 0)
    return positivos, negativos

def maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor

def media(numeros):
    return sum(numeros) / len(numeros)

def media_pares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    return sum(pares) / len(pares) if pares else 0

def media_impares(numeros):
    impares = [n for n in numeros if n % 2 != 0]
    return sum(impares) / len(impares) if impares else 0

def main():
    qtd_numeros = 5
    numeros = ler_numeros(qtd_numeros)

    pares, impares = contar_pares_impares(numeros)
    positivos, negativos = contar_positivos_negativos(numeros)
    maior, menor = maior_menor(numeros)
    media_todos = media(numeros)
    media_pares_val = media_pares(numeros)
    media_impares_val = media_impares(numeros)

    print("\nResultados:")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")
    print(f"Quantidade de números positivos: {positivos}")
    print(f"Quantidade de números negativos: {negativos}")
    print(f"Quantidade de números inseridos: {len(numeros)}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Média de números pares: {media_pares_val:.2f}")
    print(f"Média de números ímpares: {media_impares_val:.2f}")
    print(f"Média de todos os números inseridos: {media_todos:.2f}")
    print("Números lidos na ordem inversa:", numeros[::-1])

if __name__ == "__main__":
    main()
