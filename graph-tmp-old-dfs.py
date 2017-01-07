# -*- coding: utf-8 -*-


# OLD DFS, IT HAS MANY INCONSITENCIES WITH VertexLog and VisitLog !!!!!

def _dfs_helper(self, vertex,  on_discovery, on_finish, logs, time):    
        """ Private recursive method to perform the depth first search 
            
            Parameters: 
                vertex: the vertex from where to start performing the discovery
                on_discovery: a function that takes as parameters (DiGraph, vertex, logs, time)
                              which is called at every vertex discovery. Can be None.
                on_finish: a function that takes as parameters (DiGraph, vertex, logs, time)
                              which is called after a vertex search has finished. Can be None.
                logs: a dictionary vertex -> VisitLog with the logs of the previous visited nodes
                time: the current discovery time             
            
            Returns: the last timestamp when the search is finished.
        """
        logs[vertex] = VertexLog(vertex, time)
        
        if on_discovery != None:
            on_discovery(self, vertex, logs, time)
        
        for v in self.adj(vertex): 
            if not vertex in logs:
                new_time = self._dfs_helper(vertex, on_discovery, on_finish, logs, time + 1)
        
        logs[vertex].finish_time = new_time
        
        if on_finish != None:
            on_finish(self, vertex, logs, new_time)

        return new_time

    def dfs(self, vertex, on_discovery=None, on_finish=None):
        """ Performs Depth First Search starting from provided vertex  

            Parameters: 
            
                vertex: the vertex from where to start performing the discovery
                       If the vertes does not exist an Exception is raised
                on_discovery: an optional function that takes as parameters (DiGraph, vertex, logs, time)
                              which is called at every vertex discovery. Can be None.
                on_finish: an optional function that takes as parameters (DiGraph, vertex, logs, time)
                              which is called after a vertex search has finished. Can be None.
        
            Returns: the VisitLog
                        
        """
            
        if vertex not in self._edges:
            raise Exception("Couldn't find a vertex : " + str(vertex))
        
        logs = {}
        
        self._dfs_rec(vertex, on_discovery, on_finish, logs, 1)
        
        return logs
        
        
    def circles(self, source):
        """ Returns a map of the verteces, where the keys are the distance from source
            and the values are a list of verteces found a that distance from source                
        """

        if self.is_empty():
            raise Exception("Cannot perform BFS on an empty graph!")
        
        if not source in self.verteces():
            raise Exception("Can't find vertex:" + str(source))
        
        visit = Visit()  
        
        queue = Queue()        
        queue.put(source)

        while not queue.empty():
            vertex = queue.get()
            
            if not visit.is_discovered(vertex):
                # we just discovered the node
                visit.log(vertex).discovery_time = visit.last_time() + 1 
            
                for neighbor in self.adj(source):                    
                    neighbor_log = visit.log(neighbor)
                    if neighbor_log.parent == None:
                        neighbor_log.parent = vertex
                    queue.put(neighbor)                    
        
        return visit              
            
        