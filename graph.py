class Graph:
    def __init__(self):
        """ Represents a graph data structure.

        Attributes:
            graph (Dict[str, List[Tuple[str, float]]]): A dictionary representing
                the graph structure where keys are vertex identifiers and values
                are lists of tuples representing neighboring vertices and edge weights
        """

        self.graph = {}

    def add_edge(self, start, end, cost):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost))
        