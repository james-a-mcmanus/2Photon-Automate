import Experiment_parameters as exp
import mss
f = open(exp.path+'index.html','w')
with mss.mss() as sct:
	filename = sct.shot(output=exp.path+'screenshot.png')
    
