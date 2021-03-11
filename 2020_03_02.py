class Node:#like struct
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.visited = False

    def __lt__(self, node2):
        return True#we do not care about node, we only care about the priority and thats what we are comparing.


import heapq
pq = []
heapq.heappush(pq, (1, Node("TO")))
heapq.heappush(pq, (0, Node("NYC")))
heapq.heappop(pq)

def connect(node1, node2, weight):#connection is a list, and each element is a dictionary
    node1.connections.append({"node": node2, "weight": weight})
    node2.connections.append({"node": node1, "weight": weight})
    #between two nodes, the weight will be the same




def dijsktra_pq(node):
    d = {} #d[node_name] is the length of the shorted path from node to node_name
    pq = [(0, node)]

    while len(pq) > 0: #as long as there is something in pq, we keep moving
        cur_dist, cur_node = heapq.heappop(pq)#pop, remove stuff from the pq
        if cur_node.name in d:
            continue#goes to the next iteration of the while loop
        d[cur_node.name] = cur_dist
        for con in cur_node.connections:#checking its neighbours
            dist = con["weight"] + cur_dist#need to consider the distance in the S
            node = con["node"]
            heapq.heappush(pq, (dist, node))#push, add stuff to the pq. Here we are adding its neighbours
            # we need a comparison operator for python, although the operator does not do anything as we dont care about the Node order
    return d



if __name__ == '__main__':
    TO = Node("TO")#send TO to name
    #TO here is kinda like pointer (the variable)
    NYC = Node("NYC")
    DC = Node("DC")
    CDMX = Node("CDMX")
    SF = Node("SF")
    #L = [Node("TO"), Node("NYC")]
    #L[0].name


    #we have a undirected graph here
    connect(TO, NYC, 3)
    connect(TO, SF, 6)
    connect(TO, CDMX, 7)
    connect(NYC, DC, 2)
    connect(SF, DC, 5)

    print(dijsktra_pq(TO))
#
# def f():
#     pass

    #f.xyz= 5
    #say f.xyz
    #it will show 5
