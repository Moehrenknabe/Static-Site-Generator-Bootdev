import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("Test.png", TextType.IMAGES)
        node2 = TextNode("Test.png", TextType.IMAGES)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("Example Text", TextType.ITALIC_TEXT, "https://www.youtube.com")
        node2 = TextNode("Different Example Text", TextType.TEXT_PLAIN)
        self.assertNotEqual(node, node2)
    


if __name__ == "__main__":
    unittest.main()