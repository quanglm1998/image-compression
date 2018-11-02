import argparse
import numpy
import cv2
import compressor
import decompressor

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--decompress", action='store_true', help="decompression")
    parser.add_argument("--color", action='store_true', help="colored image")
    parser.add_argument("input", help="input file path")
    parser.add_argument("output", help="output file path")
    args = parser.parse_args()
    
    if (args.decompress):
        decomp = decompressor.Descompressor()
        decomp.decompress(args)
    else:
        comp = compressor.Compressor()
        comp.compress(args)