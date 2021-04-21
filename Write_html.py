def update(text,size):
    f = open('C:\\Users\\lvbt\\Documents\\index.html','w')

    message = """<html>
    <head></head>
    <body> <p style='font-size:"""+str(size)+"""px'>""" + text + """</p> </body>
    </html>"""

    f.write(message)
    f.close()
