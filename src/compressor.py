from huffman import compressor as cp
import cv2
import evaluator
import numpy as np
import os

class Compressor(object):
    def compress(self, args):
        eval = evaluator.Evaluator()

        # read image part
        # img = cv2.imread(args.input, args.color)
        # eval.original = img.size

        # a = np.array([[[1,2], [3,4]], [[5, 6], [7, 8]]])
        # b = a.ravel()
        # b = b.reshape((2, 2, 2))
        # print(b)

        # TODO: add more stuff

        # Huffman code part
        c = cp.Compressor()
        c.compress(args.input, args.output)
        eval.original = os.path.getsize(args.input)
        eval.encoded = os.path.getsize(args.output)
        eval.show_ratio()
