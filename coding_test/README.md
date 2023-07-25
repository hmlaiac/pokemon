# Solution
## 1. table_gen: Transfer dependencies to DFS Graph
## 2. iterative_dfs: Run DFS to find available tasks at the time. However, new added tasks should be less than k
## 3. time_cost: Find the total time cost required to run all workflow
```
        x = 5
        dependencies = [[2,1], [3,1]]
        k = 2
        t = 10
        graph, reversed_graph, size = table_gen(x, dependencies)
        current_task = x - size
        total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
        self.assertEqual(30, total)
```

# Limitations:
## 1. Each workflow should have one dependencies but multple "single task" (task doesen't have parents or children) E.g. x = 11, dependencies = [[1,2]]
## 2. Each dependencies should have 1 top node, which should be marked as 'end point'
```
Invalid Input example
dependencies = [[2,1], [3,1], [1,4], [1,5]] # It has two start nodes 4 and 5 which are not valid input
```