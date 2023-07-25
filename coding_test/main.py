# Create a DFS table with dictionary
# Create a transversal of DFS table, this table will record children of each node. Use to modify DFS table
def table_gen(x, dependencies):
    mem = set()
    graph = {}
    reversed_graph = {}

    for each in dependencies:
        if each[0] not in graph:
            graph[each[0]] = []

        if each[1] not in graph:
            graph[each[1]] = []

        graph[each[1]].append(each[0])
        temp = reversed_graph.get(each[0], [])
        temp.append(each[1])
        reversed_graph[each[0]] = temp

    return graph, reversed_graph, len(graph)

#start_v: begining of tree, usually a constant
#graph: modified graph, the size always change
#reversed_graph: reversal of graph, use to support modification of graph
#k: k is the maximum number of tasks can be taken in each process
def iterative_dfs(start_v, graph, reversed_graph, k_remain):
    wait_tasks = 0
    discovered = []
    stack = [start_v]
    while stack and k_remain>0:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            # node v doesn't have value
            if not graph[v]:
                # modify table
                k_remain = k_remain-1
                wait_tasks = wait_tasks+1
                del graph[v]
                if v in reversed_graph:
                    for n in reversed_graph[v]:
                        graph[n].remove(v)

            else:
                for w in graph[v]:
                    stack.append(w)


    return wait_tasks, graph

# x: total number of tasks in the workflow
# k: maximum tasks can be processed at the time
# t: time to finish each process
# dependencies: input the dependencies
# graph: DFS table to follow
# reversed_graph: record reversed relation of the table
# current_tasks: number of free tasks that can be handled at this time
def time_cost(x, k, t, dependencies, graph, reversed_graph,  current_tasks):
    total = 0
    if dependencies:
        start_v = dependencies[-1][-1]
    while x > 0:
        if current_tasks>=k:
            k_remain = 0
        else:
            k_remain = k-current_tasks

        if graph:
            wait_tasks, graph = iterative_dfs(start_v, graph, reversed_graph, k_remain)
            current_tasks = current_tasks + wait_tasks
        # Digest current tasks
        if current_tasks >= k:
            current_tasks = current_tasks - k
            x = x - k
        else:
            x = x- current_tasks
            current_tasks = 0
        total = total + t

    return total




if __name__ == "__main__":
    x = 4
    k = 2
    t = 10
    dependencies = [[2, 1], [3, 1], [1, 4]]
    graph, reversed_graph, size = table_gen(x, dependencies)
    current_task = x-size
    total = time_cost(x, k, t, dependencies, graph, reversed_graph,  current_task)
    print(total)
    print("##################")

    x = 5
    dependencies = [[2, 1], [3, 1], [4,1], [1,5]]
    k = 2
    t = 10
    graph, reversed_graph, size = table_gen(x, dependencies)
    current_task = x - size
    total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
    print(total)

    print("##################")
    x = 11
    dependencies = []
    k = 2
    t = 10
    graph, reversed_graph, size = table_gen(x, dependencies)
    current_task = x - size
    total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
    print(total)

    print("##################")
    x = 4
    dependencies = [[1,2],[1,3],[2,4],[3,4]]
    k = 2
    t = 10
    graph, reversed_graph, size = table_gen(x, dependencies)
    current_task = x - size
    total = time_cost(x, k, t, dependencies, graph, reversed_graph, current_task)
    print(total)


