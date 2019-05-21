import cv2, os
import numpy as np
import matplotlib.image as mpimg


IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS = 480, 640, 3
INPUT_SHAPE = (IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS)


def load_image(data_dir, image_file):
    """
    Load RGB images from a file
    """
    # print(type(image_file))
    # print(data_dir)
    return mpimg.imread(data_dir)

def batch_generator(data_dir, image_paths, steering_angles, batch_size, is_training):
    """
    Generate training image give image paths and associated steering angles
    """
    images = np.empty([batch_size, IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS])
    steers = np.empty(batch_size)
    while True:
        i = 0
        for index in np.random.permutation(image_paths.shape[0]):
            center = image_paths[index]
            steering_angle = steering_angles[index]
            print(center)
            # exit()
            image = load_image(data_dir, center) 

            # add the image and steering angle to the batch
            images[i] =  cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
            steers[i] = steering_angle
            i += 1
            if i == batch_size:
                break
        yield images, steers


