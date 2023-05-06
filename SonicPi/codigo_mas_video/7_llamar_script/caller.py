import subprocess

synth = 'rodeo'
sample = 'tabla_tas3'
scale = 'a4'

subprocess.run(["python", "callee.py", synth, sample, scale])
