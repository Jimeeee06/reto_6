from math import acos, asin, degrees, sqrt, isclose

class Point:
    def __init__(self, x=0, y=0):
        #Se valida que las coordenadas sean números para evitar errores en cálculos.
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Las coordenadas del punto deben ser valores numéricos.")
        self.__x = x
        self.__y = y

    def compute_distance(self, point: "Point"):
        #Se valida que el objeto recibido sea de tipo Point para poder operar.
        if not isinstance(point, Point):
            raise TypeError("El método solo puede calcular la distancia con otro objeto Point.")
        delta_x = self.get_x() - point.get_x()
        delta_y = self.get_y() - point.get_y()
        return (delta_x ** 2 + delta_y ** 2) ** 0.5
    
    def get_x(self):
        return self.__x

    def set_x(self, val):
        #Se valida el tipo de dato también en el setter.
        if not isinstance(val, (int, float)):
            raise TypeError("La coordenada x debe ser un valor numérico.")
        self.__x = val

    def get_y(self):
        return self.__y

    def set_y(self, val):
        if not isinstance(val, (int, float)):
            raise TypeError("La coordenada y debe ser un valor numérico.")
        self.__y = val
    
    def __str__(self):
        return f"({self.__x}, {self.__y})"

class Line:
    def __init__(self, length: float = 0, start: Point = None, end: Point = None):
        self.__length = length
        self.__start = start
        self.__end = end
    
    def get_start(self):
        return self.__start

    def set_start(self, p: Point):
        self.__start = p

    def get_end(self):
        return self.__end

    def set_end(self, p: Point):
        self.__end = p
    
    def set_length(self, val: float):
        self.__length = val

    def get_length(self):
        try:
            #Se intenta calcular la longitud
            # pero puede fallar si los puntos no están definidos.
            dx = self.__end.get_x() - self.__start.get_x()
            dy = self.__end.get_y() - self.__start.get_y()
            self.set_length((dx**2 + dy**2)**0.5)
        except AttributeError:
            #Si __start o __end es None, se arroja un error específico.
            raise ValueError("Los puntos de inicio y fin deben estar definidos "
            "para calcular la longitud.")
        return self.__length

#Superclass Shape
class Shape:
    def __init__(self, vertices: list[Point] = None, edges: list[Line] = None,
                 inner_angles: list[float] = None, is_regular: bool = None):
        self.__vertices = vertices
        self.__edges = edges
        self.__inner_angles = inner_angles
        self.__is_regular = is_regular

    def get_vertices(self):
        return self.__vertices

    def set_vertices(self, verts: list[Point]):
        self.__vertices = verts

    def get_edges(self):
        return self.__edges

    def set_edges(self, lines: list[Line]):
        self.__edges = lines

    def get_inner_angles(self):
        return self.__inner_angles

    def set_inner_angles(self, angles: list[float]):
        self.__inner_angles = angles

    def get_is_regular(self):
        return self.__is_regular

    def set_is_regular(self, val: bool):
        self.__is_regular = val

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass

#Derived classes from Shape
class Triangle(Shape):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        #* Un triángulo debe tener exactamente 3 aristas y 3 vértices.
        if len(vertices) != 3 or len(edges) != 3:
            raise ValueError("Un triángulo debe tener 3 vértices y 3 aristas.")
        super().__init__(vertices, edges, inner_angles, is_regular)

    def compute_perimeter(self):
        a, b, c = (edge.get_length() for edge in self.get_edges())
        return a + b + c
        
    def compute_area(self):
        a, b, c = sorted(edge.get_length() for edge in self.get_edges())
        s = self.compute_perimeter() / 2
        try:
            #La fórmula de Herón falla si los lados no pueden formar un triángulo.
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        except ValueError:
            #Se lanza un error más específico si la fórmula falla.
            raise ValueError("Las longitudes de las aristas no forman un triángulo válido.")
        return area

class Rectangle(Shape):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        #Un rectángulo debe tener exactamente 4 aristas y 4 vértices.
        if len(vertices) != 4 or len(edges) != 4:
            raise ValueError("Un rectángulo debe tener 4 vértices y 4 aristas.")
        super().__init__(vertices, edges, inner_angles, is_regular)
        self.set_is_regular(is_regular)

    def compute_area(self):    
        a, b, c, d = sorted(edge.get_length() for edge in self.get_edges())
        return a * d
    
    def compute_perimeter(self):
        a, b, c, d = sorted(edge.get_length() for edge in self.get_edges())
        return a + b + c + d
    
    def compute_inner_angles(self):
        angles = [90, 90, 90, 90]
        self.set_inner_angles(angles)
        return angles
    
    def is_regular(self):
        a, b, c, d = [edge.get_length() for edge in self.get_edges()]
        return a == b == c == d

