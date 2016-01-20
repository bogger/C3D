import os
import struct
def read(path): 

	f = open(path,'rb')
	content = f.read()
	f.close()
	size = struct.unpack('iiiii',content[:20])
	length = size[0]*size[1]*size[2]*size[3]*size[4]
	feats = struct.unpack('f'*length,content[20:])
	return feats
#print feats
#if __name__ == 'main':
#	read_binary_blob(arg)
