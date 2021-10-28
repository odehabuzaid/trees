import pytest
from trees import __version__
from trees.node import Node
from trees.tree import Tree

tree = Tree()

def test_version():
    assert __version__ == '0.1.0'


# Can successfully instantiate an empty tree
@pytest.mark.skip
def test_init_an_empty_tree():
    # Arrange 
    t_test = Tree()
    # Actual
    actual = t_test.value
    # Expected
    expected = None
    assert actual == expected

    
# Can successfully instantiate a tree with a single root node
@pytest.mark.skip
def test_successfully_init_with_single_root():
    # Arrange 
    a = Node('a')
    tree.root = a
    # Actual
    actual = tree.root.value
    # Expected
    expected = 3

    assert actual == expected
   
# Can successfully add a left child and right child to a single root node
@pytest.mark.skip
def test_successfully_add_left_right_childs_to_root():
    # Arrange 
    tree.root = Node('a')
    tree.root.left = Node('b')
    tree.root.right = Node('c')
    # Actual
    actual = '{} {}'.format(tree.left.value,tree.right.value)
    # Expected
    expected = 'a b'

    assert actual == expected
    
# Can successfully return a collection from a preorder traversal
@pytest.mark.skip
def test_successfully_return_preorder_traversal():
    # Actual
    actual = tree.pre_order()
    # Expected
    expected = ["1", "2", "4", "3"]

    assert actual == expected

# Can successfully return a collection from an inorder traversal
@pytest.mark.skip
def test_successfully_return_in_order_traversal():
  # Expected
  expected = ["4", "2", "1", "3"]
  # Actual
  actual = tree.in_order()
  
  assert actual == expected

# Can successfully return a collection from a postorder traversal
def test_successfully_return_postorder_traversal():
  # Expected
  expected = ["4", "2", "3", "1"]
  # Actual
  actual = tree.in_order()
  
  assert actual == expected


@pytest.fixture(autouse=True)
def arrange():
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    # Add Root node to tree
    tree.root=a_node 
