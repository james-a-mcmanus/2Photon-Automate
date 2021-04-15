# this is an example script to put into impsector, it runs 2 stimuli and then saves them.

import lvbt
import os
import imp
import datetime
import time
import numpy as np
import random
os.chdir(r"C:\Users\lvbt\Documents\GitHub\2Photon-Automate")
stim = imp.load_source('Stimulus', 'Stimulus.py')

prepFolder = "C:\\Users\\lvbt\\Documents\\Auto Keiv\\"
if not os.path.isdir(prepFolder):
	os.mkdir(prepFolder)

port = stim.Port()

# setup imspector measurement
m = lvbt.measurement("Measurement 1")

# run a stimulus, export it and save it. (this could be functionalised)
def bars(speed):
    if speed>2:
        return 80,2
    else:
        return 100,5
resol = 22.5
n_angles = int(360/resol)
angle  = np.arange(n_angles)*resol
speed = [2,3]
speeds = np.asarray([])
angles = np.asarray([])
for s in speed:
    speeds = np.concatenate((speeds,s*np.ones(n_angles)))
    angles = np.concatenate((angles,angle))
speeds = speeds.astype(int)
angles = angles.astype(int)
indexes = np.arange(len(speed)*n_angles)
random.shuffle(indexes)
for speed,angle in zip(speeds[indexes][:2],angles[indexes][:2]):
    a0,a1 = bars(speed)
    dgrating = stim.StimulusParameters()
    dgrating.filename = str(a0)+"to"+str(a1)+"algrating"+str(speed)+"_noise5.mat"
    dgrating.savevideo = "1"
    dgrating.externaltrigger = "1"
    dgrating.repeatstim = "0"
    dgrating.framelength = str(speed)
    dgrating.angle = str(angle)
    dt = datetime.datetime.now().strftime('%y%m%d%H%M%S')
    recordingFolder, basename = stim.generate_recording_folder(prepFolder,dt)
    dgrating.setup(port)
    dgrating.trigger(port)
    m.run()
    m.export(recordingFolder, basename)
    dgrating.save(port,recordingFolder + basename + "_stimulus.txt",dt = dt)
dgrating.reset(port)
dgrating.quit(port)
'''
# run a second stimulus
dt = datetime.datetime.now().strftime('%y%m%d%H%M%S')
recordingDir, basename = stim.generate_recording_folder(prepFolder,dt)
grating.setup()
grating.trigger()
m.run()
m.export(recordingDir, basename)
grating.save(recordingFolder + basename + "_stimulus.txt", dt = dt)
grating.reset()
'''
port.close()