from huffman import code_tree
import sys

class Encoder(object):
    def __init__(self, code_tree):
        self.code_tree = code_tree

    def encode(self, input, output):
        b = input.read(1)
        cnt = 0
        while b:
            res = self.code_tree.get_code(b[0])
            cnt += 1
            if cnt % 1000000 == 0:
                sys.stderr.write(str(cnt) + "\n")
            for b in res:
                output.write(b)
            b = input.read(1)
        res = self.code_tree.get_code(256)
        for b in res:
                output.write(b)