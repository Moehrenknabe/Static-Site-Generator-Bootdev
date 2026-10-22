from enum import Enum 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block:str) -> BlockType:
    hash_count = len(block) - len(block.lstrip("#"))
    if hash_count < len(block) and 1 <= hash_count <= 6 and block[hash_count] == " " and len(block[hash_count + 1::]) >= 1:  
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith('```'):
        return BlockType.CODE  
    lines = block.split("\n")
    quote_boolean = True 
    for line in lines:
        if not line[0].startswith(">"):
            quote_boolean = False 
    if quote_boolean == True:
        return BlockType.QUOTE 
    elif line.startswith("- "):
        return BlockType.UNORDERED_LIST
    ordered_list_boolean = True 
    expected_counter = 1
    for line in lines:
        if line.startswith(f"{expected_counter}. "):
            expected_counter += 1 
        else:
            ordered_list_boolean = False 
    if ordered_list_boolean == True:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
    

if __name__ == "__main__":
    result = block_to_block_type("1. \n2. \n3 ")
    print(result)