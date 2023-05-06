import subprocess

synth = 'rodeo'
sample = 'tabla_tas3'
scale = 'a4'
synth_options = 'amp: 1, release: 2'

subprocess.run(["python", "callee.py", synth, sample, scale, synth_options])
