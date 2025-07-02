def mtd_simpson_3_8(n, x0, xn, f):
  """
  Calcula a integral aproximada de uma função usando o método de 3/8 de Simpson.

  Args:
    n (int): O número de subintervalos (deve ser múltiplo de 3).
    x0 (float): O limite inferior de integração.
    xn (float): O limite superior de integração.
    f (function): A função a ser integrada.

  Returns:
    float: A área aproximada sob a curva usando o método de 3/8 de Simpson.
  """
  if n % 3 != 0:
    raise ValueError("O número de subintervalos 'n' deve ser múltiplo de 3 para o método de 3/8 de Simpson.")

  h = (xn - x0) / n
  integral = f(x0) + f(xn)

  for i in range(1, n):
    x_i = x0 + i * h
    if i % 3 == 0:
      integral += 2 * f(x_i)  # Termos com índice múltiplo de 3 (exceto as extremidades)
    else:
      integral += 3 * f(x_i)  # Termos com índice não múltiplo de 3

  integral *= (3 * h / 8)
  return integral
