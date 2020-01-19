fw = open('Sample.txt','w')

fw.write('Hi, this is my first file in python\n')
fw.write('This is so cool!! \n')

fw.close()

fr = open('Sample.txt','r')

text = fr.read()

print(text)

fr.close()

