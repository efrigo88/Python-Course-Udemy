# we use 'bw' parameter, 'b' means binary, we are about to write in binary
with open('writing/binary', 'bw') as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

with open('writing/binary', 'br') as binFile:
    for i in binFile:
        print(i)






