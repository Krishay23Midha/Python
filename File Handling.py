#read
f = open("myfile.txt", "r") #if we don't write 'r', it'll show the contents as r mode is default
#print(f)
text = f.read()
print(text)
f.close()

#write
f = open("myfile.txt", "w")
f.write('hello world')
print(f)
#this will automatically create a file even if it doesn't exist

#append
f = open("myfile.txt", "a")
f.write('hello world')
print(f)

with open("myfile.txt", "a") as f:
 f.write('bye')
#this will automatically close the file as we are writing with the 'with' command


#append - simply write 'a' to write something at the end of the content in  file
#create - simply write 'x' to create new file, and will show an error if one already exists
#text - simply write 't' to display a text file
#binary - simply write 'b' to display a binary file

