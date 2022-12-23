def parse_line(line_data, line_size):
    underscore = 2

    decimal_index = 0
    binary_index = underscore + 1

    data_for_decimal = ""
    data_for_binary = ""

    while decimal_index < underscore:
        data_for_decimal = data_for_decimal + line_data[decimal_index]
        decimal_index += 1

    while binary_index < line_size - 1:
        data_for_binary = data_for_binary + line_data[binary_index]
        binary_index += 1

    return data_for_decimal, data_for_binary
