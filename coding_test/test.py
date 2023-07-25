import unittest
from main import *
class TestMainMethods(unittest.TestCase):
    def test_example1(self):
        x = 4
        k = 2
        t = 10
        dependencies = [[2, 1], [3, 1], [1, 4]]
        graph, reversed_graph, size = table_gen(x, dependencies)
        current_task = x - size
        total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
        self.assertEqual(30, total)

    def test_example2(self):
        x = 5
        dependencies = [[2, 1], [3, 1], [4, 1], [1, 5]]
        k = 2
        t = 10
        graph, reversed_graph, size = table_gen(x, dependencies)
        current_task = x - size
        total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
        self.assertEqual(40, total)

    def test_example2(self):
        x = 5
        dependencies = [[2, 1], [3, 1], [4, 1], [1, 5]]
        k = 2
        t = 10
        graph, reversed_graph, size = table_gen(x, dependencies)
        current_task = x - size
        total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
        print(total)

    def test_example3(self):
        x = 11
        dependencies = []
        k = 2
        t = 10
        graph, reversed_graph, size = table_gen(x, dependencies)
        current_task = x - size
        total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
        self.assertEqual(60, total)

    def test_case1(self):
        x = 4
        dependencies = [[1, 2], [1, 3], [2, 4], [3, 4]]
        k = 2
        t = 10
        graph, reversed_graph, size = table_gen(x, dependencies)
        current_task = x - size
        total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
        self.assertEqual(30, total)

    def test_case2(self):
        x = 100
        dependencies = [[1, 2], [1, 3], [2, 4], [3, 4]]
        k = 2
        t = 10
        graph, reversed_graph, size = table_gen(x, dependencies)
        current_task = x - size
        total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
        self.assertEqual(510, total) # 96 free tasks 4 tasks in dependencies = (96/2+3)*10 = 500

    def test_case3(self):
        x = 5
        dependencies = [[2,1], [3,1]]
        k = 2
        t = 10
        graph, reversed_graph, size = table_gen(x, dependencies)
        current_task = x - size
        total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
        self.assertEqual(30, total)

    def test_case4(self):
        x = 10
        dependencies = [[2,1], [3,1], [4,1], [5,1]]
        k = 3
        t = 10
        graph, reversed_graph, size = table_gen(x, dependencies)
        current_task = x - size
        total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
        self.assertEqual(40, total) # e.g. [2,3,4], [5,6,7], [8,9,10], [1]


    def test_graph(self):
        dependencies = [[2, 1], [3, 1], [1, 4]]
        x = 4
        graph, reversed_graph, size = table_gen(x, dependencies)
        print(graph)
        print(reversed_graph)

        self.assertEqual(x, size)

    def test_dfs(self):
        dependencies = [[2, 1], [3, 1], [1, 4]]
        x = 4
        graph, reversed_graph, size = table_gen(x, dependencies)
        wait_tasks, graph = iterative_dfs(4, graph, reversed_graph, 2)
        print(wait_tasks)
        self.assertEqual(wait_tasks, 2)