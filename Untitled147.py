#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                if node.left is None:
                    node.left = new_node
                    break
                elif node.right is None:
                    node.right = new_node
                    break
                else:
                    queue.append(node.left)
                    queue.append(node.right)
    
    def get_root(self):
        return self.root
    
    def is_empty(self):
        return self.root is None
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            self.preorder_traversal(self.root)
        elif traversal_type == "inorder":
            self.inorder_traversal(self.root)
        elif traversal_type == "postorder":
            self.postorder_traversal(self.root)
        else:
            print("Invalid traversal type.")
    
    def preorder_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)
    
    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")


# Example usage
tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

print("Pre-order traversal:")
tree.print_tree("preorder")
print()

print("In-order traversal:")
tree.print_tree("inorder")
print()

print("Post-order traversal:")
tree.print_tree("postorder")
print()


# In[2]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_height(root):
    if root is None:
        return -1  # Height of an empty tree is -1

    left_height = find_height(root.left)
    right_height = find_height(root.right)

    return max(left_height, right_height) + 1


# Example usage
# Creating a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Finding the height of the tree
height = find_height(root)
print("Height of the tree:", height)


# In[3]:


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder_traversal(root):
    if root is not None:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)


def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")


# Example usage
# Creating a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Performing pre-order traversal
print("Pre-order traversal:")
preorder_traversal(root)
print()

# Performing in-order traversal
print("In-order traversal:")
inorder_traversal(root)
print()

# Performing post-order traversal
print("Post-order traversal:")
postorder_traversal(root)
print()


# In[5]:


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def print_leaves(root):
    if root is None:
        return
    
    if root.left is None and root.right is None:
        print(root.val)
    
    print_leaves(root.left)
    print_leaves(root.right)
    root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Print the leaves
print_leaves(root)


# In[7]:


from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]
        
        if v in self.adj_list:
            self.adj_list[v].append(u)
        else:
            self.adj_list[v] = [u]

    def bfs(self, start):
        visited = set()
        queue = deque()
        
        queue.append(start)
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            
            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dfs(self, start):
        visited = set()
        self._dfs_helper(start, visited)
    
    def _dfs_helper(self, node, visited):
        visited.add(node)
        print(node, end=' ')
        
        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited)
                # Create a graph
graph = Graph()

# Add edges to the graph
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)

# Perform BFS starting from node 0
print("BFS:")
graph.bfs(0)
print()

# Perform DFS starting from node 0
print("DFS:")
graph.dfs(0)
print()


# In[8]:


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    if root is None:
        return 0
    
    if root.left and root.left.left is None and root.left.right is None:
        # If the left child is a leaf node, add its value
        left_sum = root.left.val
    else:
        # Recursively calculate the sum of left leaves in the left subtree
        left_sum = sum_of_left_leaves(root.left)
    
    # Recursively calculate the sum of left leaves in the right subtree
    right_sum = sum_of_left_leaves(root.right)
    
    # Return the total sum
    return left_sum + right_sum
# Create a binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Calculate the sum of left leaves
left_leaves_sum = sum_of_left_leaves(root)
print("Sum of left leaves:", left_leaves_sum)


# In[9]:


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def sum_of_all_nodes(root):
    if root is None:
        return 0
    
    # Calculate the sum of all nodes in the left subtree
    left_sum = sum_of_all_nodes(root.left)
    
    # Calculate the sum of all nodes in the right subtree
    right_sum = sum_of_all_nodes(root.right)
    
    # Return the sum of all nodes in the tree
    return root.val + left_sum + right_sum
# Create a perfect binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Calculate the sum of all nodes
total_sum = sum_of_all_nodes(root)
print("Sum of all nodes:", total_sum)


# In[10]:


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, x):
    if root is None:
        return 0
    
    count = 0

    # Check if the current subtree has a sum equal to x
    if get_subtree_sum(root) == x:
        count += 1
    
    # Recursively count subtrees with sum x in the left and right subtrees
    count += count_subtrees_with_sum(root.left, x)
    count += count_subtrees_with_sum(root.right, x)
    
    return count

def get_subtree_sum(root):
    if root is None:
        return 0
    
    # Recursively calculate the sum of the current subtree
    return root.val + get_subtree_sum(root.left) + get_subtree_sum(root.right)
# Create a binary tree
root = TreeNode(5)
root.left = TreeNode(10)
root.right = TreeNode(15)
root.left.left = TreeNode(20)
root.left.right = TreeNode(25)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

# Define the target sum
target_sum = 45

# Count the number of subtrees with sum equal to target_sum
count = count_subtrees_with_sum(root, target_sum)
print("Number of subtrees with sum", target_sum, ":", count)


# In[11]:


from collections import deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def max_level_sum(root):
    if root is None:
        return 0
    
    queue = deque()
    queue.append(root)
    max_sum = float("-inf")  # Initialize with negative infinity
    
    while queue:
        level_sum = 0
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        max_sum = max(max_sum, level_sum)
    
    return max_sum
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(8)

# Find the maximum level sum
max_sum = max_level_sum(root)
print("Maximum level sum:", max_sum)


# In[12]:


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def print_nodes_at_odd_levels(root):
    if root is None:
        return
    
    print_nodes_at_odd_levels_helper(root, 1)

def print_nodes_at_odd_levels_helper(node, level):
    if node is None:
        return
    
    # Print the node if the level is odd
    if level % 2 == 1:
        print(node.val, end=' ')
    
    # Recursively print nodes at odd levels in the left and right subtrees
    print_nodes_at_odd_levels_helper(node.left, level + 1)
    print_nodes_at_odd_levels_helper(node.right, level + 1)
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Print the nodes at odd levels
print("Nodes at odd levels:")
print_nodes_at_odd_levels(root)
print()


# In[ ]:




