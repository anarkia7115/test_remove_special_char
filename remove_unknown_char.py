import sys
reload(sys)
sys.setdefaultencoding("utf-8")
with open("./to_be_replaced.txt") as file_input, \
    open("./special_char_removed.txt", 'w') as file_output:
    for line in file_input:
        line = line.replace(unichr(21704), "***")
        file_output.write(line + "\n")
