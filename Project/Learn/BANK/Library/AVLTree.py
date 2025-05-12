from Library.Node import Node
class AVlTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,root,key,parent= None):
        if not root:
            node = Node(key)
            node.parent = parent
            self.size += 1
            if not parent:
                self.root = node
            return node
        else:
            if key.get_id() == root.data.get_id():
                return root
            elif key.get_id() < root.data.get_id():
                root.left = self.insert(root.left,key,root)
            else:
                root.right = self.insert(root.right,key,root)

        balance = self.get_balance(root)
        if balance > 1:  #deviated left
            if key.get_id() < root.left.data.get_id():  #deviated left left
                root = self.rotateright(root)
            elif key.get_id() > root.left.data.get_id():  #deviated left right
                root.left = self.rotateleft(root.left)
                root = self.rotateright(root)
        elif balance < -1:  #deviated right
            if key.get_id() > root.right.data.get_id():  #deviated right right
                root = self.rotateleft(root)
            elif key.get_id() < root.right.data.get_id():  #deviated right left
                root.right = self.rotateright(root.right)
                root = self.rotateleft(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        if key < root.data.get_id():
            root.left = self.delete(root.left, key)
        elif key > root.data.get_id():
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.minvaluenode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data.get_id())

        balance = self.get_balance(root)
        if balance > 1:  # deviated left
            if self.get_balance(root.left) >= 0:  # deviated left left
                root = self.rotateright(root)
            elif self.get_balance(root.left) < 0:  # deviated left right
                root.left = self.rotateleft(root.left)
                root = self.rotateright(root)
        elif balance < -1:  # deviated right
            if self.get_balance(root.right) <= 0:  # deviated right right
                root = self.rotateleft(root)
            elif self.get_balance(root.right) > 0:  # deviated right left
                root.right = self.rotateright(root.right)
                root = self.rotateleft(root)
        return root
    def minvaluenode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def get_balance(self,root):
        if not root:
            return 0
        return self.heigh(root.left) - self.heigh(root.right)

    def heigh(self,root):
        if not root:
            return 0
        return max(self.heigh(root.left), self.heigh(root.right)) + 1

    def rotateleft(self, root):
        temp = root.right
        root.right = temp.left
        if temp.left:
            temp.left.parent = root
        temp.left = root
        temp.parent = root.parent
        root.parent = temp
        if temp.parent is None:
            self.root = temp
        elif temp.parent.left == root:
            temp.parent.left = temp
        else:
            temp.parent.right = temp
        return temp

    def rotateright(self, root):
        temp = root.left
        root.left = temp.right
        if temp.right:
            temp.right.parent = root
        temp.right = root
        temp.parent = root.parent
        root.parent = temp
        if temp.parent is None:
            self.root = temp
        elif temp.parent.left == root:
            temp.parent.left = temp
        else:
            temp.parent.right = temp
        return temp

    def search(self, root, key):
        if root is None or root.data.get_id() == key:
            return root
        if root.data.get_id() < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def InOrder(self, root):
        res = []
        if root:
            res = res + self.InOrder(root.left)
            res.append(root.data)
            res = res + self.InOrder(root.right)
        return res
