class NegativeAdder(Exception):
    def __init__(self, negative_nums):
        print(f'negatives not allowed: {negative_nums}')


