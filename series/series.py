def slices(series, length):
    s = []
    i = 0
    if length not in range(1, length + 1) or length > len(series):
        raise ValueError('Wrong')
    while length:
        s.append(series[i:length])
        i += 1
        length = length + 1 if length < len(series) else 0
    return s
