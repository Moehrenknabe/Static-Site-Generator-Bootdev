import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_dictionary(self):
        node = HTMLNode(props={"key": "value (link)"})
        result = node.props_to_html()
        self.assertEqual(result, ' key="value (link)"')
    def test_empty_dictionary(self):
        node = HTMLNode(props={})
        result = node.props_to_html()
        self.assertEqual(result, "")
    def test_none_props(self):
        node = HTMLNode()
        result = node.props_to_html()
        self.assertEqual(result, "")

class TestLeafNote(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_props(self):
        node = LeafNode("p", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<p href="https://www.google.com">Hello, world!</p>')
    def test_leaf_to_html_value_none(self):
        node = LeafNode("p", value=None)
        with self.assertRaises(ValueError):
            node.to_html()
    def test_leaf_to_html_empty_tag(self):
        node = LeafNode(tag=None, value="Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")
            

if __name__ == "__main__":
    unittest.main()