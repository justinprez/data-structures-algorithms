# RouteTrieNode
class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, part):
        if part not in self.children:
            self.children[part] = RouteTrieNode()

# RouteTrie
class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode(handler)

    def insert(self, path_parts, handler):
        node = self.root
        for part in path_parts:
            if part not in node.children:
                node.insert(part)
            node = node.children[part]
        node.handler = handler

    def find(self, path_parts):
        node = self.root
        for part in path_parts:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler

# Router
class Router:
    def __init__(self, root_handler, not_found_handler=None):
        self.route_trie = RouteTrie(root_handler)
        self.not_found = not_found_handler

    def add_handler(self, path, handler):
        if not isinstance(path, str):
            print(f"Invalid path '{path}' provided. Expected a string.")
            return
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        if not isinstance(path, str):
            return self.not_found
        path_parts = self.split_path(path)
        if len(path_parts) == 0:  # Handle the case for root
            return self.route_trie.root.handler

        handler = self.route_trie.find(path_parts)
        if handler is None:
            return self.not_found
        return handler

    def split_path(self, path):
        return [part for part in path.split('/') if part]

# Test cases
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

print(router.lookup("/"))  # 'root handler'
print(router.lookup("/home"))  # 'not found handler'
print(router.lookup("/home/about"))  # 'about handler'
print(router.lookup("/home/about/"))  # 'about handler'
print(router.lookup("/home/about/me"))  # 'not found handler'

# 1. Lookup without starting forward slash
print(router.lookup("home/about"))  # 'about handler'

# 2. Paths with multiple successive slashes
router.add_handler("/home//about", "about handler with double slash")
print(router.lookup("/home//about"))  # 'about handler with double slash'

# 3. Adding and looking up handlers with longer paths
router.add_handler("/home/about/me/and/you", "deep handler")
print(router.lookup("/home/about/me/and/you"))  # 'deep handler'

# 4. Empty paths or handlers
router.add_handler("", "empty path handler")
print(router.lookup(""))  # 'root handler'  # It should default to root as an empty path should be treated as root
router.add_handler("/emptyhandler", "")
print(router.lookup("/emptyhandler"))  # ''

# 5. Non-string inputs (let's see how it behaves)
router.add_handler(123, "number path")
print(router.lookup(123))  # 'not found handler'  # It should handle it as 'not found' since we're expecting strings