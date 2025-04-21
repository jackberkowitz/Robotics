# Phoebe Esser Katz
# April 19, 2025
# Robotics Lab 6: Chess part 1

from interbotix_xs_modules.arm import InterbotixManipulatorXS

import math
import numpy as   np

import sys
import time

def main():
	################### Variables ##################################
	bot = InterbotixManipulatorXS("px100", "arm", "gripper")

	endEffector = math.radians(90) # must be vertical

	elbowToWrist = 100 # mm
	shoulderToElbow = 100 # mm
	shoulderOffset = 35 # mm

	shoulderHyp = math.sqrt(shoulderToElbow**2 + shoulderOffset**2)

	xPositions = {1:102.5, 2:138.5, 3:174.5, 4:210.5} # dictionary w X coordinates
	zFinal = 40 # mm . MIGHT NEED TO CHANGE
	yFinal = 18 # mm. FOR LAB 6

	################## READ in
	if len(sys.argv) > 1:
	  pick_location = int(sys.argv[1])
	  place_location = int(sys.argv[2])
	else:
	  print("Please provide pick and place location numbers between 1 and 4.")

	#translate pick and place locations into coordinates
	xFinal = xPositions[pick_location] # mm

	#### inverse kinematics.
	elbowIK = math.acos(((xFinal**2)+(zFinal**2)-(elbowToWrist**2)-(shoulderHyp**2)) / (2*shoulderHyp*elbowToWrist))

	shoulderIKprime = math.atan(zFinal/xFinal)-math.atan((elbowToWrist*math.sin(elbowIK))/	(shoulderHyp+elbowToWrist*(math.cos(elbowIK) ) ) ) # w hypotenuse
	alpha = math.atan(shoulderOffset/shoulderToElbow) # accounting for offset
	shoulderIK = shoulderIKprime + alpha  #accounting for offset
	#### ADD: pick viable solution (pick solution where shoulder angle is greatest)

	wristIK = endEffector - elbowIK - shoulderIK # bc total will always be vertical

	waistIK = math.atan(xFinal/yFinal) # waist angle can be treated separately

	#### translate coordinate systems (use function)
	#sys.stdout.write("Hello World!")
	
	print("Waist angle: {}".format(waistIK))
	print("Shoulder angle: {}".format(shoulderIK))
	
	print("Elbow angle: {}".format(elbowIK))
	print("Wrist angle: {}".format(wristIK))
	
	time.sleep(100) # 100 s
	#### move robot to pick up location / pick up
	#bot.arm.set_single_joint_position("waist", waistIK)
	#bot.arm.set_single_joint_position("shoulder", shoulderIK)
	#bot.gripper.open()
	#bot.arm.set_single_joint_position("wrist_angle", wristIK)
	#bot.arm.set_single_joint_position("elbow", elbowIK)
	#bot.gripper.close()
    	
	#### move robot to drop off location / drop off

	#### go to sleep
	bot.arm.set_single_joint_position("waist", 0)
	bot.arm.set_single_joint_position("shoulder", -1.88)
	bot.arm.set_single_joint_position("elbow", 1.5)
	bot.arm.set_single_joint_position("wrist_angle", 0.8)

if __name__=='__main__':
    	main()
	
