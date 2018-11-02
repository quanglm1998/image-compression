import huffman.decompressor as decp
import numpy as np
import cv2

class Descompressor(object):
    def decompress(self, args):
        d = decp.Decompressor()
        img = d.decompress(input=args.input, output=None)
        cv2.imwrite(args.output, img)