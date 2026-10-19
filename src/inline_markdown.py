from textnode import TextNode, TextType

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