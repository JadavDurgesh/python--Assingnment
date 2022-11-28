def file_read(fname):
    with open(fname) as f:
        content_list = f.readline()
        print(content_list)

file_read("student.txt")