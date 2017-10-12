import cozmo


class stop:
    def getName(self):
        return "stop"

    def run(self, robot: cozmo.robot.Robot):
        #print("stop")
        return self.getName(), robot