#Derived classes from Triangle    
class Isosceles(Triangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        self.set_is_regular(False)
        a, b, c = sorted(edge.get_length() for edge in self.get_edges())
        #Se valida que la figura sea un isósceles.
        if not (a == b or b == c):
             raise ValueError("Los lados no forman un triángulo isósceles.")
        if a == b:
            self._base, self._same = c, a
        else: # b == c
            self._base, self._same = a, b

    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        try:
            #El cálculo de acos puede fallar si el valor está fuera de [-1, 1]
            #o si hay división por cero.
            angle_1 = degrees(acos(1-((self._base**2)/(2*self._same**2))))
            angle_2 = angle_3 = (180 - angle_1) / 2
        except (ValueError, ZeroDivisionError):
            #Se maneja el error matemático que ocurriría con lados inválidos.
            raise ValueError("Los lados no forman un triángulo isósceles "
            "válido para calcular los ángulos.")
        angles = [angle_1, angle_2, angle_3]
        self.set_inner_angles(angles)
        return angles

class Equilateral(Triangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        #Se valida que todos los lados sean iguales.
        #Se usa isclose para comparar flotantes.
        sides = [edge.get_length() for edge in self.get_edges()]
        if not (isclose(sides[0], sides[1]) and isclose(sides[1], sides[2])):
            raise ValueError("Los lados de un triángulo equilátero deben ser iguales.")
        self.set_is_regular(True)

    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        angles = [60, 60, 60]
        self.set_inner_angles(angles)
        return angles

class Scalene(Triangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        self.set_is_regular(False)

    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        a, b, c = sorted(edge.get_length() for edge in self.get_edges())
        try:
            # Se manejan errores de dominio en acos() o división por cero.
            angle_1 = degrees(acos((b**2 + c**2 - a**2)/(2 * b * c)))
            angle_2 = degrees(acos((a**2 + c**2 - b**2)/(2 * a * c)))
            angle_3 = 180 - angle_1 - angle_2
        except (ValueError, ZeroDivisionError):
            #Este error ocurre si los lados no pueden formar un triángulo.
            raise ValueError("Los lados no forman un triángulo válido para calcular los ángulos.")
        angles = [angle_1, angle_2, angle_3]
        self.set_inner_angles(angles)
        return angles

class TriRectangle(Triangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        #Se valida que los lados cumplan el teorema de Pitágoras para ser un triángulo rectángulo.
        a, b, c = sorted(edge.get_length() for edge in self.get_edges())
        if not isclose(a**2 + b**2, c**2):
            raise ValueError("Los lados no forman un triángulo rectángulo.")
        self.set_is_regular(False)

    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        a, b, c = sorted(edge.get_length() for edge in self.get_edges())
        try:
            #El cálculo de asin puede fallar si el valor está fuera de [-1, 1]
            #o si hay división por cero.
            angle_1 = 90
            angle_2 = degrees(asin(a / c))
            angle_3 = 180 - angle_1 - angle_2
        except (ValueError, ZeroDivisionError):
            #Esto pasaría si los lados no son de un triángulo rectángulo válido.
            raise ValueError("Error al calcular ángulos para el triángulo rectángulo.")
        angles = sorted([angle_1, angle_2, angle_3])
        self.set_inner_angles(angles)
        return angles

#Derived classes from Rectangle 
class Square(Rectangle):
    def __init__(self, vertices, edges, inner_angles, is_regular):
        super().__init__(vertices, edges, inner_angles, is_regular)
        #Se valida que los 4 lados sean iguales para considerarlo un cuadrado.
        sides = [edge.get_length() for edge in self.get_edges()]
        if not all(isclose(sides[0], s) for s in sides):
            raise ValueError("Los lados de un cuadrado deben ser todos iguales.")
        self.set_is_regular(True)
    
    def compute_area(self):
        return super().compute_area()
    
    def compute_perimeter(self):
        return super().compute_perimeter()
    
    def compute_inner_angles(self):
        super().compute_inner_angles()