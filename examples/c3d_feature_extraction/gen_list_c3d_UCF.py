import os
import sys
import glob
im_dir = '/media/researchshare/linjie/data/UCF-101_images/'
out_dir = '/media/researchshare/linjie/data/UCF-101_features/c3d/'
fds = os.listdir(im_dir)
#out_dir = 'output/c3d/'
frm_size = 16
stage=sys.argv[1]
list_path = '/home/a-linjieyang/work/video_caption/ucfTrainTestlist/%slist01.txt' % stage
sav_name='prototxt/UCF_list_frm_%s.txt' % stage
prefix_name='prototxt/UCF_list_prefix_%s.txt' % stage
list_file = open(sav_name,'w')
prefix_file = open(prefix_name,'w')
with open(list_path,'r') as f:
	for line in f:
		content = line.split()
		vid_fd = content[0][:-4]
		if len(content)==1:
			label=0
		else:
			label= int(content[1])-1
		images = os.listdir(im_dir+vid_fd)
	
		n_im = len(images)
		for i in xrange(1,n_im-frm_size+2,frm_size):
			list_file.write('%s%s/ %d %d\n' %  (im_dir, vid_fd, i, label))
			prefix_file.write('%s%s/%06d\n' % (out_dir, vid_fd, i))
		if not os.path.exists(out_dir + vid_fd):
			os.makedirs(out_dir + vid_fd)
list_file.close()
prefix_file.close()
