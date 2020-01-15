# When using `with`, you don't need to explicitly close the file stream.
# Otherwise, it is required.

with open('test.txt', mode='w') as f:
    f.write('This was created by Python script')

my_file = open('test.txt')
print(my_file.read())
my_file.close()
