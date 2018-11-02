class Evaluator(object):
    def __init__(self, original=0, encoded=0):
        self.original = original
        self.encoded = encoded

    def show_ratio(self):
        print("original size: " + str(self.original))
        print("encoded size: " + str(self.encoded))
        print("compress rate: " + str(self.original / self.encoded))