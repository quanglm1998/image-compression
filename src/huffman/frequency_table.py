# A list of symbol frequencies, has exactly 257 character, 265 + 1 EOF
class FrequencyTable(object):
    def __init__(self, frequencies):
        self.frequencies = list(frequencies)    # don't want this pass-by-value variable to be changed

    def increase(self, id):
        self.frequencies[id] += 1
    
    def get(self, id):
        return self.frequencies[id]

    def set(self, id, val):
        self.frequencies[id] = val


class FrequencyTableBuilder(object):
    @staticmethod
    def build_from_input(input):
        res = FrequencyTable([0] * 257)
        with open(input, "rb") as f:
            b = f.read(1)
            while b:
                b = b[0]
                res.increase(b)
                b = f.read(1)
        res.increase(256)
        return res

    @staticmethod
    def build_from_arr(arr):
        res = FrequencyTable([0] * 257)
