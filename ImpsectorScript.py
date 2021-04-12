# this is an example script to put into impsector, it runs 2 stimuli and then saves them.

import lvbt
import os
import imp
os.chdir(r"C:\Users\james\OneDrive\Sheffield\Building\Manipulator\Stimulus_Control")
stim = imp.load_source('Stimulus', 'Stimulus.py')

prepFolder = "D:\\JDoggyDog\\TEST2\\"
if not os.path.isdir(prepFolder):
	os.mkdir(prepFolder)

port = stim.port

# Setup a white screen.
whitescreen = stim.StimulusParameters()
whitescreen.filename = "whitescreen.mat"
whitescreen.savevideo = "1"
whitescreen.externaltrigger = "1"
whitescreen.repeatstim = "1"

# Setup a grating
grating = stim.StimulusParameters()
grating.filename = "Grating_2x1000y4000t1v20w.mat"
grating.savevideo = "0"

# setup imspector measurement
m = lvbt.measurement("Measurement 1")

# run a stimulus, export it and save it. (this could be functionalised)
recordingDir, basename = stim.generate_recording_folder(prepFolder)
whitescreen.setup()
whitescreen.trigger()
m.run()
m.export(recordingDir, basename)
whitescreen.save(recordingFolder + basename + "_stimulus.txt")
whitescreen.reset()

# run a second stimulus
recordingDir, basename = stim.generate_recording_folder(prepFolder)
grating.setup()
grating.trigger()
m.run()
m.export(recordingDir, basename)
grating.save(recordingFolder + basename + "_stimulus.txt")
grating.reset()

port.close()