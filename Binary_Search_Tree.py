import unittest


class binary_search_tree:
    def __init__(self, init=None):
        self.__value = self.__left = self.__right = None

        if init:
            for i in init:
                self.add(i)

    def __iter__(self):
        if self.__left:
            for node in self.__left:
                yield (node)

        yield (self.__value)

        if self.__right:
            for node in self.__right:
                yield (node)

    def __str__(self):
        return (','.join(str(node) for node in self))

    def add(self, value):
        if self.__left is self.__value is self.__right is None:
            self.__value = value
            return

        if value < self.__value:
            if not self.__left:
                self.__left = binary_search_tree([value])

            else:
                self.__left.add(value)

        elif value > self.__value:
            if not self.__right:
                self.__right = binary_search_tree([value])

            else:
                self.__right.add(value)

    def preorder(self):
        result = [self.__value]

        if self.__left:
            result += self.__left.preorder()

        if self.__right:
            result += self.__right.preorder()

        return result

    def inorder(self):
        result = []

        if self.__left:
            result += self.__left.inorder()

        result += [self.__value]

        if self.__right:
            result += self.__right.inorder()

        return result

    def postorder(self):
        result = []

        if self.__left:
            result += self.__left.postorder()

        if self.__right:
            result += self.__right.postorder()

        result += [self.__value]

        return result

    def BFS(self):
        # create a queue with the root element, and an empty list
        # while there are nodes in the queue
        # grab the first one and add it to the result list
        # if there is a node to the left, add that to the queue
        # if there is a node to the right, add that to the queue
        if self.__value is None:
            return [self.__value]

        queue = [self.__value]
        result = []

        while queue:
            queue += self.find_children(queue[0])

            result += [queue.pop(0)]

        return result

    def display_children(self, value):
        if not self.contained_in_tree(value):
            return "NUMBER NOT FOUND IN TREE"

        if self.find_children(value):
            return self.find_children(value)
        else:
            return "HAS NO CHILDREN"

    def find_children(self, value):
        if self.__value == value:
            result = []

            if self.__left:
                result += [self.__left.__value]

            if self.__right:
                result += [self.__right.__value]

            return result

        if value < self.__value:
            return self.__left.find_children(value)

        elif value > self.__value:
            return self.__right.find_children(value)

    def contained_in_tree(self, value):
        for item in self:
            if item == value:
                return True

        return False

    def delete(self, value):
        if not self.contained_in_tree(value):
            return "NUMBER NOT FOUND IN TREE"

        if self.__value == value:
            if not self.__left and not self.__right:
                self.__value = None

            else:
                replace_value = self.find_replace_value(self)
                self.restructure(replace_value)
                self.__value = replace_value

            return

        delete_this_node = self.find_node(value)
        replace_value = self.find_replace_value(delete_this_node)

        self.restructure(replace_value)
        delete_this_node.__value = replace_value

    def find_node(self, value):
        if value == self.__value:
            return self

        if value < self.__value:
            if value == self.__left.__value:
                return self.__left

            return self.__left.find_node(value)

        if value > self.__value:
            if value == self.__right.__value:
                return self.__right

            return self.__right.find_node(value)

    def find_replace_value(self, node):
        if node.__left:
            node = node.__left

            while node.__right:
                node = node.__right

            return node.__value

        elif node.__right:
            node = node.__right

            while node.__left:
                node = node.__left

            return node.__value

        return node.__value

    def restructure(self, value):
        if value < self.__value:
            if value == self.__left.__value:
                if self.__left.__right:
                    self.__left = self.__left.__right
                else:
                    self.__left = None

            else:
                self.__left.restructure(value)

        if value > self.__value:
            if value == self.__right.__value:
                if self.__right.__left:
                    self.__right = self.__right.__left
                else:
                    self.__right = None

            else:
                self.__right.restructure(value)


class test_binary_search_tree(unittest.TestCase):
    '''
           20
          /  \
        10   30
            /  \
           25  35
    '''

    # C level
    def test_empty(self):
        self.assertEqual(str(binary_search_tree()), 'None')

    def test_one(self):
        self.assertEqual(str(binary_search_tree([1])), '1')

    def test_add(self):
        bt = binary_search_tree()
        bt.add(20)
        bt.add(10)
        bt.add(30)
        bt.add(25)

        bt.add(35)
        self.assertEqual(str(bt), '10,20,25,30,35')

    def test_init(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(str(bt), '10,20,25,30,35')

    # B level

    def test_empty_inorder(self):
        self.assertEqual(binary_search_tree().inorder(), [None])

    def test_inorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.inorder(), [10, 20, 25, 30, 35])

    def test_preorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(list(bt.preorder()), [20, 10, 30, 25, 35])

    def test_postorder(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.postorder(), [10, 25, 35, 30, 20])

    # A level
    def test_empty_BFS(self):
        self.assertEqual(binary_search_tree().BFS(), [None])

    def test_BFS(self):
        bt = binary_search_tree([20, 10, 30, 25, 35, 15, 5])
        self.assertEqual(bt.BFS(), [20, 10, 30, 5, 15, 25, 35])

    # EXTRA CREDIT
    def test_children(self):
        bt = binary_search_tree([50, 25, 75, 10, 30, 60, 100, 80])
        self.assertEqual(bt.display_children(25), [10, 30])
        self.assertEqual(bt.display_children(75), [60, 100])
        self.assertEqual(bt.display_children(100), [80])
        self.assertEqual(bt.display_children(30), "HAS NO CHILDREN")
        self.assertEqual(bt.display_children(60), "HAS NO CHILDREN")
        self.assertEqual(bt.display_children(1), "NUMBER NOT FOUND IN TREE")

    def test_delete(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])

        # LEAVES
        self.assertEqual(str(bt), "10,20,25,30,35")
        self.assertEqual(bt.inorder(), [10, 20, 25, 30, 35])

        bt.delete(10)
        self.assertEqual(bt.inorder(), [20, 25, 30, 35])
        bt.delete(25)
        self.assertEqual(bt.inorder(), [20, 30, 35])
        bt.delete(35)
        self.assertEqual(bt.inorder(), [20, 30])
        bt.delete(30)
        self.assertEqual(bt.inorder(), [20])

        # ROOT
        bt = binary_search_tree([20, 10, 30, 25, 35])
        bt.delete(20)
        self.assertEqual(bt.inorder(), [10, 25, 30, 35])

        # BRANCH
        bt = binary_search_tree([30, 15, 45, 10, 20, 40, 50])
        self.assertEqual(str(bt), "10,15,20,30,40,45,50")
        self.assertEqual(bt.inorder(), [10, 15, 20, 30, 40, 45, 50])

        bt.delete(15)
        self.assertEqual(bt.inorder(), [10, 20, 30, 40, 45, 50])
        bt.delete(45)
        self.assertEqual(bt.inorder(), [10, 20, 30, 40, 50])

        # SINGLE NODE
        bt = binary_search_tree([40])

        bt.delete(40)
        self.assertEqual(bt.inorder(), [None])


if '__main__' == __name__:
    unittest.main()