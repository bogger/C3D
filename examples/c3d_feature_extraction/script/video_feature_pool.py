import os
import glob
import numpy as np
import read_binary_blob
import cPickle
feat_dir = '/media/researchshare/linjie/data/snapchat/features/c3d_resize/'
fds = os.listdir(feat_dir)
feat_dim = 4096
for fd in fds:
	feat_names = glob.glob(feat_dir+fd+'/*.fc7-1')
	agg_feats = np.zeros((1,feat_dim))

	for path in feat_names:
		feats = read_binary_blob.read(path)
		feats = np.asarray(feats, dtype=np.float32)
		agg_feats = np.maximum(feats, agg_feats)
	print 'start to save feature for %s' % fd 
	#print agg_feats.shape
	with open(feat_dir+fd+'/agg_feats','wb') as f:
		cPickle.dump(agg_feats,f, protocol=cPickle.HIGHEST_PROTOCOL)


