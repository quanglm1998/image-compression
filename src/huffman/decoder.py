from huffman import code_tree
import sys

class Decoder(object):
    def __init__(self, code_tree):
        self.code_tree = code_tree

    def next_symbol(self, input):
        node = self.code_tree.root
        while True:
            if node.val is not None:
                return node.val
            temp = input.read_no_eof()
            if temp == 0:
                node = node.left
            else:
                node = node.right
        raise Exception("Not in code tree")

    def decode(self, input, output):
        cnt = 0
        while True:
            foo = self.next_symbol(input)
            if foo == 256:
                break
            cnt += 1
            if cnt % 1000000 == 0:
                sys.stderr.write(str(cnt) + "\n")
            output.write(bytes((foo,)))
