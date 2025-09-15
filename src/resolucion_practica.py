def cuenta_grado(grafo):
    vertices, aristas = grafo
    grados = {v: 0 for v in vertices}
    for v1, v2 in aristas:
        grados[v1] += 1
        grados[v2] += 1
    return grados

def vertice_aislado(grafo):
    vertices, aristas = grafo
    
    # Creamos un conjunto vacío para guardar vértices conectados
    conectados = set()
    
    # Recorremos las aristas y agregamos los vértices que aparecen en ellas
    for origen, destino in aristas:
        conectados.add(origen)
        conectados.add(destino)
    
    # Ahora comparamos con todos los vértices para encontrar los que no están conectados
    aislados = [v for v in vertices if v not in conectados]
    
    return aislados



def vertice_aislado(grafo):
    vertices = set(grafo[0])
    aristas = set()
    for arista in grafo[1]:
        aristas.add(arista[0])
        aristas.add(arista[1])
    
    return list(vertices - aristas)

# src/resolucion_practica.py

def es_conexo(grafo_lista):
    componentes = componentes_conexas(grafo_lista)
    return len(componentes) == 1

def es_completo(grafo):
    vertices, aristas = grafo
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            v1, v2 = vertices[i], vertices[j]
            if not ((v1, v2) in aristas or (v2, v1) in aristas):
                return False
    return True


def aristas_de(grafo, vertice):
    """
    Devuelve una lista de aristas conectadas al vértice especificado.
    El grafo se representa como una tupla (vértices, aristas).
    """
    vertices, aristas = grafo
    return [arista for arista in aristas if vertice in arista]

# src/resolucion_practica.py

def grafo_inducido(grafo, vertices_inducidos):
    """
    Devuelve el subgrafo inducido por el conjunto de vértices especificados.
    El grafo es una tupla (vértices, aristas), y se retorna el subgrafo con los vértices y aristas
    que están en el conjunto de vértices inducidos.
    """
    vertices, aristas = grafo
    vertices_inducidos_set = set(vertices_inducidos)
    
    # Filtrar las aristas que solo conectan vértices en el conjunto de vértices inducidos
    aristas_inducidas = [arista for arista in aristas if arista[0] in vertices_inducidos_set and arista[1] in vertices_inducidos_set]
    
    # Retornar el subgrafo
    return vertices_inducidos, aristas_inducidas

# src/resolucion_practica.py

def grafo_complementario(grafo):
    vertices, aristas = grafo
    complementario = []
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            v1, v2 = vertices[i], vertices[j]
            if not ((v1, v2) in aristas or (v2, v1) in aristas):
                complementario.append((v1, v2))
    return vertices, complementario


def componentes_conexas(grafo_lista):
    vertices, aristas = grafo_lista

    # Creamos el diccionario de adyacencias
    adyacentes = {v: [] for v in vertices}
    for origen, destino in aristas:
        adyacentes[origen].append(destino)
        adyacentes[destino].append(origen)  # no dirigido

    visitados = set()
    componentes = []

    # Función auxiliar para DFS(deep first search busca en grafos)
    def dfs(v, componente):
        visitados.add(v)
        componente.append(v)
        for vecino in adyacentes[v]:
            if vecino not in visitados:
                dfs(vecino, componente)

    # Recorremos todos los vértices
    for v in vertices:
        if v not in visitados:
            componente = []
            dfs(v, componente)
            componentes.append(componente)

    return componentes


def lee_grafo(entrada):
    num_vertices = int(entrada[0])
    vertices = entrada[1:num_vertices + 1]
    aristas = []

    for arista in entrada[num_vertices + 1:]:
        v1, v2 = arista.split()
        aristas.append((v1, v2))
    
    return vertices, aristas



def dijkstra_hasta(grafo, origen, destino):
    dist = {v: float("inf") for v in grafo}
    dist[origen] = 0
    caminos = {v: None for v in grafo}  # Para reconstruir el camino
    visitados = set()

    while len(visitados) < len(grafo):
        u = None
        min_dist = float("inf")
        for v in dist:
            if v not in visitados and dist[v] < min_dist:
                min_dist = dist[v]
                u = v
        
        if u is None:
            break

        if u == destino:
            # Reconstrucción del camino desde el destino al origen
            camino = []
            while u is not None:
                camino.append(u)
                u = caminos[u]
            camino.reverse()  # Invertir para que el camino vaya del origen al destino
            return dist[destino], camino

        visitados.add(u)

        for vecino, peso in grafo[u]:
            if vecino not in visitados:
                nueva_dist = dist[u] + peso
                if nueva_dist < dist[vecino]:
                    dist[vecino] = nueva_dist
                    caminos[vecino] = u

    return None, None  # Si no hay camino, retornamos None
