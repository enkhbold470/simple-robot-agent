#!/usr/bin/env python3
"""
Simple demonstration of the Robot Agent capabilities.
"""

import sys
import os
import time

# Add parent directory to the path so we can import robot_agent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from robot_agent import RobotAgent

def main():
    """Main function to demonstrate robot capabilities."""
    print("Starting Simple Robot Agent Demo")
    print("--------------------------------")
    
    # Create a new robot
    robot = RobotAgent("DemoBot")
    
    # Add sensors
    robot.add_sensor("front_sensor", "ultrasonic", {"max_range": 300})
    robot.add_sensor("left_sensor", "infrared", {"max_range": 100})
    robot.add_sensor("right_sensor", "infrared", {"max_range": 100})
    robot.add_sensor("temp_sensor", "temperature")
    
    # Add actuators
    robot.add_actuator("left_motor", "dc_motor", {"max_speed": 100})
    robot.add_actuator("right_motor", "dc_motor", {"max_speed": 100})
    robot.add_actuator("gripper", "servo", {"min_angle": 0, "max_angle": 180})
    
    # Create a custom task executor
    def execute_custom_task(task_name):
        """Execute custom tasks based on the task name."""
        if task_name == "forward_then_scan":
            print("\nExecuting custom task: forward_then_scan")
            robot.move(10)
            print("Reading sensors after moving forward...")
            front_dist = robot.read_sensor("front_sensor")
            print(f"Front distance: {front_dist:.2f} units")
            return True
        
        elif task_name == "rotate_and_grab":
            print("\nExecuting custom task: rotate_and_grab")
            robot.rotate(90)
            print("Robot rotated 90 degrees")
            print("Activating gripper...")
            robot.set_actuator("gripper", "close")
            time.sleep(1)  # Simulate closing time
            return True
            
        elif task_name == "spin_in_place":
            print("\nExecuting custom task: spin_in_place")
            for angle in [90, 90, 90, 90]:  # 4 x 90 = 360 degrees
                robot.rotate(angle)
                time.sleep(0.5)
            print("Completed full spin")
            return True
            
        return False  # Task not recognized
    
    # Override the execute_next_task method to handle custom tasks
    original_execute = robot.execute_next_task
    
    def custom_execute():
        """Custom task execution that extends the default behavior."""
        if not robot.tasks:
            return False
            
        task = robot.tasks[0]
        if execute_custom_task(task):
            robot.tasks.pop(0)  # Remove the task we just executed
            return True
        else:
            # If not a custom task, use the original execution
            return original_execute()
            
    # Replace the method with our custom implementation
    robot.execute_next_task = custom_execute
    
    # Add tasks to the queue
    robot.add_task("forward_then_scan")
    robot.add_task("rotate_and_grab")
    robot.add_task("spin_in_place")
    
    # Run the robot
    print("\nStarting robot tasks...")
    robot.run()
    
    print("\nDemo completed successfully!")

if __name__ == "__main__":
    main()