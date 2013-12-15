import re

file = open('text.txt','r+')
content = file.read()
#print content

lines = content.split('\n')
#print lines[0]

'''
new = re.sub(r'name = "[a-z]+\s?[a-z]+?";',
           r'name = "new name";',
           content)
print new
'''

new = re.sub(r'name = "[\w][\w\s]*";',
           r'name = "new name";',
           content)
print new

'''
name = 'fa';
name = "fa";
name = "fa"
name = "fafa afaf afa"
name = "fafa afaf afa";
'''
