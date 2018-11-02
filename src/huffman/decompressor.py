import bitstream.input as instream
from huffman import canonical_code
from huffman import code_tree
from huffman import decoder
import sys

class Decompressor(object):
    def decompress(self, input, output):
        with open(input, "rb") as inp,\
                open(output, "wb") as out:
            
            input_stream = instream.BitInputStream(inp)

            sys.stderr.write("reading code tree\n")
            cano = canonical_code.CanonicalCode()
            cano.read_code_length(input_stream)

            code_tree_builder = code_tree.CodeTreeBuilder()
            code = code_tree_builder.build_from_canonical_code(cano)

            sys.stderr.write("decoding\n")
            dc = decoder.Decoder(code)
            dc.decode(input_stream, out)
