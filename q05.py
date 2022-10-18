paisA = float(input('País A. Informe o número de habitantes: '))
paisB = float(input('País B. Informe o número de habitantes: '))
taxaA = float(input('Informe a taxa de crescimento do país A: '))
taxaAper = taxaA / 100
taxaB = float(input('Informe a taxa de crescimento do país B: '))
taxaBper = taxaB / 100
anos = 0

while not (paisA >= paisB):
    paisA = round(paisA * taxaAper  + paisA)
    paisB = round(paisB * taxaBper + paisB)
    anos = anos + 1

print(f''' A população do país A de {paisA} habitantes 
ultrapassou o pais B de {paisB} habitantes após {anos} anos.
''')