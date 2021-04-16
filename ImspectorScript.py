# this is an example script to put into impsector, it runs 2 stimuli and then saves them.

import lvbt
import os
import imp
import datetime
import time
import numpy as np
import random

def bars(speed):
    if speed>2:
        return 80,2
    else:
        return 100,5

os.chdir(r"C:\Users\lvbt\Documents\GitHub\2Photon-Automate")
stim = imp.load_source('Stimulus', 'Stimulus.py')
exp = imp.load_source('Experiment_parameters', 'Experiment_parameters.py')

prepFolder = exp.prepFolder
random_angles_path = exp.prepFolder+'random_angles.csv'
if not os.path.isdir(prepFolder):
	os.mkdir(prepFolder)

port = stim.Port()

# setup imspector measurement
m = lvbt.measurement("Measurement 1")
# run a stimulus, export it and save it. (this could be functionalised)

angles,speeds = np.loadtxt(random_angles_path).astype(int)

for speed,angle in zip(speeds,angles):
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
    try:
        dgrating.setup(port)
        dgrating.trigger(port)
        #port.close()
        start = time.time()
        m.run()
        if time.time()-start<exp.rec_time_limit:
            break
        #port.open()
        m.export(recordingFolder, basename)
        dgrating.save(port,recordingFolder + basename + "_stimulus.txt",dt = dt)
    except:
        break
dgrating.reset(port)
dgrating.quit(port)
port.close()