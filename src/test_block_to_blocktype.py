import unittest 
from block_to_blocktype import block_to_block_type, BlockType

class test_block_to_blocktype(unittest.TestCase):
    def test_paragraph(self):
        block = (" adsawdad ")
        case = block_to_block_type(block)
        control = BlockType.PARAGRAPH
        self.assertEqual = (case, control)
    def test_heading(self):
        block = ("###### awiduaw")
        case = block_to_block_type(block)
        control = BlockType.HEADING
        self.assertEqual = (case, control)
    def test_code(self):
        block = ("```\n aWE1234E ```")
        case = block_to_block_type(block)
        control = BlockType.CODE 
        self.assertEqual = (case, control)
    def test_quote(self):
        block = ("> awdhuawdhu")
        case = block_to_block_type(block)
        control = BlockType.QUOTE 
        self.assertEqual(case, control)
    def test_unordered_list(self):
        block = ("- 2323\n- 323232\n- 2323")
        case = block_to_block_type(block)
        control = BlockType.UNORDERED_LIST
        self.assertEqual(case, control)    
    def test_ordered_list(self):
        block = ("1. adawd\n2. dadaw\n3. adwawda")
        case = block_to_block_type(block)
        control = BlockType.ORDERED_LIST
        self.assertEqual(case, control)

if __name__ == "__main__":
    unittest.main()