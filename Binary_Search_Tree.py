import unittest

class binary_search_tree:
    def __init__ (self, init=None):
        self.__value = self.__left = self.__right = None

        if init:
            for i in init:
                self.add(i)

    def __iter__(self):
        if self.__left:
            for node in self.__left:
                yield(node)

        yield(self.__value)

        if self.__right:
            for node in self.__right:
                yield(node)

    def __str__(self):
        return(','.join(str(node) for node in self))

    def add(self, value):
        # if this is the first value for this node, just set to node's value
        # if the value is less than this node's value
            # if there isn't a left
                # create a new tree and have left refer to it
            # else
                # make a recursive call
        # else
            #if there isn't a right...
        pass


    def preorder(self):
        pass

    def inorder(self):
        pass

    def postorder(self):
        pass

    def BFS(self):
        # create a queue with the root element, and an empty list
        # while there are nodes in the queue
            # grab the first one and add it to the result list
            # if there is a node to the left, add that to the queue
            # if there is a node to the right, add that to the queue
        pass

class test_binary_search_tree (unittest.TestCase):
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
    '''
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
    '''

    # A level
    '''
    def test_empty_BFS(self):
        self.assertEqual(binary_search_tree().BFS(), [None])
    def test_BFS(self):
        bt = binary_search_tree([20, 10, 30, 25, 35])
        self.assertEqual(bt.BFS(), [20, 10, 30, 25, 35])
    '''

if '__main__' == __name__:
    unittest.main()