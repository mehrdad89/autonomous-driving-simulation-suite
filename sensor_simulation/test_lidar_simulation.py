import unittest
import numpy as np
from lidar_simulation import simulate_lidar

class TestLidarSimulation(unittest.TestCase):

    def test_num_points(self):
        num_points = 360
        angles, distances = simulate_lidar(num_points=num_points)
        self.assertEqual(len(angles), num_points)
        self.assertEqual(len(distances), num_points)

    def test_distance_range(self):
        num_points = 360
        max_distance = 100.0
        _, distances = simulate_lidar(num_points=num_points, max_distance=max_distance)
        self.assertTrue(np.all(distances >= 1.0))
        self.assertTrue(np.all(distances <= max_distance))

    def test_angles_range(self):
        num_points = 360
        angles, _ = simulate_lidar(num_points=num_points)
        self.assertTrue(np.all(angles >= 0))
        self.assertTrue(np.all(angles <= 2 * np.pi))

if __name__ == "__main__":
    unittest.main()
