import numpy as np
from skimage import io
from skimage.feature import hog
from skimage import data, exposure
from pdf2image import convert_from_path
import matplotlib.pyplot as plt

class Map:
    def __init__(self, path_file):
        #self.image = io.imread(path_file)
        pages = convert_from_path(path_file)
        for page in pages:
            page.save('outmapita.jpg', 'JPEG')
        #page.save('out.jpg', 'JPEG')

    def map_gradiente(self):
        image = io.imread('out.jpg')

        fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                            cells_per_block=(1, 1), visualize=True, multichannel=True)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

        ax1.axis('off')
        ax1.imshow(image, cmap=plt.cm.gray)
        ax1.set_title('Input image')

        # Rescale histogram for better display
        hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

        ax2.axis('off')
        ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
        ax2.set_title('Histogram of Oriented Gradients')
        plt.show()
