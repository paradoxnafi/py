# 23rd video

f_write = open('first-file.txt', 'w')
f_write.write('Hey there')
f_write.write('We are typing in a file\n')
f_write.write('Afer new line\n\n')
f_write.close()

f_read = open('first-file.txt', 'r')
print_this_crap = f_read.read()

print(print_this_crap)
f_read.close()