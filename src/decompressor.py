import huffman.decompressor as decp

class Descompressor(object):
    def decompress(self, args):
        d = decp.Decompressor()
        d.decompress(args.input, args.output)