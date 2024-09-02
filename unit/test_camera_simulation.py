import unittest
import numpy as np
from camera_simulation import simulate_camera

class TestCameraSimulation(unittest.TestCase):

    def test_image_size(self):
        image_height = 480
        image_width = 640
        image = simulate_camera(image_height=image_height, image_width=image_width)
        self.assertEqual(image.shape, (image_height, image_width, 3))

    def test_pixel_value_range(self):
        image = simulate_camera()
        self.assertTrue(np.all(image >= 0))
        self.assertTrue(np.all(image <= 255))

if __name__ == "__main__":
    unittest.main()
