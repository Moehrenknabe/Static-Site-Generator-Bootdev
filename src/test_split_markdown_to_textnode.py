import unittest 
from split_markdown_to_textnode import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

class test_split_nodes_images(unittest.TestCase):
    def test_multi_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    def test_no_images(self):
        node = TextNode(
            "This text has no images", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This text has no images", TextType.TEXT)
            ],
            new_nodes,
        )
    def test_empty_string(self):
        node = TextNode(
            "![image1](imgur.com/1.png)![image2](imgur.com/2.png)", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image1", TextType.IMAGE, "imgur.com/1.png"),
                TextNode("image2", TextType.IMAGE, "imgur.com/2.png")
            ],
            new_nodes,
        )

class test_split_nodes_link(unittest.TestCase):
    def test_multi_links(self):
        node = TextNode(
            "This is text with not one [Youtube](youtube.com) but two links [Google](google.com)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with not one ", TextType.TEXT),
                TextNode("Youtube", TextType.LINK, "youtube.com"),
                TextNode(" but two links ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "google.com")
            ],
            new_nodes 
        )
    def test_no_links(self):
            node = TextNode(
                "This text has no links", TextType.TEXT
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This text has no links", TextType.TEXT)
                ],
                new_nodes,
            )
    def test_empty_string(self):
        node = TextNode(
            "[link1](youtube.com)[link2](google.com)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link1", TextType.LINK, "youtube.com"),
                TextNode("link2", TextType.LINK, "google.com")
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()