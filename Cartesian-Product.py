file1_obj = open('file1', 'r')

while 1:
    file1_line = file1_obj.readline()
    if len(file1_line) == 0:
        break
    file2_obj = open('file2', 'r')
    while 1:
        file2_line = file2_obj.readline()
        if len(file2_line) == 0:
            file2_obj.close()
            break
        print file1_line[:len(file1_line)-1] + ' ' + file2_line[:len(file2_line)-1]
