def get_binary(data):
    scale = 16
    num_of_bits = 32
    result = bin(int(data, scale))[2:].zfill(num_of_bits)
    return result


def get_decimal(data):
    result = int(data, base=16)
    return result
