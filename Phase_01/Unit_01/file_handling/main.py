file_content = [
    'additional line 1',
    'additional line 2',
]

# file = open('example.txt', 'a')
# file.write('\n'.join(file_content))
# file.close()

file = open('example.txt', 'r')
content = file.read()
print(content)