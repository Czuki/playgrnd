# def distance(strand_a, strand_b):
#     if zip(strand_a, strand_b) != zip(strand_b, strand_a):
#         raise ValueError('strands are of not equal length')
#     return sum([a != b for a, b in zip(strand_a, strand_b)])

def distance(strand1, strand2):
    return sum(i != j for i, j in zip(strand1, strand2))