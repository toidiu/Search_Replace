import re

#globals
in_file = 'text.txt'
out_file = 'text.txt'


#open file and read content
file = open(in_file,'r')
content = file.read()
#print content

#find and replace content
new_content = re.sub(
           ###search term
           r'name = "[\w][\w\s]*";',
           ###replacement term
           r'name = "bllaaa name";',
           ###content read from file
           content
)
#print new_content

#open file in write mode to replace content
file = open(out_file,'w')
file.write(new_content)
file.close()

''' text.txt
name = 'fa';
name = "fa";
name = "fa"
name = "fafa afaf afa"
name = "fafa afaf afa";
'''
