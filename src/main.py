from textnode import TextNode
from textnode import TextType
from split_delimiter import split_nodes_delimiter

def main():
    node = TextNode("this is an example text", TextType.BOLD, "https://www.youtube.com")
    print(node)

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    print(split_nodes_delimiter([node], "`", TextType.CODE))

main()