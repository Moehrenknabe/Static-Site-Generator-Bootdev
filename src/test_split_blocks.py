import unittest 
from split_blocks import markdown_to_blocks

class test_blocks(unittest.TestCase):
    def test_mixed_one(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_mixed_one(self):
        md = """
This is some stuff i write

Which is **bold** and _italic_

- but 
- not 
- useful 

But here take this ![image](image.link) and a [link](site.com)

Have Fun! 
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
            "This is some stuff i write",
            "Which is **bold** and _italic_",
            "- but \n- not \n- useful",
            "But here take this ![image](image.link) and a [link](site.com)",
            "Have Fun!"
            ]

        )
if __name__ == "__main__":
    unittest.main()