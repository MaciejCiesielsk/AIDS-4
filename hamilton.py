import random

class Hamilton:
    def __init__(self, n, saturation):
        self.n = n
        self.saturation = saturation
        self.graph = self.create_graph()

    def create_graph(self):
        if self.saturation < 0 or self.saturation > 100:
            print("Saturation must be between 0 and 100.")
            return None
        graph = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        cycle = [i for i in range(self.n)]
        cycle.append(0)
        for i in range(self.n):
            graph[cycle[i]][cycle[i+1]] = 1
            graph[cycle[i+1]][cycle[i]] = 1
        
        num_edges = int(self.n * (self.n - 1) * max(min(self.saturation, 100), 0) / 200)
        
        while num_edges > 0:
            u = random.randint(0, self.n-1)
            v = random.randint(0, self.n-1)
            if u != v and graph[u][v] == 0:
                graph[u][v] = 1
                graph[v][u] = 1
                num_edges -= 1
        
        return graph
    

    def print_matrix(self):
        if self.graph is None:
            print("Graph is not generated.")
            return
        print("    " + "  ".join(str(i) for i in range(1, len(self.graph)+1)))  
        print("--+" + "---"*len(self.graph)) 
        for i, row in enumerate(self.graph, start=1):
            print(f"{i} | {'  '.join(str(int(cell)) for cell in row)}")


    def find_eulerian_cycle_util(self, u, visited, cycle):
        for v in range(self.n):
            if self.graph[u][v] and not visited[v]:
                visited[v] = True
                cycle.append(v)
                self.find_eulerian_cycle_util(v, visited, cycle)


    def find_eulerian_cycle(self):
        visited = [False for _ in range(self.n)]
        cycle = []
        self.find_eulerian_cycle_util(0, visited, cycle)
        return cycle
    
    def create_non_hamilton_graph(self):
        graph = [[0 for _ in range(self.n)] for _ in range(self.n)]
        cycle = [i for i in range(self.n)]
        cycle.append(0)
        for i in range(self.n):
            graph[cycle[i]][cycle[i+1]] = 1
            graph[cycle[i+1]][cycle[i]] = 1
        
        num_edges = int(self.n * (self.n - 1) * max(min(self.saturation, 100), 0) / 200)
        
        while num_edges > 0:
            u = random.randint(0, self.n-1)
            v = random.randint(0, self.n-1)
            if u != v and graph[u][v] == 0:
                graph[u][v] = 1
                graph[v][u] = 1
                num_edges -= 1
        
        isolated_vertex = random.randint(0, self.n-1)
        for i in range(self.n):
            graph[isolated_vertex][i] = 0
            graph[i][isolated_vertex] = 0
        
        return graph
    def print_non_hamilton_matrix(self):
        if self.graph is None:
            print("Graph is not generated.")
            return
        print("    " + "  ".join(str(i) for i in range(1, len(self.graph)+1)))  
        print("--+" + "---"*len(self.graph)) 
        for i, row in enumerate(self.graph, start=1):
            print(f"{i} | {'  '.join(str(int(cell)) for cell in row)}")