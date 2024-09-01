import numpy as np
import matplotlib.pyplot as plt

def simulate_lidar(num_points=360, max_distance=100.0):
    """
    Simulate a LIDAR scan with `num_points` rays and a maximum distance of `max_distance` meters.
    Returns an array of distances representing LIDAR hits.
    """
    angles = np.linspace(0, 2 * np.pi, num_points)
    distances = np.random.uniform(1.0, max_distance, num_points)
    return angles, distances

def plot_lidar(angles, distances):
    """
    Plot the LIDAR scan data.
    """
    x = distances * np.cos(angles)
    y = distances * np.sin(angles)
    
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, 'o')
    plt.xlim(-max_distance, max_distance)
    plt.ylim(-max_distance, max_distance)
    plt.title('Simulated LIDAR Data')
    plt.xlabel('X [meters]')
    plt.ylabel('Y [meters]')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    num_points = 360
    max_distance = 100.0
    
    angles, distances = simulate_lidar(num_points, max_distance)
    plot_lidar(angles, distances)
