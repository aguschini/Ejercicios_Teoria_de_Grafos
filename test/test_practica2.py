# test_practica2.py

import pytest
from src.resolucion_practica import (
    cuenta_grado,
    vertice_aislado,
    componentes_conexas,
    es_conexo,
    es_completo,
    aristas_de,
    grafo_inducido,
    grafo_complementario
)

# --- Datos de prueba ---
grafo1 = (['A','B','C'], [('A','B'), ('B','C'), ('C','B')])  # grafo con multiaristas
grafo2 = (['A','B','C','D','E'], [('A','B'), ('B','C'), ('C','B'), ('D','E')])  # todos conectados
grafo3 = (['A','B','C'], [('A','B'), ('A','C'), ('B','C')])  # grafo completo
grafo4 = (['A','B','C','D'], [('A','B'), ('C','D')])  # grafo desconexo
grafo5 = (['A','B','C','D'], [('A','B')])  # grafo con aislados 'C' y 'D'

# --- Tests ---

def test_cuenta_grado():
    assert cuenta_grado(grafo1) == {'A': 1, 'B': 3, 'C': 2}
    assert cuenta_grado(grafo2) == {'A': 1, 'B': 3, 'C': 2, 'D': 1, 'E': 1}
    assert cuenta_grado(grafo3) == {'A': 2, 'B': 2, 'C': 2}
    assert cuenta_grado(grafo5) == {'A': 1, 'B': 1, 'C': 0, 'D': 0}

def test_vertice_aislado():
    assert vertice_aislado(grafo1) == []
    assert vertice_aislado(grafo2) == []
    assert set(vertice_aislado(grafo5)) == {'C','D'}

def test_componentes_conexas():
    comps2 = componentes_conexas(grafo2)
    comps2_sorted = [sorted(c) for c in comps2]
    assert sorted(comps2_sorted) == [['A','B','C'], ['D','E']]

    comps4 = componentes_conexas(grafo4)
    comps4_sorted = [sorted(c) for c in comps4]
    assert sorted(comps4_sorted) == [['A','B'], ['C','D']]

def test_es_conexo():
    assert es_conexo(grafo1) == True
    assert es_conexo(grafo4) == False
    assert es_conexo(grafo5) == False

def test_es_completo():
    assert es_completo(grafo3) == True
    assert es_completo(grafo1) == False
    assert es_completo(grafo2) == False

def test_aristas_de():
    assert set(aristas_de(grafo1, 'A')) == {('A','B')}
    assert set(aristas_de(grafo1, 'B')) == {('A','B'), ('B','C'), ('C','B')}
    assert set(aristas_de(grafo5, 'C')) == set()  # aislado

def test_grafo_inducido():
    subgrafo = grafo_inducido(grafo4, ['A','B','C'])
    assert subgrafo[0] == ['A','B','C']
    assert set(subgrafo[1]) == {('A','B')}

def test_grafo_complementario():
    comp3 = grafo_complementario(grafo3)
    # grafo3 es completo, su complementario debe estar vacío
    assert comp3[0] == ['A','B','C']
    assert comp3[1] == []

    comp1 = grafo_complementario(grafo1)
    # grafo1: [('A','B'),('B','C'),('C','B')] → complementario debe tener ('A','C')
    assert set(comp1[1]) == {('A','C')}

    comp5 = grafo_complementario(grafo5)
    # grafo5: [('A','B')] → complementario debe incluir todos los pares restantes
    assert set(comp5[1]) == {('A','C'), ('A','D'), ('B','C'), ('B','D'), ('C','D')}
