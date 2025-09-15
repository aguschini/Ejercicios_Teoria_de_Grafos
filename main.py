from src.practica1 import *
from src.practica2 import *

if __name__ == "__main__":
    # Ejemplo de grafo
    grafo_lista = ['5', 'A','B','C','D','E', 'A B', 'B C', 'C B', 'D E']

    # Convertimos a (vertices, aristas)
    vertices, aristas = lee_grafo(grafo_lista)
    grafo = (vertices, aristas)

    print("Vertices:", vertices)
    print("Aristas:", aristas)

    # Grados de cada vértice
    print("\nGrados de los vertices:")
    print(cuenta_grado(grafo))

    # Vértices aislados
    print("\nVertices aislados:")
    print(vertice_aislado(grafo))

    # Componentes conexas
    print("\nComponentes conexas:")
    print(componentes_conexas(grafo))

    # Conectividad
    print("\n¿Es conexo?:", es_conexo(grafo))

    # Completitud
    print("¿Es completo?:", es_completo(grafo))

    # Aristas de un vértice
    print("\nAristas de B:")
    print(aristas_de(grafo, 'B'))

    # Grafo inducido
    subconjunto = ['A','B','C']
    print(f"\nGrafo inducido por {subconjunto}:")
    print(grafo_inducido(grafo, subconjunto))

    # Grafo complementario
    print("\nGrafo complementario:")
    print(grafo_complementario(grafo))

    