import unittest
import numpy as np
from radar_simulation import simulate_radar

class TestRadarSimulation(unittest.TestCase):

    def test_num_objects(self):
        num_objects = 10
        distances, velocities, angles = simulate_radar(num_objects=num_objects)
        self.assertEqual(len(distances), num_objects)
        self.assertEqual(len(velocities), num_objects)
        self.assertEqual(len(angles), num_objects)

    def test_distance_range(self):
        max_distance = 200.0
        distances, _, _ = simulate_radar(max_distance=max_distance)
        self.assertTrue(np.all(distances >= 1.0))
        self.assertTrue(np.all(distances <= max_distance))

    def test_velocity_range(self):
        max_velocity = 50.0
        _, velocities, _ = simulate_radar(max_velocity=max_velocity)
        self.assertTrue(np.all(velocities >= -max_velocity))
        self.assertTrue(np.all(velocities <= max_velocity))

    def test_angle_range(self):
        _, _, angles = simulate_radar()
        self.assertTrue(np.all(angles >= -np.pi/4))
        self.assertTrue(np.all(angles <= np.pi/4))

if __name__ == "__main__":
    unittest.main()
