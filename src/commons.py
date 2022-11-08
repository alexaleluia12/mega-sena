def convert_to_list(lines):
    new_lines = []
    for line in lines:
        tmp = line.split(',')
        tmp = [int(i) for i in tmp]
        new_lines.append(tmp)

    return new_lines
