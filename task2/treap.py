from random import randint


class Node:
    def __init__(self, value: int, priority: int):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    def find_node_with_parent(self, value: int):
        parent_node = None
        current_node = self.root

        while current_node is not None:
            if value == current_node.value:
                return current_node, parent_node

            parent_node = current_node

            if value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return None, parent_node
    
    def left_rotate(self, cur_node: Node):
        if cur_node is None or cur_node.right is None:
            return

        right_child = cur_node.right
        cur_node.right = right_child.left
        right_child.left = cur_node

        _, parent_node = self.find_node_with_parent(cur_node.value)

        if parent_node is None:
            self.root = right_child
        elif parent_node.left == cur_node:
            parent_node.left = right_child
        else:
            parent_node.right = right_child


    def right_rotate(self, cur_node: Node):
        if cur_node is None or cur_node.left is None:
            return

        left_child = cur_node.left
        cur_node.left = left_child.right
        left_child.right = cur_node

        _, parent_node = self.find_node_with_parent(cur_node.value)

        if parent_node is None:
            self.root = left_child
        elif parent_node.left == cur_node:
            parent_node.left = left_child
        else:
            parent_node.right = left_child
            

    def insert(self, value: int, priority=None):
        if priority is None:
            priority = randint(0, 100)

        new_node = Node(value, priority)

        if self.root is None:
            self.root = new_node
            return

        found_node, parent_node = self.find_node_with_parent(value)

        if found_node is not None:
            return

        if value < parent_node.value:
            parent_node.left = new_node
            if priority > parent_node.priority:
                self.right_rotate(parent_node)
        else:
            parent_node.right = new_node
            if priority > parent_node.priority:
                self.left_rotate(parent_node)

    def delete(self, value: int):
        node_to_delete, parent_node = self.find_node_with_parent(value)

        if node_to_delete is None:
            return

        while node_to_delete.left is not None or node_to_delete.right is not None:
            if node_to_delete.left is None:
                self.left_rotate(node_to_delete)

            elif node_to_delete.right is None:
                self.right_rotate(node_to_delete)

            elif node_to_delete.left.priority > node_to_delete.right.priority:
                self.right_rotate(node_to_delete)

            else:
                self.left_rotate(node_to_delete)

            node_to_delete, parent_node = self.find_node_with_parent(value)

        if parent_node is None:
            self.root = None
        elif parent_node.left == node_to_delete:
            parent_node.left = None
        else:
            parent_node.right = None

    def find(self, value: int):
        cur_node, _ = self.find_node_with_parent(value)
        return cur_node
    
    def inorder(self):
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            result.append(node.value)
            dfs(node.right)

        dfs(self.root)
        return result
    
    def print_tree(self):
        def dfs(node, level=0, prefix="Root: "):
            if node is None:
                return

            print(" " * (level * 4) + f"{prefix}{node.value} (p={node.priority})")

            if node.left or node.right:
                dfs(node.left, level + 1, "L--- ")
                dfs(node.right, level + 1, "R--- ")

        dfs(self.root)

    

treap = Treap()

treap.insert(5, 10)
treap.insert(3, 20)
treap.insert(8, 5)
treap.insert(2, 15)
treap.insert(4, 7)

treap.print_tree()

print(treap.inorder())  

node = treap.find(3)
if node:
    print(node.value)

node = treap.find(100)
if node:
    print(node.value)

treap.delete(3)
treap.print_tree()