from huffman import compressor as cp
import cv2
import evaluator
import numpy as np
import os

class Compressor(object):
    def compress(self, args):
        eval = evaluator.Evaluator()

        # read image part
        img = cv2.imread(args.input, args.color)

        # TODO: add more stuff

        # Huffman code part
        c = cp.Compressor()
        c.compress(img=img, input=None, output=args.output)
        eval.original = img.size
        eval.encoded = os.path.getsize(args.output)
        eval.show_ratio()
