path = "student.csv"
file = open( path, 'r' )
with file as files :
    content = files.read()
print( content )
file.close()