from split_blocks import markdown_to_blocks
from block_to_blocktype import block_to_block_type, BlockType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_children
from textnode import TextNode, TextType, text_node_to_html_node

def md_to_html_node(md: str):
    blocks = markdown_to_blocks(md)
    html_nodes = []
    for block in blocks:
        # Determine Blocktype 
        block_type = block_to_block_type(block)
        # Create a HTML Node for the corrosponding block type 
        lines = block.split("\n")
        cleaned_lines = []
        
        if block_type == BlockType.QUOTE:
            for line in lines:
                cleaned_lines.append(line.lstrip(">").strip())
            new_text = " ".join(cleaned_lines)
            children_list = text_to_children(new_text)
            parent_node = ParentNode("blockquote", children_list)
            html_nodes.append(parent_node)
        elif block_type == BlockType.PARAGRAPH:
            cleaned_paragraph = block.replace("\n", " ")
            children_list = text_to_children(cleaned_paragraph)
            parent_node = ParentNode("p", children_list)
            html_nodes.append(parent_node)
        elif block_type == BlockType.UNORDERED_LIST:
            list_items = []
            for line in lines:
                cleaned_line = (line.lstrip("-").strip())
                child_text = text_to_children(cleaned_line)
                parent_node = ParentNode("li", child_text)
                list_items.append(parent_node)
            parent_node = ParentNode("ul", list_items)
            html_nodes.append(parent_node)
        elif block_type == BlockType.ORDERED_LIST:
            list_items = []
            counter = 1 
            for line in lines:
                cleaned_lines = line.lstrip(f"{counter}. ").strip()
                counter += 1 
                child_text = text_to_children(cleaned_lines)
                parent_node = ParentNode("li", child_text)
                list_items.append(parent_node)
            parent_node = ParentNode("ol", list_items)
            html_nodes.append(parent_node)
        elif block_type == BlockType.CODE:
            clean = block.lstrip("```\n").strip("```")
            text_node = TextNode(clean, TextType.TEXT)
            leafnode = text_node_to_html_node(text_node)
            code_tag = ParentNode("code", [leafnode])
            pre_tag = ParentNode("pre", [code_tag])
            html_nodes.append(pre_tag)
        elif block_type == BlockType.HEADING:
            hash_count = len(block) - len(block.lstrip("#"))
            clean = block.lstrip("# ").strip()
            children_list = text_to_children(clean)
            parent_node = ParentNode(f"h{hash_count}", children_list)
            html_nodes.append(parent_node)
    div_node = ParentNode("div", html_nodes)        


    return div_node

