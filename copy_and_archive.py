import time
import tarfile
import hashlib
source=open('/dev/loop5','rb')
tm=str(time.time())
blocksize=512
bytes=b'x00'
evidence=open('evidence__'+tm+'.dd','wb')
hash_algo=hashlib.sha256()
while bytes:
	bytes=source.read(blocksize)
	evidence.write(bytes)
	hash_algo.update(bytes)
hash_algo.update(tm.encode())
print(hash_algo.hexdigest())
source.close()
evidence.close()
compressed=tarfile.open('evidence__'+tm+'.tar','w:xz')
compressed.add('evidence__'+tm+'.dd')
compressed.close()
