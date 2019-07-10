#!/usr/bin/env python3
import cozmo
import time
import asyncio
import subprocess
import requests
from cozmo.util import degrees, distance_mm, speed_mmps
from observable import Observable

class Robot:

    _robot = None

    @staticmethod
    def drive(mm, webhookJenkins):
        print("Drive")
        _robot.drive_straight(distance_mm(mm), speed_mmps(50)).wait_for_completed()
        # webhook call
        print(webhookJenkins)
        requests.get(webhookJenkins, auth=("dea.noe.leimbacher", "lidop"), verify=False)


    # @staticmethod
    # def speak(text, webhookJenkins):
    #     print("Speak")
    #     _robot.say_text(text).wait_for_completed()
    #     webhook call
    #     print(webhookJenkins)
    #     requests.get(webhookJenkins, auth=("dea.noe.leimbacher", "lidop"), verify=False)

    @staticmethod
    def command1(method, argument):
        print("command1")
        getattr(_robot, method)(argument).wait_for_completed()

    @staticmethod
    def command2(method, argument1, argument2):
        print("command2")
        getattr(_robot, method)(argument1, argument2).wait_for_completed()


    def __init__(self, robot: cozmo.robot.Robot, obs: Observable):
        global _robot
        _robot = robot
        _obs = obs
        obs.on("drive", Robot.drive)
        #obs.on("speak", Robot.speak)
        obs.on("command1", Robot.command1)
        obs.on("command2", Robot.command2)

    def main(self):
        cozmo.logger.info("Press CTRL-C to quit")
        self.get_in_position()
        cozmo.logger.info("RObot: %s", _robot.pose)

        while True:
            print("COZMO is waiting")
            time.sleep(60.0 - time.time() % 60.0)

    def get_in_position(self):
        _robot.set_lift_height(1, in_parallel = True)
        _robot.set_head_angle(degrees(0), in_parallel = True)
        _robot.wait_for_all_actions_completed()
    #    _robot.say_text("Ich bin bereit!").wait_for_completed()