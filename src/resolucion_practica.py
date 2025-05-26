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



def componentes_conexas(grafo_lista):
    vertices = grafo_lista[0]
    aristas = grafo_lista[1]

    adyacencia = {v: [] for v in vertices}

    for u, v in aristas:
        adyacencia[u].append(v)
        adyacencia[v].append(u) 
    
    visitados = set()
    componentes = []

    for vertice in vertices:
        if vertice not in visitados:
            componente = []
            pila = [vertice]
            
            while pila:
                v = pila.pop()
                if v not in visitados:
                    visitados.add(v)
                    componente.append(v)
                    for vecino in adyacencia[v]:
                        if vecino not in visitados:
                            pila.append(vecino)
            
            componentes.append(componente)
    
    print(f"{componentes}")
    return componentes
    