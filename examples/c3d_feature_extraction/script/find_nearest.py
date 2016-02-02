import os
import cPickle
import shutil
import numpy as np
src_dir = '/media/researchshare/linjie/data/snapchat/video/'
im_dir= '/media/researchshare/linjie/data/snapchat/images/'
feat_dir = '/media/researchshare/linjie/data/snapchat/features/c3d_resize/'
sav_dir = '/media/researchshare/linjie/data/snapchat/similar_c3d_resize/'
fds = os.listdir(feat_dir)
vid_n = len(fds)
print vid_n
#exit()
top_n = 5
feat_n = 4096
sample_r = 100
similar = np.zeros((vid_n, top_n), dtype = np.int32)
feats = np.zeros((vid_n, feat_n), dtype = np.float32)

valid_vid_n = 0
for i in xrange(vid_n):
	fd = fds[i]
		
	#valid_vid_n += 1
	with open(feat_dir+fd+'/agg_feats','rb') as fp:
		agg_feats = cPickle.load(fp)
		feats[i,:] = agg_feats

#print 'valid videos %s' % valid_vid_n
#feats = feats[:vid_n,:]
for i in xrange(vid_n):
	dist = np.linalg.norm(feats - feats[i,:], axis=1)
	index = np.argsort(dist)
	similar[i,:] = index[1:top_n+1]
for i in xrange(0, vid_n, sample_r):#sample some videos to show nearest neighbours
	if not os.path.exists(sav_dir+fds[i]):
		os.makedirs(sav_dir+fds[i])
		
	shutil.copy(src_dir+fds[i]+'.mp4',sav_dir+fds[i]+'/source.mp4')
	for j in xrange(top_n):
		shutil.copy(src_dir+fds[similar[i,j]]+'.mp4', sav_dir+fds[i]+'/top'+str(j)+'.mp4')



