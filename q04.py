paisA = float(8e4)
paisB = float(2e5)
taxaA = 0.03
taxaB = 0.015
anos = 0

while not (paisA >= paisB):
    paisA = round(paisA * taxaA + paisA)
    paisB = round(paisB * taxaB + paisB)
    anos = anos + 1

print(f''' A população do país A de {paisA} habitantes 
ultrapassou o pais B de {paisB} habitantes após {anos} anos.
''')

