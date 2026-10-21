def markdown_to_blocks(raw_markdown_string:str) -> list[str]:
    splitted = raw_markdown_string.split("\n\n")
    blocks = []
    for i in splitted:
        stripped = i.strip()
        if len(stripped) == 0:
            continue
        blocks.append(stripped)
    return blocks 

if __name__ == "__main__":
    print(markdown_to_blocks(
        "# This is a heading\n\n This is a paragraph of text. It has some **bold** and _italic_ words inside of it.\n\n - This is the first list item in a list block\n - This is a list item\n - This is another list item"
    ))