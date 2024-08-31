# autonomous-driving-simulation-suite
This project is designed to simulate various driving scenarios using industry-standard formats such as OpenScenario and OpenDrive. It aims to validate and test autonomous driving algorithms under different conditions, ensuring safety and reliability before deployment in real-world environments.

# Key Features
  1. Scenario Library: A collection of predefined scenarios including urban intersections, highway merges, and emergency braking.
  2. Road Network Modeling: Custom road environments using OpenDrive, covering city streets, highways, and rural roads.
  3. Sensor Data Simulation: Integration of Open Simulation Interface (OSI) to simulate LIDAR, radar, and camera data.
  4. Automated Testing: Python scripts to automate simulation runs, collect performance metrics, and generate reports.
  5. Visualization and Reporting: A web-based dashboard for visualizing results, scenario replays, and detailed performance reports.
# Technologies Used
  Python: Core scripting language for automation and analysis.\
  CARLA or LGSVL: Simulation platforms for running the scenarios.\
  OpenScenario: creating and defining driving scenarios.\
  OpenDrive: For modeling road networks.\
  Open Simulation Interface (OSI): For simulating sensor data.\
  Flask/Django: developing the dashboard.\
  Matplotlib/Plotly: For data visualization.
# Installation Instructions
## Prerequisites
  Python 3.x\
  CARLA or LGSVL Simulator installed\
  pip (Python package installer)\
  Git (for cloning the repository)
## Step 1: Clone the Repository
`git clone https://github.com/mehrdad89/autonomous-driving-simulation-suite.git`\
`cd autonomous-driving-simulation-suite`

## Step 2: Install Dependencies
`pip install -r requirements.txt`
## Step 3: Set Up the Simulation Environment
Install and set up your chosen simulation platform (CARLA or LGSVL).\
Follow the platform’s documentation to ensure it’s correctly configured.
## Step 4: Run a Sample Scenario
`python scripts/run_simulation.py --scenario scenarios/urban_intersection.xosc --network road_networks/city_streets.xodr`
# How to Use the Suite
### Running a Simulation
To run a specific scenario, use the run_simulation.py script with the appropriate scenario and road network files:

`python scripts/run_simulation.py --scenario <path_to_xosc> --network <path_to_xodr>`
### Analyzing Results
After the simulation, use the analyze_results.py script to analyze the performance metrics:
`python scripts/analyze_results.py --simulation_output <output_file>`
### Generating Reports
Generate detailed performance reports with:
`python scripts/generate_report.py --results <results_file> --output <report_file>`
### Dashboard Visualization
Start the dashboard to visualize the results:
`python scripts/dashboard.py`\
Navigate to `http://localhost:5000` in your browser to interact with the simulation results.

# Contributing
Contributions are welcome! If you have suggestions for new features or improvements, feel free to fork the repository and submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.

# Acknowledgments
Special thanks to the developers of CARLA, LGSVL, and the communities behind OpenScenario, OpenDrive, and OSI for providing the tools and standards that made this project possible.
