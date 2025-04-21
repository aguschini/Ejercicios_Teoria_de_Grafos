def cuenta_grado(grafo_lista):
    salida = {}
    vertices, aristas = grafo_lista

    for vertice in vertices:
        salida[vertice] = 0

    for arista in aristas:
        u, v = arista
        if u in salida:
            salida[u] += 1
        if v in salida:
            salida[v] += 1

    print(f"{salida}")

def vertice_aislado(grafo_lista):
    salida = {}
    vertices, aristas = grafo_lista

    for vertice in vertices:
        salida[vertice] = 0

    for arista in aristas:
        u, v = arista
        if u in salida:
            salida[u] += 1
        if v in salida:
            salida[v] += 1
  
    verticecero = []
    i = 0
    for vertice in vertices:
        if salida[vertice] == 0:         
            verticecero[i] = vertice
            i += 1
            print(f"{verticecero}")