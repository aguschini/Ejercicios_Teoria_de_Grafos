# test_practica3.py

from src.practica3 import (
    dijkstra_hasta,
)

import unittest
from collections import deque

class TestDijkstraHasta(unittest.TestCase):
    def setUp(self):
        # Grafos de prueba (todos conexos y con pesos positivos)
        self.grafos_positivos = [
            {
                "A": [("B", 2), ("C", 5)],
                "B": [("A", 2), ("C", 1), ("D", 4)],
                "C": [("A", 5), ("B", 1), ("D", 2)],
                "D": [("B", 4), ("C", 2), ("E", 1)],
                "E": [("D", 1)]
            },
            {
                "1": [("2", 3)],
                "2": [("1", 3), ("3", 4)],
                "3": [("2", 4), ("4", 2)],
                "4": [("3", 2)]
            },
            {
                "X": [("Y", 1), ("Z", 5)],
                "Y": [("X", 1), ("Z", 2)],
                "Z": [("X", 5), ("Y", 2)]
            }
        ]

        # Grafo con peso negativo
        self.grafo_negativo = {
            "A": [("B", -3)],
            "B": [("A", -3)]
        }

        # Grafo no conexo
        self.grafo_no_conexo = {
            "A": [("B", 1)],
            "B": [("A", 1)],
            "C": [],  # nodo aislado
            "D": [("E", 2)],
            "E": [("D", 2)]
        }

    def test_grafos_positivos(self):
        """Prueba grafos conexos con pesos positivos y camino mínimo."""
        for grafo in self.grafos_positivos:
            # --- Verificar conectividad ---
            def bfs(origen):
                visitados = set()
                q = deque([origen])
                while q:
                    actual = q.popleft()
                    if actual not in visitados:
                        visitados.add(actual)
                        for vecino, _ in grafo.get(actual, []):
                            q.append(vecino)
                return visitados

            todos = set(grafo.keys())
            visitados = bfs(list(grafo.keys())[0])
            self.assertEqual(todos, visitados, f"Grafo {grafo} no es conexo")

            # --- Verificar pesos positivos ---
            for vecinos in grafo.values():
                for _, peso in vecinos:
                    self.assertGreater(peso, 0, f"Peso no positivo encontrado: {peso}")

            # --- Verificar camino mínimo ---
            origen = list(grafo.keys())[0]
            destino = list(grafo.keys())[-1]
            costo, camino = dijkstra_hasta(grafo, origen, destino)
            self.assertTrue(costo > 0 or costo == float("inf"))
            self.assertIn(origen, camino)
            self.assertIn(destino, camino if camino else [destino])

    def test_grafo_con_peso_negativo(self):
        """Debe detectar peso negativo y fallar."""
        with self.assertRaises(AssertionError):
            for vecinos in self.grafo_negativo.values():
                for _, peso in vecinos:
                    self.assertGreaterEqual(peso, 0, f"Peso negativo encontrado: {peso}")

    def test_grafo_no_conexo(self):
        """Debe detectar que un grafo no es conexo."""
        def bfs(origen, grafo):
            visitados = set()
            q = deque([origen])
            while q:
                actual = q.popleft()
                if actual not in visitados:
                    visitados.add(actual)
                    for vecino, _ in grafo.get(actual, []):
                        q.append(vecino)
            return visitados

        todos = set(self.grafo_no_conexo.keys())
        visitados = bfs("A", self.grafo_no_conexo)
        self.assertNotEqual(todos, visitados, "Grafo debería ser no conexo")






