from metrics import *
from keras.models import load_model
import keras
import numpy as np
import math
def predict(data):
    model = load_model(r'files/an_metaphor_lstm.h5',
                    custom_objects={
                        'loss': keras.losses.CategoricalCrossentropy(),
                        'f1': f1,
                        'precision': precision,
                        'recall': recall
                    })
    x_input = np.array(data) #transformed
    float_predictions = model.predict(x_input)
    labeled_data = []
    for i in range(len(float_predictions)):
        prediction = float_predictions[i]
        #probabilidad de ser no ser metáfora, probabilidad de serlo
        label = (prediction[0], prediction[1],'No es metáfora: {:.2%} de probabilidad'.format(prediction[0][0]), 'Es metáfora: {:.2%} de probabilidad:'.format(prediction[1][0]))#(prediction[1], prediction[0], abs(prediction[0]), abs(prediction[0])+prediction[1])
        labeled_data.append((i, label))
    return labeled_data
