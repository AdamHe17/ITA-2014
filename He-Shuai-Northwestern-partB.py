import zipfile
import gzip
f = gzip.open('code.gz', 'rb')
content = f.read()
with open('code.in', 'w') as o:
	o.write(content)
f.close()