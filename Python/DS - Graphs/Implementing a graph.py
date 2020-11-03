# Adjacent list implementation
class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacentList = {}

    def addVertex(self,node):
        self.adjacentList[node] = []
        self.number_of_nodes += 1

    def addEdge(self,node1,node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        for key in self.adjacentList:
            print(key,end = '--->')
            for value in self.adjacentList[key]:
                print(value,end = ' ')

my_graph = Graph()
my_graph.addVertex('0')
my_graph.addVertex('1')
my_graph.addVertex('2')
my_graph.addVertex('3')
my_graph.addVertex('4')
my_graph.addVertex('5')
my_graph.addVertex('6')
my_graph.addEdge('3', '1')
my_graph.addEdge('3', '4')
my_graph.addEdge('4', '2')
my_graph.addEdge('4', '5')
my_graph.addEdge('1', '2')
my_graph.addEdge('1', '0')
my_graph.addEdge('0', '2')
my_graph.addEdge('6', '5')
print(my_graph)
print(my_graph.showConnections())