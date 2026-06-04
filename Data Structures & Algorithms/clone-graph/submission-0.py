"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        mapOldToNew = {}

        def dfs(root, seen):
            if root not in mapOldToNew:
                mapOldToNew[root] = Node(root.val, [])
            
            seen.add(root)
            newNode = mapOldToNew[root]

            for nei in root.neighbors:
                if nei not in seen:
                    dfs(nei, seen)
                newNode.neighbors.append(mapOldToNew[nei])
            return newNode
        return dfs(node, set())
            



        