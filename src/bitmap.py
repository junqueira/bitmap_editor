# !/usr/bin/python
# -*- coding: utf8 -*-
import numpy
import os

def main():
    os.system("date")

if __name__ == '__main__':
    main()

class Bitmap():

    def __init__(self, args=[]):
        self.matriz = []
        self.default_color = "0"
        self.cmd_options = ''
        self.rows = 0
        self.cols = 0

    def __getitem__(self, key):
        return self.list[key]

    def __setitem__(self, key, value):
        self.list[key] = value

    def __len__(self):
        return len(self.list)

    def set_options(self, cmd, cmd_options):
        """
        Comandos
        --------
        I M N
        Cria uma nova matriz MxN. Todos os pixels são brancos (O).

        C
        Limpa a matriz. O tamanho permanece o mesmo. Todos os pixels ficam brancos (O).

        L X Y C
        Colore um pixel de coordenadas (X,Y) na cor C.

        V X Y1 Y2 C
        Desenha um segmento vertical na coluna X nas linhas de Y1 a Y2 (intervalo inclusivo) na cor C.

        H X1 X2 Y C
        Desenha um segmento horizontal na linha Y nas colunas de X1 a X2 (intervalo inclusivo) na cor C.

        K X1 Y1 X2 Y2 C
        Desenha um retangulo de cor C. (X1,Y1) é o canto superior esquerdo e (X2,Y2) o canto inferior direito.

        F X Y C
        Preenche a região com a cor C. A região R é definida da seguinte forma:
        O pixel (X,Y) pertence à região. Outro pixel pertence à região, se e somente se,
        ele tiver a mesma cor que o pixel (X,Y) e tiver pelo menos um lado em comum com
        um pixel pertencente à região.

        S name
        Escreve a imagem em um arquivo de nome name.

        X
        Encerra o programa.

        Considerações
        -------------
        Comandos diferentes de I, C, L, V, H, K, F, S e X devem ser ignorados
        """
        self.cmd_options = cmd_options
        method_name = {'I': 'create_image',
                       'C': 'clear_image',
                       'L': 'color_image_pixel',
                       'V': 'draw_vertical_segment',
                       'H': 'draw_horizontal_segment',
                       'F': 'color_image_region',
                       'S': 'display_image',
                       'X': 'terminate_session'}
        method = getattr(self, method_name.get(cmd.upper()), lambda: "nothing")
        print(method())

    def create_image(self):
        """create image with MxN pixels"""
        try:
            rows = int(self.cmd_options[0])
            cols = int(self.cmd_options[1])
            self.matriz = numpy.zeros((rows, cols))
            return self.matriz
        except IndexError:
            print('list index out of range, create_image sample => I M N')

    def clear_image(self):
        """Clears the table, setting all pixels to white (O)"""
        try:
            rows = int(self.cmd_options[0])
            cols = int(self.cmd_options[1])
            matriz = [[self.default_color for coll in range(cols)] for row in range(rows)]
            return matriz
        except IndexError:
            print('list index out of range, clear_image sample => C')

    def color_image_pixel(self):
        """Colours the pixel (X,Y) with colour C"""
        try:
            pixel_x = int(self.cmd_options[0])
            pixel_y = int(self.cmd_options[1])
            color = self.cmd_options[2]
            self.matriz[pixel_x-1][pixel_y-1] = color
            return self.matriz
        except IndexError:
            print('list index out of range, color_image_pixel sample => L X Y C')

    def draw_vertical_segment(self):
        """vertical segment of colour C in column X between multiple rows Y1.Y2..YN"""
        try:
            pixel_x = int(self.cmd_options[0])
            color = self.cmd_options[-1:]
            pixel_y1s = self.cmd_options[1, len(self.cmd_options)-2]

            for item in pixel_y1s:
                pixel_y = int(item) -1
                self.matriz[pixel_y][pixel_x] = color
        except IndexError:
            print('list index out of range, draw_vertical_segment sample => V X Y1 Y2 C')

    def draw_horizontal_segment(self):
        """horizontal segment of colour C in row Y between multiple columns X1.X2..XN
           self.matriz[3:,:] http://www.python-course.eu/numpy
        """
        try:
            pixel_y = self.cmd_options[len(self.cmd_options)-2]-1
            color = self.cmd_options.last
            pixel_xs = self.cmd_options[0,len(self.cmd_options)-2]

            for item in pixel_xs:
                pixel_x = int(item)-1
                self.matrix[pixel_y][pixel_x] = color
        except IndexError:
            print('list index out of range, draw_vertical_segment sample => H X1 X2 Y C')

    def display_image(self):
        for m in self.matrix:
            print(m.join()) # m.join("\t")

    def terminate_session(self):
        exit
        pass

    def read_file(self):
        with open(desc, 'rb') as ff:
          contents = ff.read().split('\r\n')
          try:
            return self.set_options(contents)
          except:
            pass
          finally:
            ff.close()

    def fill(self, x, y, w, h, color):
        for I in range(w):
            for J in range(h):
                self.put(x+I, y+J, color)

    def display(self):
        for J in range(self.height):
            for I in range(self.width):
                if self.get(i,j) == white:
                    sys.stdout.write(" ")
                else:
                    sys.stdout.write("H")
            print

    def put(self, x,y, color):
        assert type(color) is c_color
        self.pixels[y][x] = color

    def get(self, x,y):
        result = self.pixels[y][x]
        assert type(result) is c_color
        return result
