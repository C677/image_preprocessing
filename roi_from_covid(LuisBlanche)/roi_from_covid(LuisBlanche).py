from keras.models import load_model
import numpy as np
import os, glob
from skimage.io import imread
from skimage.transform import pyramid_reduce, resize
import matplotlib.image as image

IMG_SIZE = 256

src_root_ct = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\CT_COVID\\'
save_path = 'C:\\Users\\hyoj_\\OneDrive\\Desktop\\internship\\C677\\covid\\roi_lung2\\'

def read_png(filepath):
    scans = []
    for file in os.listdir(filepath):
        if (file.find('.png') is not -1):
            img = imread(filepath + file)
            img = resize(img, output_shape=(IMG_SIZE, IMG_SIZE, 1), preserve_range=True)
            scans.append(img)
    np.save('dataset.npy', scans)

model=load_model('lung_model.hdf5')
read_png(src_root_ct)
ct_scans = np.load('dataset.npy')
preds = model.predict(ct_scans)

for i, pred in enumerate(preds):
    image.imsave(os.path.join(save_path, str(i) + '.png'), pred.squeeze(), cmap='gray')