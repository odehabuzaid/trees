class Node:
    """
    Binary Tree Node 
    """
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
    def __str__(self):
        return '%s' % self.data
