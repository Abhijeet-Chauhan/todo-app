contents = ['a','b','c']

filenames = ['a.txt','b.txt','c.txt']

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}",'w')
    file.write(content)
