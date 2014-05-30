import re

#globals
in_file = 'in.txt'
out_file = 'out.txt'


#open file and read content
file = open(in_file,'r')
content = file.read()
#print content

#find and replace content
new_content = re.sub(
           ###search term 
           r'name = "[\w][\w\s]*";',
           ###replacement term
           r'name = "NEW NAME";',
           ###content read from file
           content
)
#print new_content

#open file in write mode to replace content
file = open(out_file,'w')
file.write(new_content)
file.close()

''' SAMPLE in.txt
name = 'fa';            //dont replace
name = "fa";            //replace
name = "fa"             //dont replace
name = "fafa afaf afa"  //dont replace
name = "fafa afaf afa"; //replace
'''
