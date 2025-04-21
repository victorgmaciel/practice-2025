import time
from collections import OrderedDict
import xml.etree.ElementTree as ET

class LRUCacheWithTTL:
    def __init__(self, capacity: int, ttl_seconds: int):
        self.capacity = capacity                  # max number of items in cache
        self.ttl = ttl_seconds                    # time-to-live in seconds
        self.cache = OrderedDict()               # key -> (value, timestamp)

    def _is_expired(self, timestamp):
        return time.time() - timestamp > self.ttl

    def get(self, key):
        if key not in self.cache:
            return None

        value, timestamp = self.cache.pop(key)

        # If the item is expired, don't return it
        if self._is_expired(timestamp):
            return None

        # Mark it as recently used
        self.cache[key] = (value, timestamp)
        return value

    def put(self, key, value):
        # If the key is already in the cache, remove it so we can update it
        if key in self.cache:
            self.cache.pop(key)
        # If we're over capacity, evict the least recently used item
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)

        # Insert the new item with current timestamp
        self.cache[key] = (value, time.time())


# ---------------------------------------------------------------------------------------------
# SSML Parser
# A generic XML node with children and attributes
class Node:
    def __init__(self, tag, attrs=None, children=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children = children or []

    def __repr__(self):
        return f"Node(tag={self.tag}, attrs={self.attrs}, children={self.children})"

# A text leaf node (represents just raw text content)
class Text:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Text({self.text})"

def parse_ssml_to_tree(ssml_str: str):
    def build_node(element):
        children = []

        # Add the text content inside the current tag, if any
        if element.text and element.text.strip():
            children.append(Text(element.text.strip()))

        # Recursively process child elements
        for child in element:
            children.append(build_node(child))

            # Handle tail text (after a child element, still within parent)
            if child.tail and child.tail.strip():
                children.append(Text(child.tail.strip()))

        return Node(tag=element.tag, attrs=element.attrib, children=children)

    root = ET.fromstring(ssml_str)
    return build_node(root)



# -------------------------------------------
#  SSML Parser: Node Tree → String

def tree_to_ssml_string(node):
    def render(n):
        if isinstance(n, Text):
            return n.text

        # Format attributes as k="v"
        attr_str = " ".join(f'{k}="{v}"' for k, v in n.attrs.items())
        open_tag = f"<{n.tag}" + (f" {attr_str}" if attr_str else "") + ">"
        close_tag = f"</{n.tag}>"

        # Recursively render children
        inner = "".join(render(child) for child in n.children)
        return f"{open_tag}{inner}{close_tag}"

    return render(node)

