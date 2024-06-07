import random
import math


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

    def find_hamilton_cycle(self):
        visited = [False for _ in range(self.n)]
        path = []
        path.append(0)
        if not self.hamilton_cycle_util(path, visited):
            print("No Hamiltonian cycle exists.")
            return False
        print("Hamiltonian cycle exists:")
        for vertex in path:
            print(vertex, end=" ")
        print(path[0])
        return True
    
    def hamilton_cycle_util(self, path, visited):
        if len(path) == self.n:
            if self.graph[path[-1]][path[0]] == 1:
                return True
            else:
                return False
        for v in range(self.n):
            if self.is_safe(v, path, visited):
                path.append(v)
                visited[v] = True
                if self.hamilton_cycle_util(path, visited):
                    return True
                path.pop()
                visited[v] = False
        return False
    
    def is_safe(self, v, path, visited):
        if self.graph[path[-1]][v] == 0:
            return False
        if visited[v]:
            return False
        return True
    

    def export_to_tikz(self, file_path):
        with open(file_path, "w") as file:
            file.write("\\documentclass{standalone}\n")
            file.write("\\usepackage{tikz}\n")
            file.write("\\begin{document}\n")
            file.write("\\begin{tikzpicture}\n")
            for i in range(len(self.graph)):
                angle = i * (360 / len(self.graph))
                x = 2 * math.cos(math.radians(angle))
                y = 2 * math.sin(math.radians(angle))
                file.write(f"\\node ({i+1}) at ({x},{y}) {{{i+1}}};\n")
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    if self.graph[i][j] == 1:
                        file.write(f"\\draw[->] ({i+1}) -- ({j+1});\n")
            file.write("\\end{tikzpicture}\n")
            file.write("\\end{document}\n")
        print(f"Graph exported to {file_path}")
    
    