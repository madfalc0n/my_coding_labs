import markdown


f = open('myfile.txt', 'r')
htmlmarkdown=markdown.markdown( f.read() )


print(htmlmarkdown)