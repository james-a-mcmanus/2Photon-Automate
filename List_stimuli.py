import Stimulus
import Experiment_parameters as exp
import Generate

import numpy as np

def bars(speed,reverse):
    if speed>2:
        if reverse:
            return 2,80
        else:
            return 80,2
    else:
        if reverse:
            return 5,100
        else:
            return 100,5
def dyna_gratings(speed,noise=True,reverse = False,generate_angle_file=True,file_index = 0):
    stim_list = []
    random_angles_path = exp.prepFolder+'random_angles.csv'
    if generate_angle_file:
        Generate.generate_angles(speed,random_angles_path,n_angles = 16)        
    angles,speeds = np.loadtxt(random_angles_path)[:,file_index:].astype(int)
    for speed,angle in zip(speeds,angles):
        a0,a1 = bars(speed,reverse)
        dgrating = Stimulus.StimulusParameters()
        dgrating.filename = str(a0)+"to"+str(a1)+"algrating"+str(speed)+noise*'_noise5'+".mat"
        dgrating.savevideo = "1"
        dgrating.externaltrigger = "1"
        dgrating.repeatstim = "0"
        dgrating.framelength = str(speed)
        dgrating.angle = str(angle)
        stim_list.append(dgrating)
    return stim_list

def rf_bars():
    stim_list = []
    rf_bar = Stimulus.StimulusParameters()
    rf_bar.filename = '50movc0bar5.mat'
    rf_bar.savevideo = "1"
    rf_bar.externaltrigger = "1"
    rf_bar.repeatstim = "0"
    rf_bar.framelength = "5"
    
    rf_bar.angle = "90"
    stim_list.append(rf_bar)
    rf_bar.angle = "0"
    stim_list.append(rf_bar)
    return stim_list
    
def repeat_stim(name,framelength,angle,n):
    stim_list = []
    stim = Stimulus.StimulusParameters()
    stim.filename = name
    stim.savevideo = "1"
    stim.externaltrigger = "1"
    stim.repeatstim = "0"
    stim.framelength = framelength
    stim.angle = angle
    stim_list = [stim]*n
    return stim_list    

def algratings(speeds,thicks,repeat):
    stim_list = []
    for i in range(repeat):
        for speed in speeds:
            for thick in thicks:
                grating = Stimulus.StimulusParameters()
                grating.filename = str(thick)+"algrating"+str(speed)+".mat"
                grating.savevideo = "1"
                grating.externaltrigger = "1"
                grating.repeatstim = "0"
                grating.framelength = str(speed)
                grating.thick = "0"
                stim_list.append(grating)
    return stim_list
