class CanonicalCode(object):
    def __init__(self, code_tree=None):
        self.code_length = ([0] * 257)
        
        def dfs(node, d):
            if node.val is not None:
                self.code_length[node.val] = d
                return
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        if code_tree is not None:
            dfs(code_tree.root, 0)

    def write_code_length(self, output):
        for val in self.code_length:
            for j in reversed(range(8)):
                output.write((val >> j) & 1)

    def read_code_length(self, input):
        def next_int(input):
            res = 0
            for i in range(8):
                res = (res << 1) | input.read_no_eof()
            return res

        for i in range(257):
            self.code_length[i] = next_int(input)