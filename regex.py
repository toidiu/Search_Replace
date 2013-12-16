import re

#open file and read content
file = open('text.txt','r')
content = file.read()
#print content

#seperate content into lines
#lines = content.split('\n')
#print lines[0]

#find and replace content
new_content = re.sub(r'name = "[\w][\w\s]*";',
           r'name = "test name";',
           content)
print new_content

#open file in write mode to replace content
file = open('text.txt','w')
file.write(new_content)
file.close()

''' text.txt
name = 'fa';
name = "fa";
name = "fa"
name = "fafa afaf afa"
name = "fafa afaf afa";
'''
