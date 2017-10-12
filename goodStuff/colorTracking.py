import asyncio
import cozmo
from cozmo.util import degrees, time
from find_cube import find_cube
import numpy as np

YELLOW_LOWER = np.array([79,116,188])
YELLOW_UPPER = np.array([116, 180, 255])
RED_LOWER = np.array([116,116,188])
RED_UPPER = np.array([143, 180, 255])


class colorTracking:
    def getName(self):
        return "colorTrack"

    def run(self, robot: cozmo.robot.Robot):
        robot.set_head_angle(degrees(-15)).wait_for_completed()
        robot.move_lift(-5)
        goLeft = False

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
                    if cube[0] < 170:
                        goLeft = True
                    else:
                        goLeft = False
                    if cube[2] < 0:
                        # robot.drive_wheels(0,0)
                        robot.stop_all_motors()
                    elif cube[0] < 160: #turn left
                        robot.drive_wheels(25, 50)
                        # time.sleep(1)
                    elif cube[0] > 200: #turn right
                        robot.drive_wheels(50, 25)
                        # time.sleep(1)
                    else:
                        robot.drive_wheels(50,50)
                        # time.sleep(1)
                else:
                    if goLeft:
                        robot.drive_wheels(-50,50)
                        # time.sleep(1)
                    else:
                        robot.drive_wheels(50,-50)
                        # time.sleep(1)

                time.sleep(1)
                robot.stop_all_motors()
                # return "stop", robot