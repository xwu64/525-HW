file1_obj = open('Outer_Join_file1', 'r')

while 1:
    file1_line = file1_obj.readline()
    if len(file1_line) == 0:
        break
    file1_line = file1_line[:len(file1_line) - 1]
    file1_line = file1_line.split(' ')

    file2_obj = open('Outer_Join_file2', 'r')

    outline = file1_line[:]
    outline.append('null')
    outline.append('null')

    while 1:
        file2_line = file2_obj.readline()
        if len(file2_line) == 0:
            file2_obj.close()
            break

        file2_line = file2_line[:len(file2_line) - 1]
        file2_line = file2_line.split(' ')

        if file1_line[0] == file2_line[1] and file1_line[2] == file2_line[2]:
            outline = file1_line[:]
            outline.append(file2_line[0])
            outline.append(file2_line[3])
            print outline

    if outline[len(outline) - 1] == 'null':
        print outline

