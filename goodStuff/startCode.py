import asyncio
import sys
import cv2
import numpy as np
import cozmo
import time
import os

from cozmo.util import degrees, distance_mm, Speed, radians

from generalSearch import generalSearch
from statemachine import StateMachine
from stop import stop
from colorTracking import colorTracking

def run(robot: cozmo.robot.Robot):

    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled = True
    robot.camera.enable_auto_exposure = True

    FSM = StateMachine()
    gSearch = generalSearch()
    stopState = stop()
    # FSM.setStartState(gSearch)
    cTrack = colorTracking()
    FSM.setStartState(gSearch)
    FSM.addState(gSearch) #todo: after gSearch, go to cTrack state
    FSM.addState(stopState)
    FSM.addState(cTrack)
    FSM.run(robot)

if __name__ == '__main__':
    cozmo.run_program(run, use_viewer = True, force_viewer_on_top = True)