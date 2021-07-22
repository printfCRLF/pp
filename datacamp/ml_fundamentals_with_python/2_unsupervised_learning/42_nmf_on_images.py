import data
from matplotlib import pyplot as plt
from sklearn.decomposition import NMF
from sklearn.decomposition import PCA


def explore_led_digits_dataset(samples):
    # Select the 0th row: digit
    digit = samples[0, ]

    # Print digit
    print(digit)

    # Reshape digit to a 13x8 array: bitmap
    bitmap = digit.reshape(13, 8)

    # Print bitmap
    print(bitmap)

    # Use plt.imshow to display bitmap
    plt.imshow(bitmap, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()


def show_as_image(sample):
    bitmap = sample.reshape((13, 8))
    plt.figure()
    plt.imshow(bitmap, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()


def nmf_learns_part_of_images(samples):
    # Create an NMF model: model
    model = NMF(n_components=7)
    # Apply fit_transform to samples: features
    features = model.fit_transform(samples)
    # Call show_as_image on each component
    for component in model.components_:
        show_as_image(component)

    # Assign the 0th row of features: digit_features
    digit_features = features[0]
    # Print digit_features
    print(digit_features)


def pca_does_not_learn_parts(samples):
    # Create a PCA instance: model
    model = PCA(n_components=7)
    # Apply fit_transform to samples: features
    features = model.fit_transform(samples)
    # Call show_as_image on each component
    for component in model.components_:
        show_as_image(component)


digits = data.load_lcd_digits()
explore_led_digits_dataset(digits)
nmf_learns_part_of_images(digits)
# pca_does_not_learn_parts(digits)
