from textnode import TextNode, TextType
import re


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_text = old_node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise Exception("improper markdown, formatted section not closed")
        result = []
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(split_text[i], TextType.TEXT))
            else:
                result.append(TextNode(split_text[i], text_type))
        new_nodes.extend(result)
    return new_nodes


def extract_markdown_images(text: str) -> list[set]:
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text: str) -> list[set]:
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)
