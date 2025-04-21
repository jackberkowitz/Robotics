# Jack Berkowitz
# April 20, 2025
# Robotics Lab 6: Chess part 1

from interbotix_xs_modules.arm import InterbotixManipulatorXS

import numpy as np

import sys

def main():
    bot = InterbotixManipulatorXS("px100", "arm", "gripper")

  #Dictionaries
    waist = {1: -0.1687, 2: -0.1549, 3: -0.0813, 4: -0.095} # dictionary waist coordinates
    shoulder = {1: -0.074, 2: 0.1871, 3: 0.60, 4: 1.067} # dictionary shoulder coordinates
    elbow = {1: 0.615, 2: 0.1764, 3: -0.56, 4: -1.416} #dictionary elbow coordinates
    wrist = {1: 1.02, 2: 1.181, 3: 1.50, 4: 1.808} #dictionary wrist coordinates
    
    waist_inter = {1: -0.1687, 2: -0.1549, 3: -0.1135, 4: -0.096}
    shoulder_inter = {1: -0.256, 2: 0.043, 3: 0.4279, 4: 0.56}
    elbow_inter = {1: 0.1626, 2: -0.1381, 3: -0.785, 4: -0.93}
    wrist_inter = {1: 1.635, 2: 1.644, 3: 1.8653, 4: 1.617}

  ####READ IN
    if len(sys.argv) > 1:
      pick_location = int(sys.argv[1])
      place_location = int(sys.argv[2])
    else:
      print("Please provide pick and place location numbers between 1 and 4.")

  #translate pick and place locations into coordinates
    waistI = waist[pick_location]
    shoulderI = shoulder[pick_location]
    elbowI = elbow[pick_location]
    wristI = wrist[pick_location]
    
    waist_inter_pick = waist_inter[pick_location]
    shoulder_inter_pick = shoulder_inter[pick_location]
    elbow_inter_pick = elbow_inter[pick_location]
    wrist_inter_pick = wrist_inter[pick_location]
    
    waist_inter_place = waist_inter[place_location]
    shoulder_inter_place = shoulder_inter[place_location]
    elbow_inter_place = elbow_inter[place_location]
    wrist_inter_place = wrist_inter[place_location]

    waistF = waist[place_location]
    shoulderF = shoulder[place_location]
    elbowF = elbow[place_location]
    wristF = wrist[place_location]

  #Move Robot to Home
    bot.arm.go_to_home_pose()

  #Move Robot to pick up location / pick up
    bot.gripper.open()
   
    if pick_location == 3 or pick_location == 4:
   	 bot.arm.set_single_joint_position("waist", waistI)
   	 bot.arm.set_single_joint_position("wrist_angle", wristI)
   	 bot.arm.set_single_joint_position("elbow", elbowI)
   	 bot.arm.set_single_joint_position("shoulder", shoulderI)
   	 bot.gripper.close()
    else:
   	 bot.arm.set_single_joint_position("waist", waistI)
   	 bot.arm.set_single_joint_position("shoulder", shoulderI)
   	 bot.arm.set_single_joint_position("wrist_angle", wristI)
   	 bot.arm.set_single_joint_position("elbow", elbowI)
   	 bot.gripper.close()

  #Move Robot to Inter Position (Pick)
    if pick_location == 3 or pick_location == 4 or pick_location == 2:
    	bot.arm.set_single_joint_position("shoulder", shoulder_inter_pick)
    	bot.arm.set_single_joint_position("elbow", elbow_inter_pick)
    	bot.arm.set_single_joint_position("waist", waist_inter_pick)
    else:
    	bot.arm.set_single_joint_position("elbow", elbow_inter_pick)
    	bot.arm.set_single_joint_position("shoulder", shoulder_inter_pick)
    	bot.arm.set_single_joint_position("waist", waist_inter_pick)
    	
  #Move Robot to Inter Position (Place)
    	bot.arm.set_single_joint_position("elbow", elbow_inter_place)
    	bot.arm.set_single_joint_position("shoulder", shoulder_inter_place)
    	bot.arm.set_single_joint_position("waist", waist_inter_place)
   	
  #Move Robot to drop off location / drop off
    if place_location == 3 or place_location == 4:
    	bot.arm.set_single_joint_position("waist", waistF)
    	bot.arm.set_single_joint_position("wrist_angle", wristF)
    	bot.arm.set_single_joint_position("elbow", elbowF)
    	bot.arm.set_single_joint_position("shoulder", shoulderF)
    	bot.gripper.open()
    else:
    	bot.arm.set_single_joint_position("waist", waistF)
    	bot.arm.set_single_joint_position("shoulder", shoulderF)
    	bot.arm.set_single_joint_position("wrist_angle", wristF)
    	bot.arm.set_single_joint_position("elbow", elbowF)
    	bot.gripper.open()

  #Move Robot Back to Home
    #bot.gripper.open()
    if place_location == 3 or place_location == 4:
    	bot.arm.set_single_joint_position("shoulder", 0.45)
    else:
    	bot.arm.set_single_joint_position("shoulder", -0.15)
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()  
    

if __name__=='__main__':
    main()

