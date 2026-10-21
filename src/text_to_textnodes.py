from textnode import TextType, TextNode
from split_markdown_to_textnode import extract_markdown_links, extract_markdown_images
from inline_markdown import split_nodes_delimiter

def text_to_textnodes(text):
    text_textnode = TextNode(text, TextType.TEXT)
    textnodes = []
    textnodes.append(text_textnode)
    markdown_textnode = split_nodes_delimiter(textnodes, "**", TextType.BOLD)
    markdown_textnode = split_nodes_delimiter(textnodes, "_", TextType.ITALIC)
    markdown_textnode = split_nodes_delimiter(textnodes, "`", TextType.CODE)
    markdown_textnode = extract_markdown_links([markdown_textnode])
    markdown_textnode = extract_markdown_images([markdown_textnode])
    return markdown_textnode

    