import numpy as np
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, ResNet50
from keras.applications.imagenet_utils import decode_predictions


def parepare_your_input_image():
    img = image.load_img("data/dog.png", target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_expanded = np.expand_dims(img_array, axis=0)
    img_ready = preprocess_input(img_expanded)
    return img_ready


def use_a_real_world_example(img_ready):
    # Instantiate a ResNet50 model with 'imagenet' weights
    model = ResNet50(weights="imagenet")
    # Predict with ResNet50 on your already processed img
    preds = model.predict(img_ready)
    # Decode the first 3 predictions
    print('Predicted:', decode_predictions(preds, top=3)[0])


if __name__ == "__main__":
    img_ready = parepare_your_input_image()
    use_a_real_world_example(img_ready)
