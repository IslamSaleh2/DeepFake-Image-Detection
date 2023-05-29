from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import warnings
from keras.preprocessing import image
from keras.models import load_model
warnings.filterwarnings("ignore")

'''
importing BusterNetCore and pretrained_busterNet to create testing model
'''
from BusterNetCore import create_BusterNet_testing_model
busterNetModel = create_BusterNet_testing_model("C:/Users/Dell/Desktop/generated_code/pretrained_busterNet.hd5")

#Reading single image
#file = open("file1.txt","r+")
#path = file.read()  
#real = mpimg.imread(path)

file = open("file.txt","r+")
path = file.read()    
real = image.load_img(path, target_size=(512, 512))


#Expand the dimesion of the image to predict copy-move regions 
X = np.expand_dims(real, axis=0)

# Z : image of predicted regions
Z = busterNetModel.predict(X, verbose=1)

#show the original image
imgplot = plt.imshow(X[0])
plt.show()

#show the detedcted image
imgplot = plt.imshow(Z[0])
plt.show()
