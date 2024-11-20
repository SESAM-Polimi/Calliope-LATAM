import calliope
# import cal_graph as gg
try:
    calliope.set_log_level('Error')
except:
    calliope.set_log_verbosity('Error')

model = calliope.Model('model.yaml')
model.run(force_rerun=True)
