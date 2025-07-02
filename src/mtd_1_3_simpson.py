import numpy as np

def mtd_simpson_1_3(n, x0, xn, f):
  """
  Calcula a integral aproximada de uma função usando o método de 1/3 de Simpson.

  Args:
    n (int): O número de subintervalos (deve ser par).
    x0 (float): O limite inferior de integração.
    xn (float): O limite superior de integração.
    f (function): A função a ser integrada.

  Returns:
    float: A área aproximada sob a curva usando o método de 1/3 de Simpson.
  """
  if n % 2 != 0:
    raise ValueError("O número de subintervalos 'n' deve ser par para o método de 1/3 de Simpson.")

  h = (xn - x0) / n
  integral = f(x0) + f(xn)

  for i in range(1, n):
    x_i = x0 + i * h # outra maneira de calcular sem precisar passar todos os valores de x
    if i % 2 == 0:
      integral += 2 * f(x_i)  # Termos com índice par (exceto as extremidades)
    else:
      integral += 4 * f(x_i)  # Termos com índice ímpar

  integral *= (h / 3)
  return integral
