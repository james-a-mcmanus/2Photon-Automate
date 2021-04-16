import random
import numpy as np
import sys
import os
import Experiment_parameters as exp
def generate_angles(speed,file_path,n_angles = 16):
    resol = 360/n_angles
    angle  = np.arange(n_angles)*resol
    speeds = np.asarray([])
    angles = np.asarray([])
    for s in speed:
        speeds = np.concatenate((speeds,s*np.ones(n_angles)))
        angles = np.concatenate((angles,angle))
    speeds = speeds.astype(int)
    angles = angles.astype(int)
    indexes = np.arange(len(speed)*n_angles)
    random.shuffle(indexes)
    speeds = speeds[indexes]
    angles = angles[indexes]
    np.savetxt(file_path, np.stack((angles,speeds)))


speed = [2,3]
if not os.path.isdir(exp.prepFolder):
	os.mkdir(exp.prepFolder)
file_path = exp.prepFolder+'random_angles.csv'
generate_angles(speed,file_path,n_angles = 16)
print(np.loadtxt(file_path).astype(int))