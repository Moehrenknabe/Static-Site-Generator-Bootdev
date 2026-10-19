import unittest 
from inline_markdown import split_nodes_delimiter
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_code_split(self):
        node = TextNode('This is text with code `print("hello world!")` in the middle', TextType.TEXT)
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        node2 = [
            TextNode('This is text with code ', TextType.TEXT),
            TextNode('print("hello world!")', TextType.CODE),
            TextNode(' in the middle', TextType.TEXT)
            ]
        self.assertEqual(actual, node2)
    def test_bold_split(self):
        node = TextNode('This is text with **bold** in the middle', TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        node2 = [
            TextNode('This is text with ', TextType.TEXT),
            TextNode('bold', TextType.BOLD),
            TextNode(' in the middle', TextType.TEXT)
        ]
        self.assertEqual(actual, node2)
    def test_italic_split(self):
        node = TextNode('This text has _italic_ in the middle', TextType.TEXT)
        actual = split_nodes_delimiter([node], "_", TextType.ITALIC)
        node2 = [
            TextNode('This text has ', TextType.TEXT),
            TextNode('italic', TextType.ITALIC),
            TextNode(' in the middle', TextType.TEXT)
        ]
        self.assertEqual(actual, node2)
    def test_unclosed_delimiter(self):
        node = TextNode('This has italic_ in the middle', TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "_", TextType.ITALIC)
    def test_non_text_type(self):
        node = TextNode('**bold**', TextType.BOLD)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        node2 = [node]
        self.assertEqual(actual, node2)
    def test_multiple_delimiter_pairs(self):
        node = TextNode('Both of these **bold** are **bold**', TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        node2 = [
            TextNode('Both of these ', TextType.TEXT),
            TextNode('bold', TextType.BOLD),
            TextNode(' are ', TextType.TEXT),
            TextNode('bold', TextType.BOLD)
        ]
        self.assertEqual(actual, node2)


if __name__ == "__main__":
    unittest.main()