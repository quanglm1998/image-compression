import heapq

class Node(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CodeTree(object):
    def __init__(self, root, code_list):
        self.root = root
        self.code_list = code_list

    def __str__(self):
        res = ""
        for u in self.code_list:
            res += str(u)
            res += '\n'
        return res

    def get_code(self, symbol):
        return self.code_list[symbol]


class CodeTreeBuilder(object):
    def build_from_freq_table(self, freq):
        heap = []
        for (id, val) in enumerate(freq):
            if val > 0:
                heapq.heappush(heap, (val, id, Node(val=id)))

        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            new = (left[0] + right[0], left[1], Node(left=left[2], right=right[2]))
            heapq.heappush(heap, new)

        return self.build_from_node(heap[0][2])

    def dfs(self, node, code_list, prefix):
        if node.val is not None:
            code_list[node.val] = prefix
            return
        self.dfs(node.left, code_list, prefix + (0, ))
        self.dfs(node.right, code_list, prefix + (1, ))

    def build_from_node(self, root):
        code_list = ([0] * 257)
        self.dfs(root, code_list, ())
        return CodeTree(root, code_list)

    def build_from_canonical_code(self, cano):
        nodes = []
        for i in range(len(cano.code_length), -1, -1):
            new_nodes = []
            if i > 0:
                for (id, foo) in enumerate(cano.code_length):
                    if foo == i:
                        new_nodes.append(Node(val=id))
            for j in range(0, len(nodes), 2):
                new_nodes.append(Node(left=nodes[j], right=nodes[j + 1]))
            nodes = new_nodes
        return self.build_from_node(nodes[0])