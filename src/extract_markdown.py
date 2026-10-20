import re 

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text) # Only alt text regex so far 
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches 
