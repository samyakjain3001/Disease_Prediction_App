#FOR THE FIRST MODEL
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
model = load_model('models_dir/model111.h5')
model222=load_model("models_dir/my_model.h5")
# call model to predict an image
def api(full_path):
    data = image.load_img(full_path, target_size=(50, 50, 3))
    data = np.expand_dims(data, axis=0)
    data = data * 1.0 / 255

    #with graph.as_default():
    predicted = model.predict(data)
    return predicted
    
#FOR THE SECOND MODEL
def api1(full_path):
    data = image.load_img(full_path, target_size=(64, 64, 3))
    data = np.expand_dims(data, axis=0)
    data = data * 1.0 / 255

    #with graph.as_default():
    predicted = model222.predict(data)
    return predicted