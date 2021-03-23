import re
import os
import sys

def clean(tk):
	match = re.search(r'^[\.,!\?;:\(\)\[\]\'\"\s\t]*(.*?)[\.,!\?;:\(\)\[\]\'"\s\t]*$', tk)
	if match:
		return match.group(1)
	return tk

for line in sys.stdin:
    line = line.strip()
    for w in line.split():
        print clean(w)
    print
    