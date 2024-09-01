import numpy as np
import matplotlib.pyplot as plt

def simulate_camera(image_height=480, image_width=640):
    """
    Simulate a camera image as a random noise image.
    Returns an image array.
    """
    image = np.random.randint(0, 256, (image_height, image_width, 3), dtype=np.uint8)
    return image

def display_image(image):
    """
    Display the simulated camera image.
    """
    plt.imshow(image)
    plt.title('Simulated Camera Image')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    image_height = 480
    image_width = 640
    
    image = simulate_camera(image_height, image_width)
    display_image(image)
