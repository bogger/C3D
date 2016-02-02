import os
from sklearn.cluster import KMeans
import cPickle
import numpy as np
#src_dir = '/media/researchshare/linjie/data/snapchat/video/'
feat_dir = '/media/researchshare/linjie/data/snapchat/features/c3d/'
fds = os.listdir(feat_dir)
vid_n = len(fds)
feat_n = 4096
sample_r = 100
feats_all = np.zeros((vid_n,feat_n),dtype=np.float32)
for i, fd in enumerate(fds):
	with open (feat_dir+fd+'/agg_feats','rb') as fb:
		feats = cPickle.load(fb)
	feats_all[i,:]= feats
model = KMeans(n_clusters=10, n_init=5, max_iter=200, n_jobs=5)
y_pred = model.fit_predict(feats_all)
labels={}
for i,fd in enumerate(fds):
	labels[fd] = y_pred[i]
with open('kmeans_label','wb') as fb:
	cPickle.dump(labels,fb)

