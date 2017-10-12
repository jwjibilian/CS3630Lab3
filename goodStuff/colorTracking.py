import asyncio
import cozmo
from cozmo.util import degrees, time
from find_cube import find_cube
import numpy as np

YELLOW_LOWER = np.array([71, 158, 158])
YELLOW_UPPER = np.array([130, 210, 255])

class colorTracking:
    def getName(self):
        return "colorTrack"

    def run(self, robot: cozmo.robot.Robot):
        robot.set_head_angle(degrees(-5)).wait_for_completed()
        robot.move_lift(-5)

        while True:
            event = robot.world.wait_for(cozmo.camera.EvtNewRawCameraImage, timeout=30)
            if event.image is not None:
                image = np.asarray(event.image)

                cube = None

                try:
                    cube = find_cube(image, YELLOW_LOWER, YELLOW_UPPER)
                    print(cube)
                    # time.sleep(1)
                except asyncio.TimeoutError:
                    print("Cube not found")

                if cube:
                    if cube.pose.position.x < 85:
                        robot.drive_wheels(0,0)
                    else:
                        robot.drive_wheels(50,50)
                        time.sleep(0.25)
                robot.drive_wheels(0,0)
                time.sleep(1)
                # action.wait_for_completed()
                # return "stop", robot