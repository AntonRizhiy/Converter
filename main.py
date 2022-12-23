import converters as conv  # import file converters for using functions get_binary and get_decimal
import parser_line as pl  # import file parser_line for using function parse_line

try:
    file = open('in.txt', 'r')  # open file to count number of lines in file

    file_data = file.readlines()  # read all file and get array lines
    file_size = len(file_data)  # get size array

    file.close()  # close file

    file = open('in.txt', 'r')  # open file to work with every line
    start_position = 0  # current position to start parse the line in file

    new_file = open('out_Anton.txt', 'w')  # created new file to write result convert

    while start_position < file_size:  # loop to work with every line
        line_data = file.readline()  # read line to get data
        line_size = len(line_data)  # get size line

        # Get two arrays. Index for convert to decimal and array for convert to binary.
        data_for_decimal, data_for_binary = pl.parse_line(line_data, line_size)

        index = conv.get_decimal(data_for_decimal)  # converted value index
        binary = conv.get_binary(data_for_binary)  # converted value in binary

        # Write single line with index, input array to convert and converted result in binary form
        new_file.write(f"At index {index} hex value {data_for_binary} converted to bin {binary}\n")

        start_position += 1  # increment current position to step on next line in file

    file.close()  # close read file
    new_file.close()  # close writen file

except FileNotFoundError:  # if name file is incorrect
    print('File not found, sry ;(')
