from huffman import frequency_table
from huffman import code_tree as ct
from huffman import canonical_code
from huffman import encoder
from bitstream import output as outstream
import numpy as np
import cv2
import contextlib
import sys

class Compressor(object):
    def compress(self, img=None, input=None, output=None):
        arr = np.array([])
        if img is not None:
            arr = img.ravel()

        sys.stderr.write("building frequency table\n")
        if input is not None:
            freq = frequency_table.FrequencyTableBuilder.build_from_input(input)
        else:
            freq = frequency_table.FrequencyTableBuilder.build_from_arr(arr)

        sys.stderr.write("building code tree\n")
        code_tree_builder = ct.CodeTreeBuilder()
        code_tree = code_tree_builder.build_from_freq_table(freq.frequencies)

        cano = canonical_code.CanonicalCode(code_tree)
        code_tree = code_tree_builder.build_from_canonical_code(cano)

        sys.stderr.write("encoding file\n")
        if input is not None:
            with open(input, "rb") as inp,\
                    contextlib.closing(outstream.BitOutputStream(open(output, "wb"))) as out:
                cano.write_code_length(out)
                ec = encoder.Encoder(code_tree)
                ec.encode_from_input(inp, out)
        else:
            with contextlib.closing(outstream.BitOutputStream(open(output, "wb"))) as out:
                cano.write_code_length(out)
                self.write_shape(img.shape, out)
                ec = encoder.Encoder(code_tree)
                ec.encode_from_arr(arr, out)

    def write_shape(self, shape, output):
        if len(shape) == 2:
            shape = shape + (1, )
        for u in shape:
            for i in reversed(range(16)):
                output.write((u >> i) & 1)