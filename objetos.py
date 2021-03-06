import colores


class Obj:
  def __init__(self, win, x, y, w, h, ty, out, t_expl):
      self.x = x
      self.dir = 0
      self.y = y
      self.w = w
      self.h = h
      self.ty = ty
      self.out = out
      self.win = win
      self.t_expl = t_expl
      self.col = colores.col
      self.mp = [[[0, 0, 0, 1, 0, 0, 0],  # 0 avion
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 0, 1, 0, 1, 1],
                  [1, 0, 0, 1, 0, 0, 1],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 1, 1, 0, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 1, 0]],

                  [[0, 0, 0, 1, 0, 0, 0],  # 1 avion izq
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0, 0],
                  [0, 1, 1, 1, 1, 0, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 1, 0, 1, 1, 1, 0],
                  [0, 0, 0, 1, 0, 1, 0],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 1, 1, 0, 0, 0],
                  [0, 1, 1, 1, 1, 0, 0],
                  [0, 1, 0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0, 1, 0]],

                  [[0, 0, 0, 1, 0, 0, 0],  # 2 avion derecha
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0],
                  [0, 0, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 0, 1, 0],
                  [0, 1, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 1, 0, 0],
                  [0, 0, 1, 1, 1, 1, 0],
                  [0, 1, 1, 1, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0, 0]],

                  [[0, 0, 0, 0, 0, 4, 4, 4],  # 3 heli der 0
                  [0, 0, 0, 4, 4, 4, 0, 0],
                  [0, 0, 0, 0, 0, 4, 0, 0],
                  [0, 0, 0, 0, 5, 5, 5, 0],
                  [5, 0, 0, 5, 5, 5, 5, 5],
                  [6, 6, 6, 6, 6, 6, 6, 6],
                  [6, 6, 6, 6, 6, 6, 6, 6],
                  [5, 0, 0, 0, 5, 5, 5, 0],
                  [0, 0, 0, 0, 0, 5, 0, 0],
                  [0, 0, 0, 0, 5, 5, 5, 0]],

                  [[0, 0, 0, 4, 4, 4, 0, 0],  # 4 heli der 1
                  [0, 0, 0, 0, 0, 4, 4, 4],
                  [0, 0, 0, 0, 0, 4, 0, 0],
                  [0, 0, 0, 0, 5, 5, 5, 0],
                  [5, 0, 0, 5, 5, 5, 5, 5],
                  [6, 6, 6, 6, 6, 6, 6, 6],
                  [6, 6, 6, 6, 6, 6, 6, 6],
                  [5, 0, 0, 0, 5, 5, 5, 0],
                  [0, 0, 0, 0, 0, 5, 0, 0],
                  [0, 0, 0, 0, 5, 5, 5, 0]],


                  [[4, 4, 4, 0, 0, 0, 0, 0],  # 5 heli izq <- 0
                  [0, 0, 4, 4, 4, 0, 0, 0],
                  [0, 0, 4, 0, 0, 0, 0, 0],
                  [0, 5, 5, 5, 0, 0, 0, 0],
                  [5, 5, 5, 5, 5, 0, 0, 5],
                  [6, 6, 6, 6, 6, 6, 6, 6],
                  [6, 6, 6, 6, 6, 6, 6, 6],
                  [0, 5, 5, 5, 0, 0, 0, 5],
                  [0, 0, 5, 0, 0, 0, 0, 0],
                  [0, 5, 5, 5, 0, 0, 0, 0]],

                  [[0, 0, 4, 4, 4, 0, 0, 0],  # 6 heli izq <- 1
                  [4, 4, 4, 0, 0, 0, 0, 0],
                  [0, 0, 4, 0, 0, 0, 0, 0],
                  [0, 5, 5, 5, 0, 0, 0, 0],
                  [5, 5, 5, 5, 5, 0, 0, 5],
                  [6, 6, 6, 6, 6, 6, 6, 6],
                  [6, 6, 6, 6, 6, 6, 6, 6],
                  [0, 5, 5, 5, 0, 0, 0, 5],
                  [0, 0, 5, 0, 0, 0, 0, 0],
                  [0, 5, 5, 5, 0, 0, 0, 0]],

                  [[0, 0, 0, 7, 7, 0, 0, 0, 0],   # 7 barco der ->
                  [0, 0, 0, 7, 7, 0, 0, 0, 0],
                  [0, 0, 7, 7, 7, 0, 0, 0, 0],
                  [0, 7, 7, 7, 7, 7, 0, 0, 0],
                  [8, 8, 8, 8, 8, 8, 8, 8, 8],
                  [8, 8, 8, 8, 8, 8, 8, 8, 0],
                  [9, 9, 9, 9, 9, 9, 9, 0, 0],
                  [0, 9, 9, 9, 9, 9, 9, 0, 0]],

                  [[0, 0, 0, 0, 7, 7, 0, 0, 0],  # 8 barco izq <-
                  [0, 0, 0, 0, 7, 7, 0, 0, 0],
                  [0, 0, 0, 0, 7, 7, 7, 0, 0],
                  [0, 0, 0, 7, 7, 7, 7, 7, 0],
                  [8, 8, 8, 8, 8, 8, 8, 8, 8],
                  [0, 8, 8, 8, 8, 8, 8, 8, 8],
                  [0, 0, 9, 9, 9, 9, 9, 9, 9],
                  [0, 0, 9, 9, 9, 9, 9, 9, 0]],

                  [[0,   0,  0,  0,  0,  0, 22],          # 9 avion izq
                  [0,  22, 22,  0,  0, 22, 22],
                  [21, 21, 21, 21, 21, 21, 21],
                  [21, 21, 21,  0,  0, 21,  0],
                  [0,   0, 21, 21, 21,  0,  0],
                  [0,   0,  0, 21, 21,  0,  0]],

                  [[22,  0,  0,  0,  0,  0,  0],          # 10 avion der
                  [22, 22,  0,  0, 22, 22,  0],
                  [21, 21, 21, 21, 21, 21, 21],
                  [0,  21,  0,  0, 21, 21, 21],
                  [0,   0, 21, 21, 21,  0,  0],
                  [0,   0, 21, 21,  0,  0,  0]],

                  [[0,  12, 12, 12, 12, 12,  0],     # 11 gasolina
                  [12, 12,  0,  0,  0, 12, 12],
                  [12, 12,  0, 12, 12, 12, 12],
                  [12, 12,  0,  0, 12, 12, 12],
                  [12, 12,  0, 12, 12, 12, 12],
                  [12, 12,  0, 12, 12, 12, 12],
                  [13, 13, 13, 13, 13, 13, 13],
                  [13, 13,  0, 13,  0, 13, 13],
                  [13, 13,  0, 13,  0, 13, 13],
                  [13, 13,  0, 13,  0, 13, 13],
                  [13, 13,  0,  0,  0, 13, 13],
                  [13, 13, 13, 13, 13, 13, 13],
                  [12, 12,  0,  0,  0, 12, 12],
                  [12, 12,  0, 12, 12, 12, 12],
                  [12, 12,  0,  0, 12, 12, 12],
                  [12, 12,  0, 12, 12, 12, 12],
                  [12, 12,  0,  0,  0, 12, 12],
                  [12, 12, 12, 12, 12, 12, 12],
                  [13, 13,  0, 13, 13, 13, 13],
                  [13, 13,  0, 13, 13, 13, 13],
                  [13, 13,  0, 13, 13, 13, 13],
                  [13, 13,  0, 13, 13, 13, 13],
                  [13, 13,  0,  0,  0, 13, 13],
                  [13, 13, 13, 13, 13, 13, 13]],

                  [[0, 0, 0, 0, 0, 8, 0, 0],     # 12 explosion 1
                  [0, 0, 0, 8, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 8, 0],
                  [8, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 6, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 0, 4],
                  [0, 4, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 4, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 4, 0],
                  [9, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 9, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 9, 0, 0]],

                  [[0, 0, 15, 0, 0, 0],          # 13 explosion 2
                  [0, 0, 0, 0, 15, 0],
                  [15, 0, 0, 0, 0, 0],
                  [0, 0, 0, 15, 0, 0],
                  [0, 15, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 15],
                  [0, 0, 9, 0, 0, 0],
                  [0, 0, 0, 0, 9, 0]],

                  [[0,   0,  7,  7,  7,  0,  0,  0],          # 13 casa
                  [0,   7,  7,  7,  7,  7,  0,  0],
                  [7,   7,  7,  7,  7,  7,  7,  0],
                  [13, 13, 13, 13, 13, 13, 13,  0],
                  [13,  0, 13,  0, 13,  0, 13,  0],
                  [13,  0, 13,  0, 13,  0, 13,  0],
                  [13, 13, 13, 13, 13, 13, 13,  0],
                  [0,   0,  0,  0,  0,  0,  0,  0],
                  [0,   0,  0,  0,  0, 15,  0,  0],
                  [0,   0,  0,  0,  0, 15,  0,  0],
                  [0,   0,  0,  0, 15, 15, 15,  0],
                  [0,   0,  0, 15, 15, 15, 15, 15],
                  [0,   0,  0,  0, 15, 15, 15,  0],
                  [0,   0,  0,  0,  0, 16,  0,  0],
                  [0,   0,  0,  0,  0, 16,  0, 0]]]

  def mostrar(self):
    obj = self.ty

    if self.t_expl > 20:
        obj = 12
    elif self.t_expl:
        obj = 13

    # segun el tipo de objeto y la posicion donde lo queremos mostras
    # se se van creando peque??os cuadrados del color elegido
    for col in range(len(self.mp[obj][0])):
      for lin in range(len(self.mp[obj])):
        if self.mp[obj][lin][col] and (not self.out or self.t_expl):
          x = self.x + col * int(self.w/len(self.mp[obj][0]))
          y = self.y + lin * int(self.h/len(self.mp[obj]))
          w = int(self.w/len(self.mp[obj][0]))
          h = int(self.h/len(self.mp[obj]))
          self.win.fill(self.col[self.mp[obj][lin][col]], rect=[x, y, w, h])
    
    if self.t_expl:
      self.t_expl -= 1
