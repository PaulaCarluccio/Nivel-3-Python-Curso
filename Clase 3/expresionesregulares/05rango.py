import re
#regex = "([a-zA-Z]+$)"
regex = "([a-cA-C1-5]+$)"
if re.match(regex, "cba"):
 print("Ok match")
else:
 print("NO OK match")