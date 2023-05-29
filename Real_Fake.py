from tensorflow.keras.models import Model, load_model
model=load_model("C:/Users/Dell/Desktop/generated_code/completed_augmented_trained_model.h5")
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from keras.preprocessing import image
from keras.models import load_model


def predict(model, img):
    """Run model prediction on image
    Args:
        model: keras model
        img: PIL format image
    Returns:
        list of predicted labels and their probabilities 
    """
    x = image.img_to_array(img)
    x = x - np.min(x)
    x = x/np.max(x)
    #--
    x = np.expand_dims(x, axis=0)
    #x = preprocess_input(x)
    
    preds = model.predict(x)
    return preds[0]


def plot_preds(img, preds):
    """Displays image and the top-n predicted probabilities in a bar graph
    Args:
        preds: list of predicted labels and their probabilities
    """
    labels = ("fake", "real")
    gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1])
    plt.figure(figsize=(8,8))
    plt.subplot(gs[0])
    plt.imshow(np.asarray(img))
    plt.subplot(gs[1])
    plt.barh([0, 1], preds, alpha=0.5)
    plt.yticks([0, 1], labels)
    plt.xlabel('Probability')
    plt.xlim(0, 1)
    plt.tight_layout()

file = open("file.txt","r+")
path = file.read()    
img = image.load_img(path, target_size=(224, 224))
preds = predict(model, img)

activities = ['fake', 'real']
slices = [1-preds[0],preds[0]]
colors = ['r', 'b']
plt.pie(slices, labels = activities, colors=colors,
        startangle=90, shadow = True, explode = (0, 0),
        radius = 1, autopct = '%1.1f%%')
plt.show()



