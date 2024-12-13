"""pusher_controller controller."""
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

piston_linear_motor = robot.getDevice('Slider_y_plus')
piston_linear_motor.setPosition(0)
piston_linear_motor.setVelocity(0.0)

piston_linear_motor1 = robot.getDevice('Slider_x_minus')
piston_linear_motor1.setPosition(0)
piston_linear_motor1.setVelocity(0.0)

piston_linear_motor2 = robot.getDevice('Slider_z_plus')
piston_linear_motor2.setPosition(0)
piston_linear_motor2.setVelocity(0.0)

def delay(seconds):
    steps = int(seconds * 1000 / timestep)  # Convert seconds to steps
    for _ in range(steps):
        if robot.step(timestep) == -1:
            break  # Exit if simulation stops

while robot.step(timestep) != -1:

    piston_linear_motor.setVelocity(1)
    piston_linear_motor.setPosition(0.032)
    
    # piston_linear_motor1.setVelocity(0.1)
    # piston_linear_motor1.setPosition(0.032)
    
    # piston_linear_motor2.setVelocity(0.1)
    # piston_linear_motor2.setPosition(0.032)
    delay(0.5)
    piston_linear_motor.setPosition(0)
    # piston_linear_motor1.setPosition(0)
    # piston_linear_motor2.setPosition(0)
    delay(0.5)

    pass

