def calcular_r_quadrado(ys, gis):
  """
  Calcula o coeficiente de determinação R² (R-quadrado).

  Args:
    ys (list ou numpy.ndarray): Uma lista ou array numpy com os valores reais de y.
    gis (list ou numpy.ndarray): Uma lista ou array numpy com os valores previstos de y (g(xi)).

  Returns:
    float: O valor do R-quadrado.
  """
  ys = np.array(ys)
  gis = np.array(gis)

  y_media = np.mean(ys)

  sq_residuo = np.sum((gis - y_media)**2)
  print(sq_residuo)

  sq_total = np.sum((ys - y_media)**2)

  r_quadrado = sq_residuo / sq_total

  return r_quadrado
