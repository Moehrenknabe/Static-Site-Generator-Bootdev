from textnode import TextNode, TextType
from textnode import text_node_to_html_node
from split_markdown_to_textnode import split_nodes_image, split_nodes_link

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        else:
            sections = old_node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise ValueError ("This is not valid Markdown syntax!")
            for i in range(len(sections)):
                if len(sections[i]) == 0:
                    continue  
                if i % 2 == 0: 
                    new_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(sections[i], text_type))
    return new_nodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children 

def text_to_textnodes(text):
    text_textnode = TextNode(text, TextType.TEXT)
    textnodes = []
    textnodes.append(text_textnode)
    markdown_textnode = split_nodes_delimiter(textnodes, "**", TextType.BOLD)
    markdown_textnode = split_nodes_delimiter(markdown_textnode, "_", TextType.ITALIC)
    markdown_textnode = split_nodes_delimiter(markdown_textnode, "`", TextType.CODE)
    markdown_textnode = split_nodes_image(markdown_textnode)
    markdown_textnode = split_nodes_link(markdown_textnode)
    return markdown_textnode