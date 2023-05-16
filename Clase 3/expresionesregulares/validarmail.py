import re
email = "dami@dami.com"
test = re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+',email)
if (test):
    print("Ok")
else:
    print("NO Ok")