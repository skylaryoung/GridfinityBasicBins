from openscad_runner import OpenScadRunner
osr = OpenScadRunner("gridfinity-rebuilt-bin-generator.scad", "examples/2x2.stl")
osr.run()
for line in osr.echos:
    print(line)
for line in osr.warnings:
    print(line)
for line in osr.errors:
    print(line)
if osr.good():
    print("Successfully created example.stl")