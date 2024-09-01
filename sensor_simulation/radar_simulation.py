import numpy as np

def simulate_radar(num_objects=10, max_distance=200.0, max_velocity=50.0):
    """
    Simulate radar data for `num_objects` with random distances, velocities, and angles.
    Returns arrays for distances, velocities, and angles.
    """
    distances = np.random.uniform(1.0, max_distance, num_objects)
    velocities = np.random.uniform(-max_velocity, max_velocity, num_objects)
    angles = np.random.uniform(-np.pi/4, np.pi/4, num_objects)
    return distances, velocities, angles

def print_radar_data(distances, velocities, angles):
    """
    Print the radar data in a formatted way.
    """
    print("Simulated Radar Data:")
    print(f"{'Distance (m)':>15} {'Velocity (m/s)':>20} {'Angle (rad)':>15}")
    print("-" * 50)
    for d, v, a in zip(distances, velocities, angles):
        print(f"{d:>15.2f} {v:>20.2f} {a:>15.2f}")

if __name__ == "__main__":
    num_objects = 10
    max_distance = 200.0
    max_velocity = 50.0
    
    distances, velocities, angles = simulate_radar(num_objects, max_distance, max_velocity)
    print_radar_data(distances, velocities, angles)
