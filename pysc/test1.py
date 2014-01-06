import pysc

@pysc.on("end_of_elaboration")
def do_elab(phase):
    print "Elab"
    print pysc.gc.readDict()

@pysc.on("start_of_initialization")
@pysc.on("end_of_initialization")
@pysc.on("start_of_elaboration")
@pysc.on("start_of_simulation")
@pysc.on("end_of_simulation")
@pysc.on("start_of_evaluation")
@pysc.on("end_of_evaluation")
def do_phase(phase):
    print "Phase", phase

print "Start"

