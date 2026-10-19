import unittest
from htmlnode import HTMLNode

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
            

if __name__ == "__main__":
    unittest.main()