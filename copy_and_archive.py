import time
import tarfile
import hashlib
source=open('/dev/loop5','rb')
tm=str(time.time())
blocksize=512
bytes=b'x00'
evidence=open('evidence__'+tm+'.dd','wb')
while bytes:
	bytes=source.read(blocksize)
	evidence.write(bytes)
source.close()
evidence.close()

compressed=tarfile.open('evidence__'+tm+'.tar','w:xz')
compressed.add('evidence__'+tm+'.dd')
compressed.close()

hash_algo=hashlib.sha256()
evidence=open('evidence__'+tm+'.tar','rb')
while bytes:
	bytes=evidence.read(blocksize)
	hash_algo.update(bytes)
hash_algo.update(tm.encode())
print(hash_algo.hexdigest())
