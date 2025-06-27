def mtd_trapezio (n, x0, xn, ys):
  """
  Calcula a integral aproximada de uma função usando o método do trapézio.
  
  Args:
    n (int): O número de subintervalos.
    x0 (float): O limite inferior de integração.
    xn (float): O limite superior de integração.
    ys (list): Uma lista dos valores da função nos pontos x0, x1, ..., xn.

  Returns:
    float: A área aproximada sob a curva usando o método do trapézio.
  """
  h = (xn - x0)/n
  ys_size = len(ys)
  sum = 0
  # somatório de 1 até n-1
  for i in range(1, ys_size-1):
    sum += ys[i]
  sum = 2 * sum
  sum += ys[0] + ys[ys_size-1]
  at = sum * (h/2)
  return at


def plota_trapezoids_grafico(n, x0, xn, f, ys):
  """
  Plota a função e os trapézios que aproximam a área sob a curva usando o método do trapézio.

  Args:
      n (int): O número de subintervalos (trapézios).
      x0 (float): O limite inferior de integração.
      xn (float): O limite superior de integração.
      f (function): A função a ser integrada.
      ys (list): Uma lista dos valores da função nos pontos x0, x1, ..., xn.

  Returns:
      None: Exibe um gráfico da função e dos trapézios.
  """
  x_values = np.linspace(x0, xn, n + 1)
  x_smooth = np.linspace(x0, xn, 100)
  y_smooth = f(x_smooth)

  plt.figure(figsize=(8, 6))
  plt.plot(x_smooth, y_smooth, label='f(x) = 1/x', color='blue')

  for i in range(n):
    x_trap = [x_values[i], x_values[i+1], x_values[i+1], x_values[i]]
    y_trap = [0, 0, ys[i+1], ys[i]]
    plt.fill(x_trap, y_trap, alpha=0.3, edgecolor='red', linewidth=1)

  plt.scatter(x_values, ys, color='red', zorder=5)
  plt.title(f'Aproximação da integral de 1/x (n={n})')
  plt.xlabel('x')
  plt.ylabel('f(x)')
  plt.legend()
  plt.grid(True)
  plt.show()
