# Simple Robot Agent

A simple implementation of a robot agent with modular sensor and actuator support.

## Features

- Modular sensor and actuator support
- Task queue for sequential operation
- Position and orientation tracking
- Simple movement and rotation capabilities
- Extensible architecture for additional functionalities

## Getting Started

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone the repository:
```
git clone https://github.com/enkhbold470/simple-robot-agent.git
cd simple-robot-agent
```

2. Install the required packages:
```
pip install -r requirements.txt
```

### Usage

Run the example robot:

```python
python robot_agent.py
```

Create your own robot by importing the `RobotAgent` class:

```python
from robot_agent import RobotAgent

# Initialize robot
my_robot = RobotAgent("MyBot")

# Add components
my_robot.add_sensor("front_sensor", "ultrasonic")
my_robot.add_actuator("main_motor", "servo")

# Add tasks
my_robot.add_task("move_forward")
my_robot.add_task("check_surroundings")

# Run the robot
my_robot.run()
```

## Documentation

For comprehensive documentation, visit our [Robot Wiki](https://enkhbold470.github.io/simple-robot-agent/wiki/).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project provides a basic framework for robot control and can be expanded for various applications
- For real hardware implementation, additional libraries for specific sensors and actuators would be required