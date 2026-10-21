from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    textnode_list = []
  
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            textnode_list.append(old_node)
        else:
            images = extract_markdown_images(old_node.text)
            if len(images) == 0:
                textnode_list.append(old_node)
                continue 
            remaining_text = old_node.text 
            for image_alt, image_link in images:
                new_node = remaining_text.split(f"![{image_alt}]({image_link})", 1) 
                if len(new_node[0]) > 0:
                    textnode_list.append(TextNode(new_node[0], TextType.TEXT))
                textnode_list.append(TextNode(image_alt, TextType.IMAGE, image_link))
                remaining_text = new_node[1]
            if len(remaining_text) > 0:
                textnode_list.append(TextNode(remaining_text, TextType.TEXT))
            
    return textnode_list
    
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    textnode_list = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            textnode_list.append(old_node)
        else:
            links = extract_markdown_links(old_node.text)
            if len(links) == 0:
                textnode_list.append(old_node)
                continue 
            remaining_text = old_node.text 
            for link_alt, link in links:
                new_node = remaining_text.split(f"[{link_alt}]({link})", 1)
                if len(new_node[0]) > 0:
                    textnode_list.append(TextNode(new_node[0], TextType.TEXT))
                textnode_list.append(TextNode(link_alt, TextType.LINK, link))
                remaining_text = new_node[1]
            if len(remaining_text) > 0:
                textnode_list.append(TextNode(remaining_text, TextType.TEXT))
    return textnode_list 