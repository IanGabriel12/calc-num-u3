from sys import argv
from mmq.quadr import ajuste_quadratico
import matplotlib.pyplot as plt
import numpy as np

if len(argv) != 2:
    print("Usage: main_linear.py file.csv")
    exit(0)

with open(argv[1], 'r') as file:
    points: list[tuple[float, float]] = []
    next(file)
    for line in file:
        x, y = map(float, line.split(','))
        points.append((x, y))
    
    a, b, c = ajuste_quadratico(points)
    min_x = min(x for x, _ in points)
    max_x = max(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_y = max(y for _, y in points)

    x_all = np.linspace(min_x, 2050.9167, 1000)
    y_all = a *(x_all**2) + b*x_all + c

    # with open("tables/tabela_dados_quadratico.csv", "w") as out_file:
    #     out_file.write("x,y,xy,x^4,x^3,x^2,x^2y\n")
    #     for x, y in points:
    #         out_file.write(f"{x:.4f},{y:.2f},{x*y:.4f},{x**4:.4f},{x**3:.4f},{x**2:.4f},{x**2 * y}\n")
    
    with open("r2_comparation/results/parametros_resultado.txt", "a") as out_file:
        out_file.write(f"Parâmetros quadratico a={a:.10f}, b={b:.10f}, c={c:.10f}\n");

    start = 1958.2027
    end = 2025.375
    step = 1/12

    early_decimal_dates = []
    x = start
    while x <= end + 1e-6:  # tolerância para evitar erro de ponto flutuante
        early_decimal_dates.append(round(x, 4))
        x += step

    early_predictions = [a*(x**2) + b*x + c for x in early_decimal_dates]

    with open("r2_comparation/ajuste_1958_2025_quadratico.csv", "w") as out_file:
        out_file.write("decimal_date,adjusted_prediction\n")
        for date, prediction in zip(early_decimal_dates, early_predictions):
            out_file.write(f"{date:.4f},{prediction:.2f}\n")

    future_years = np.arange(2025, 2051, 1)
    future_decimal_dates = [year + month/12 for year in future_years for month in range(12)]
    future_predictions = [a*(x**2) + b*x + c for x in future_decimal_dates]

    #with open("predictions/previsoes_2025_2050_quadratica.csv", "w") as out_file:
        #out_file.write("decimal_date,monthly_prediction\n")
        #for date, prediction in zip(future_decimal_dates, future_predictions):
            #out_file.write(f"{date:.4f},{prediction:.2f}\n")

    plt.figure(figsize=(12, 6))
    plt.title('Ajuste Quadrático das Emissões de CO₂')
    plt.xlabel('Ano')
    plt.ylabel('CO₂ (ppm)')
    plt.grid(True)

    plt.xlim(1950, 2055)
    plt.ylim(300, 500)

    plt.xticks(np.arange(1950, 2051, 10))
    plt.yticks(np.arange(300, 501, 10))

    plt.plot([x for x, _ in points], [y for _, y in points], 'o', markersize=1, label='Dados reais')

    plt.plot(x_all, y_all, 'b-', label='Ajuste Quadrático')

    plt.plot(future_decimal_dates, future_predictions, 'r.', label='Previsões 2025-2050', 
    markersize=3)

    plt.legend(loc='upper left')
    plt.savefig("graphics/ajuste_quadratico.png", dpi=300, bbox_inches='tight')
    plt.show()

