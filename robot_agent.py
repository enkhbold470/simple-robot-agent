#!/usr/bin/env python3

class RobotAgent:
    """Simple robot agent with basic capabilities"""
    
    def __init__(self, name="SimpleBot"):
        self.name = name
        self.position = (0, 0)  # (x, y) position
        self.orientation = 0  # degrees, 0 is facing east/right
        self.sensors = {}
        self.actuators = {}
        self.tasks = []
        self.state = "idle"
        print(f"Robot '{self.name}' initialized.")
    
    def add_sensor(self, name, sensor_type, config=None):
        """Add a sensor to the robot"""
        self.sensors[name] = {
            "type": sensor_type,
            "config": config or {},
            "data": None
        }
        print(f"Sensor '{name}' of type '{sensor_type}' added.")
    
    def add_actuator(self, name, actuator_type, config=None):
        """Add an actuator to the robot"""
        self.actuators[name] = {
            "type": actuator_type,
            "config": config or {},
            "state": "idle"
        }
        print(f"Actuator '{name}' of type '{actuator_type}' added.")
    
    def read_sensor(self, name):
        """Read data from a sensor"""
        if name not in self.sensors:
            raise ValueError(f"Sensor '{name}' not found.")
        
        # In a real implementation, this would communicate with hardware
        # For now, we simulate random sensor data
        import random
        self.sensors[name]["data"] = random.random()
        return self.sensors[name]["data"]
    
    def set_actuator(self, name, state):
        """Set state of an actuator"""
        if name not in self.actuators:
            raise ValueError(f"Actuator '{name}' not found.")
        
        # In a real implementation, this would communicate with hardware
        self.actuators[name]["state"] = state
        print(f"Actuator '{name}' set to state '{state}'.")
    
    def move(self, distance):
        """Move the robot forward by a distance"""
        import math
        # Calculate new position based on orientation
        rad = math.radians(self.orientation)
        dx = distance * math.cos(rad)
        dy = distance * math.sin(rad)
        
        self.position = (self.position[0] + dx, self.position[1] + dy)
        print(f"Robot moved to position {self.position}.")
    
    def rotate(self, angle):
        """Rotate the robot by an angle in degrees"""
        self.orientation = (self.orientation + angle) % 360
        print(f"Robot rotated to {self.orientation} degrees.")
    
    def add_task(self, task):
        """Add a task to the robot's task queue"""
        self.tasks.append(task)
        print(f"Task added. Queue now has {len(self.tasks)} tasks.")
    
    def execute_next_task(self):
        """Execute the next task in the queue"""
        if not self.tasks:
            print("No tasks in queue.")
            return False
        
        task = self.tasks.pop(0)
        self.state = "executing"
        print(f"Executing task: {task}")
        
        # In a real implementation, this would interpret and execute the task
        # For now, we just simulate task execution
        import time
        time.sleep(1)  # Simulate task execution time
        
        self.state = "idle"
        print(f"Task completed. {len(self.tasks)} tasks remaining.")
        return True
    
    def run(self):
        """Run the robot's main control loop"""
        print(f"Robot '{self.name}' starting...")
        try:
            while self.tasks:
                self.execute_next_task()
            print("All tasks completed.")
        except KeyboardInterrupt:
            print("\nRobot operation interrupted.")
        finally:
            print(f"Robot '{self.name}' shutting down.")


# Example usage
if __name__ == "__main__":
    # Initialize robot
    robot = RobotAgent("ExampleBot")
    
    # Add components
    robot.add_sensor("front_distance", "ultrasonic", {"max_range": 400})
    robot.add_sensor("temperature", "thermometer")
    robot.add_actuator("left_motor", "dc_motor", {"max_speed": 100})
    robot.add_actuator("right_motor", "dc_motor", {"max_speed": 100})
    
    # Add tasks
    robot.add_task("move_forward_10")
    robot.add_task("turn_right_90")
    robot.add_task("move_forward_5")
    
    # Run the robot
    robot.run()