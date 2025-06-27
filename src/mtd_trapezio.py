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
