from sys import argv
from mmq.pot import pow_adjustment
import matplotlib.pyplot as plt
import numpy as np

if len(argv) != 2:
    print("Usage: main_exp.py file.csv")
    exit(0)

with open(argv[1], 'r') as file:
    points: list[tuple[float, float]] = []
    next(file)
    for line in file:
        x, y = map(float, line.split(','))
        points.append((x, y))
    
    a, b = pow_adjustment(points)
    min_x = min(x for x, _ in points)
    max_x = max(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_y = max(y for _, y in points)

    x_all = np.linspace(min_x, 2050.9167, 1000)
    y_all = b * (x_all**a)

    future_years = np.arange(2025, 2051, 1)
    future_decimal_dates = [year + month/12 for year in future_years for month in range(12)]
    future_predictions = [b * (x**a) for x in future_decimal_dates]

    with open("predictions/previsoes_2025_2050_potencial.csv", "w") as out_file:
        out_file.write("decimal_date,monthly_prediction\n")
        for date, prediction in zip(future_decimal_dates, future_predictions):
            out_file.write(f"{date:.4f},{prediction:.2f}\n")

    plt.title('Ajuste Potencial das Emissões de CO₂')
    plt.xlabel('Ano (decimal)')
    plt.ylabel('CO₂ (ppm)')
    plt.grid(True)

    plt.plot([x for x, _ in points], [y for _, y in points], 'o', markersize=0.75, label='Dados reais')

    plt.plot(x_all, y_all, 'b-', label='Ajuste Potencial')

    plt.plot(future_decimal_dates, future_predictions, 'r.', label='Previsões 2025-2050', markersize=3)

    plt.legend()
    plt.savefig("graphics/ajuste_potencial.png", dpi=300, bbox_inches='tight')
    plt.show()