import hashlib

a = 'sdfdsf'
a = hashlib.md5(a.encode()).hexdigest()

print(hashlib.md5(a.decode()))