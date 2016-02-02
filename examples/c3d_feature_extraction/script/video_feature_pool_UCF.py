import os
import glob
import numpy as np
import read_binary_blob
import cPickle
import sys
sav_dir = '/media/researchshare/linjie/data/UCF-101_features/'
feat_dir = '/media/researchshare/linjie/data/UCF-101_features/c3d/'
fds = os.listdir(feat_dir)
pool_type='mean'
feat_dim = 4096
stage=sys.argv[1]#'train'
list_path='/home/a-linjieyang/work/video_caption/ucfTrainTestlist/%slist01.txt' % stage
with open(list_path,'r') as f:
	pooled_feats=[]
	for line in f:
		content = line.split()
		vid_fd = content[0][:-4]
		feat_names = os.listdir(feat_dir+vid_fd)
		feat_n = len(feat_names)
		feats_seq = np.zeros((feat_n,feat_dim))
		
		for i,path in enumerate(feat_names):
			feats = read_binary_blob.read(feat_dir+vid_fd+'/'+path)
			feats_seq[i,:] = np.asarray(feats, dtype=np.float32)
			#agg_feats = np.maximum(feats, agg_feats)
		if pool_type=='mean':
			agg_feats = np.mean(feats_seq, axis=0)
		else:
			agg_feats = np.amax(feats_seq, axis=0)
		pooled_feats.append(agg_feats)
pooled_feats = np.vstack(pooled_feats)
with open('%sc3d_pooled_%s' % (sav_dir,stage),'wb') as fout:
	cPickle.dump(pooled_feats,fout, protocol=cPickle.HIGHEST_PROTOCOL)
		#print 'start to save feature for %s' % fd 
		#print agg_feats.shape
		#with open(feat_dir+fd+'/agg_feats','wb') as f:
			#cPickle.dump(agg_feats,f, protocol=cPickle.HIGHEST_PROTOCOL)


