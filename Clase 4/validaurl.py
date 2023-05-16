import re
url = "https://damiandeluca.com.ar"
test = re.match(r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$',url)

if test:
    print("URL Ok")
else:
    print("URL NO Ok")

#Ejemplo by https://www.regextester.com/93652