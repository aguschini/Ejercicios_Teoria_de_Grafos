# test.py
import pytest
from src.practica1 import lee_grafo

def test_lee_grafo_basico():
    entrada = ['3', 'A', 'B', 'C', 'A B', 'B C', 'C B']
    vertices_esperados = ['A', 'B', 'C']
    aristas_esperadas = [('A', 'B'), ('B', 'C'), ('C', 'B')]
    
    vertices, aristas = lee_grafo(entrada)
    
    assert vertices == vertices_esperados
    assert aristas == aristas_esperadas

def test_lee_grafo_sin_aristas():
    entrada = ['2', 'X', 'Y']
    vertices_esperados = ['X', 'Y']
    aristas_esperadas = []
    
    vertices, aristas = lee_grafo(entrada)
    
    assert vertices == vertices_esperados
    assert aristas == aristas_esperadas

def test_lee_grafo_con_espacios_extra():
    entrada = ['2', 'A', 'B', 'A B', 'B    A']
    vertices_esperados = ['A', 'B']
    aristas_esperadas = [('A', 'B'), ('B', 'A')]
    
    vertices, aristas = lee_grafo(entrada)
    
    assert vertices == vertices_esperados
    assert aristas == aristas_esperadas
    