class Node:
    def __init__(self, value):
        self.value = value
        self.next = []

class Tree:
    def __init__(self):
        self.head = None
        self.mem = {}
    def insert(self, tasks):
        prev = tasks[0]
        next = tasks[1]
        if self.head == None:
            self.head = self.__createNode(next)
            new_node = self.__createNode(prev)
            self.head.next.append(new_node)
        else:
            # shifting head & add a Node
            if next not in self.mem:
                new_node = self.__createNode(next)
                new_node.next.append(self.head)
                self.head = new_node

            if prev not in self.mem:
                new_node = self.__createNode(prev)
                temp = self.mem[next].next.append(new_node)


    def __createNode(self, value):
        node = Node(value)
        self.mem[value] = node
        print(value)
        return node



def tree(dependencies):
    mem = {}
    size = len(dependencies)
    for each in dependencies:
        new_node = Node(each[0])

        if each[1] in mem:
            # select the node from previous mem
            node = mem[each[1]]
        else:
            # create a new node for holding data
            Node(each[1])
            mem.add(each[1])
    head = Node(dependencies[-1][1])


# def func(x, dependencies, k, t):
#     #total time computed in task
#     total = 0
#
#     # free_tasks: any tasks are not listed in tree
#     free_tasks = x-len(dependencies)
#     total = (free_tasks//k)
#     # print(total)
arr = []
def recur(head):
  if not head.next:
      return
  else:
      total = 0
      print("head is:",head.value)
      arr = []
      for each in head.next:
        total = total+1
        print(each.value)
        arr.append(each.value)
        recur(each)





      # print("current node is", head.value, " total is", total)
      # total = total+1


if __name__ == "__main__":
    #Test Tree
    tree = Tree()

    x = 6
    dependencies = [[6,2], [2,1], [3,1], [4,1], [1,5]]
    k = 2
    t = 10
    for each in dependencies:
        tree.insert(each)

    recur(tree.head)

    x = 11
    dependencies = []
    k = 2
    t = 10

    # func(x, dependencies, k, t)