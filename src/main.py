from textnode import TextNode
from textnode import Texttypes

def main():
    node = TextNode("this is an example text", Texttypes.bold_text, "https://www.youtube.com")
    print(node)

main()