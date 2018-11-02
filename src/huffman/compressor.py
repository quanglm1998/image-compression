from huffman import frequency_table
from huffman import code_tree as ct
from huffman import canonical_code
from huffman import encoder
from bitstream import output as outstream
import contextlib
import sys

class Compressor(object):
    def compress(self, input, output):

        sys.stderr.write("building frequency table\n")
        freq = frequency_table.FrequencyTableBuilder.build_from_input(input)

        sys.stderr.write("building code tree\n")
        code_tree_builder = ct.CodeTreeBuilder()
        code_tree = code_tree_builder.build_from_freq_table(freq.frequencies)

        cano = canonical_code.CanonicalCode(code_tree)
        code_tree = code_tree_builder.build_from_canonical_code(cano)

        sys.stderr.write("encoding file\n")
        with open(input, "rb") as inp,\
                contextlib.closing(outstream.BitOutputStream(open(output, "wb"))) as out:
            cano.write_code_length(out)
            ec = encoder.Encoder(code_tree)
            ec.encode(inp, out)
