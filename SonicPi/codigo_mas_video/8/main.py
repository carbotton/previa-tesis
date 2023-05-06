import subprocess

synth = 'piano'
sample = 'bd_pure'
scale = 'a4'

subprocess.run(["python", "callee.py", synth, sample, scale])


"""
Ejemplos rapidos:

    synth:
        chipbass, piano, kalimba, rodeo, pretty_bell 
    
    sample:
        tabla_tas3, bd_pure, elec_chime, elec_bong

"""