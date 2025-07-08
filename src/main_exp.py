from sys import argv
from mmq.exp import exponential_adjustment
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
    
    a, b = exponential_adjustment(points)
    min_x = min(x for x, _ in points)
    max_x = max(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_y = max(y for _, y in points)

    x = np.linspace(min_x, max_x)
    y = b * np.exp(a * x)

    plt.title('Gráfico de teste')
    plt.xlabel('Eixo X (Tempo)')
    plt.ylabel('Eixo Y (Amplitude)')
    plt.grid(True)

    plt.yticks(np.arange(min_y, max_y, 1.0))
    plt.yticks(np.arange(min_y, max_y, 0.1), minor=True)

    plt.grid(which='major', color='gray', linestyle=':', linewidth=1)

    plt.plot([x for x, _ in points], [y for _, y in points], 'x') # Plote os pontos
    plt.plot(x, y) # Plote o ajuste exponencial
    plt.show()