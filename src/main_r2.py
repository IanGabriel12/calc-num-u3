from sys import argv
from calc_r2 import calcular_r_quadrado

if len(argv) != 3:
    print("Usage: main_r2.py file.csv file2.csv")
    exit(0)

ys = []
gis = []

with open(argv[1], 'r') as file:
    next(file)  
    for line in file:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            ys.append(float(parts[1]))

with open(argv[2], 'r') as file:
    next(file)
    for line in file:
        parts = line.strip().split(',')
        if len(parts) >= 2:
            gis.append(float(parts[1]))

if len(ys) != len(gis):
    print("Erro: os arquivos têm quantidades diferentes de registros.")
    exit(1)

r2 = calcular_r_quadrado(ys, gis)

with open("r2_comparation_paris_agreement/resultsv2/r2_resultado.txt", "a") as out_file:
    out_file.write(f"Coeficiente de Determinacao R2 para o Ajuste Quadratico: {r2:.6f}\n")

