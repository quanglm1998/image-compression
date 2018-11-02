import bitstream.input as instream
from huffman import canonical_code
from huffman import code_tree
from huffman import decoder
import numpy as np
import sys

class Decompressor(object):
    def decompress(self, input=None, output=None):
        with open(input, "rb") as inp:
            input_stream = instream.BitInputStream(inp)

            sys.stderr.write("reading code tree\n")
            cano = canonical_code.CanonicalCode()
            cano.read_code_length(input_stream)

            code_tree_builder = code_tree.CodeTreeBuilder()
            code = code_tree_builder.build_from_canonical_code(cano)

            sys.stderr.write("decoding\n")
            dc = decoder.Decoder(code)
            arr = np.array([])
            if output is not None:
                out = open(output, "wb")
                dc.decode_to_output(input_stream, out)
            else:
                shape = self.read_shape(input_stream)
                arr = dc.decode_to_arr(input_stream)
                if shape[2] == 1:
                    shape = shape[:2]
                img = arr.reshape(shape)
                return img

    def read_shape(self, input):
        def next_int(input):
            res = 0
            for i in range(16):
                res = (res << 1) | input.read_no_eof()
            return res

        shape = ()
        for i in range(3):
            shape = shape + (next_int(input),)
        return shape