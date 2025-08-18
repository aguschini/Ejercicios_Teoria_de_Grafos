def cuenta_grado(grafo):
    """
    Calcula el grado de cada vértice en un grafo no dirigido.

    Entrada:
        grafo: (vertices, aristas)


    Ejemplo Entrada:
        grafo = (['A','B','C'], [('A','B'), ('B','C'), ('C','B')])

    Ejemplo Retorno:
        {'A': 1, 'B': 3, 'C': 2}
    """
    pass

def vertice_aislado(grafo):
    """
    Devuelve la lista de vértices aislados (sin aristas incidentes).

    Ejemplo Entrada:
        grafo = (['A','B','C','D','E'], [('A','B'), ('B','C'), ('C','B')])

    Ejemplo Retorno:
        ['D','E']
    """
    pass

def componentes_conexas(grafo):
    """
    Obtiene las componentes conexas de un grafo no dirigido.

    Ejemplo Entrada:
        grafo = (['A','B','C','D','E'], [('A','B'), ('B','C'), ('C','B'), ('D','E')])

    Ejemplo Retorno:
        [['A','B','C'], ['D','E']]
    """
    pass

def es_conexo(grafo):
    """
    Devuelve True si el grafo es conexo, False en caso contrario.

    Ejemplo Entrada 1:
        grafo = (['A','B','C'], [('A','B'), ('B','C')])
    Ejemplo Retorno 1:
        True

    Ejemplo Entrada 2:
        grafo = (['A','B','C','D'], [('A','B'), ('C','D')])
    Ejemplo Retorno 2:
        False
    """
    pass
    
def es_completo(grafo):
    """
    Devuelve True si el grafo es completo (grafo no dirigido simple).

    Ejemplo Entrada 1:
        grafo = (['A','B','C'], [('A','B'), ('A','C'), ('B','C')])
    Ejemplo Retorno 1:
        True

    Ejemplo Entrada 2:
        grafo = (['A','B','C'], [('A','B'), ('B','C')])
    Ejemplo Retorno 2:
        False
    """
    pass
    	
def aristas_de(grafo, vertice):
    """
    Devuelve todas las aristas incidentes a un vértice dado.

    Ejemplo Entrada:
        grafo = (['A','B','C'], [('A','B'), ('A','C'), ('B','C')])
        vertice = 'A'

    Ejemplo Retorno:
        [('A','B'), ('A','C')]
    """
    pass


def grafo_inducido(grafo, subconjunto_vertices):
    """
    Devuelve el subgrafo inducido por un subconjunto de vértices.

    Ejemplo Entrada:
        grafo = (['A','B','C','D'], [('A','B'), ('A','C'), ('B','D')])
        subconjunto_vertices = ['A','B','C']

    Ejemplo Retorno:
        (['A','B','C'], [('A','B'), ('A','C')])
    """
    pass

def grafo_complementario(grafo):
    """
    Devuelve el grafo complementario (todos los pares de vértices que no son aristas).

    Ejemplo Entrada:
        grafo = (['A','B','C'], [('A','B'), ('B','C')])

    Ejemplo Retorno:
        (['A','B','C'], [('A','C')])
    """
    pass