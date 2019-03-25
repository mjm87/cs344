from keras.datasets import boston_housing
(train_images, train_labels), (test_images, test_labels) = boston_housing.load_data()


print(
        'training images \
            \n\tcount: {len(train_images)} \
            \n\tdimensions: ' + str(train_images.ndim) + ' \
            \n\tshape: ' + str(train_images.shape) + ' \
            \n\tdata type: ' + str(train_images.dtype) + '\n\n',
        'testing images \
            \n\tcount: ' + str(len(test_labels)) + ' \
            \n\tdimensions: ' + str(train_labels.ndim) + ' \
            \n\tshape: ' + str(test_labels.shape) + ' \
            \n\tdata type: ' + str(test_labels.dtype) + ' \
            \n\tvalues: ' + str(test_labels) + '\n',
    )
