import os
import sys
import functools

def simple_test(x):
  print (os.name)
  if os.name == "nt":
    status=os.system("Win64\\Release\\" + x +".exe")
    print(status)
    if (status != 0):
      sys.exit(status)

def simple_test2(x, args, y):
  print (os.name)
  if os.name == "nt":
    status=os.system("Win64\\Release\\" + x +".exe" + " " + args + " < test_inputs\\" + y)
    print(status)
    if (status != 0):
      sys.exit(status)

def simple_test3(x, y, args, args2, args3):
  print (os.name)
  if os.name == "nt":
    status=os.system("Win64\\Release\\" + x +".exe" + " < " + args + " > " + args2)
    print(status)
    if (status != 0):
      sys.exit(status)
    cmd = "Win64\\Release\\" + y +".exe" + " " + args2 + " "+ args3
    print(cmd)
    status=os.system(cmd)
    print(status)
    if (status != 0):
      sys.exit(status)

def simple_test4(x, args, args2, args3):
  print (os.name)
  if os.name == "nt":
    cmd = "Win64\\Release\\" + x +".exe" + " < " + args + " > " + args2
    print(cmd)
    status=os.system(cmd)
    print(status)
    if (status != 0):
      sys.exit(status)
    with open(args2) as a2:
      a2txt = [a for a in a2.readlines()]
    with open(args3) as a3:
      a3txt = [a for a in a3.readlines()]
    ok = len(a2txt) == len(a3txt)
    ok = functools.reduce(lambda a, b: a and b, zip(a2txt, a3txt), ok)
    if not(ok):
      print("texts differ")
      sys.exit(1)
    # TODO compare args2/args3
    #cmd = "Win64\\Release\\" + y +".exe" + " " + args2 + " "+ args3
    #print(cmd)
    #status=os.system(cmd)
    #print(status)
    #if (status != 0):
    #  print("sys.exit(status)")
	  
BOUND_TESTS=["basicLinear2.pwqp",
        "basicLinear.pwqp",
        "basicTestParameterPosNeg.pwqp",
        "basicTest.pwqp",
        "devos.pwqp",
        "equality1.pwqp",
        "equality2.pwqp",
        "equality3.pwqp",
        "equality4.pwqp",
        "equality5.pwqp",
        "faddeev.pwqp",
        "linearExample.pwqp",
        "neg.pwqp",
        "philippe3vars3pars.pwqp",
        "philippe3vars.pwqp",
        "philippeNeg.pwqp",
        "philippePolynomialCoeff1P.pwqp",
        "philippePolynomialCoeff.pwqp",
        "philippe.pwqp",
        "product.pwqp",
        "split.pwqp",
        "test3Deg3Var.pwqp",
        "toplas.pwqp",
        "unexpanded.pwqp"]

PIP_TESTS=["boulet.pip",
        "brisebarre.pip",
        "cg1.pip",
        "esced.pip",
        "ex2.pip",
        "ex.pip",
        "exist.pip",
        "exist2.pip",
        "fimmel.pip",
        "max.pip",
        "negative.pip",
        "seghir-vd.pip",
        "small.pip",
        "sor1d.pip",
        "square.pip",
        "sven.pip",
        "tobi.pip"]

for k in PIP_TESTS:
    simple_test2("islpip", "--format=set --context=gbr -T", k)
    simple_test2("islpip", "--format=set --context=lexmin -T", k)
    simple_test2("islpip", "--format=affine --context=gbr -T", k)
    simple_test2("islpip", "--format=affine --context=lexmin -T", k)

CODEGEN_TESTS = [f for f in os.listdir(os.path.join("test_inputs", "codegen")) 
    if os.path.isfile(os.path.join("test_inputs", "codegen", f))
    and f.endswith(".st")] + [os.path.join("cloog", f) for f in os.listdir(os.path.join("test_inputs", "codegen", "cloog")) 
    if os.path.isfile(os.path.join("test_inputs", "codegen", "cloog", f))
    and f.endswith(".st")]

CODEGEN_TESTS2 = [f for f in os.listdir(os.path.join("test_inputs", "codegen")) 
    if os.path.isfile(os.path.join("test_inputs", "codegen", f))
    and f.endswith(".in")] + [os.path.join("omega", f) for f in os.listdir(os.path.join("test_inputs", "codegen", "omega")) 
    if os.path.isfile(os.path.join("test_inputs", "codegen", "omega", f))
    and f.endswith(".in")] + [os.path.join("pldi2012", f) for f in os.listdir(os.path.join("test_inputs", "codegen", "pldi2012")) 
    if os.path.isfile(os.path.join("test_inputs", "codegen", "pldi2012", f))
    and f.endswith(".in")] 

for k in CODEGEN_TESTS:
    simple_test4("islcodegen", 
        os.path.join("test_inputs", "codegen", k), 
        os.path.join("test_inputs", "codegen", k + "-test.c").replace(".st", ".c"),
        os.path.join("test_inputs", "codegen", k).replace(".st", ".c"))

for k in CODEGEN_TESTS2:
    simple_test4("islcodegen", 
        os.path.join("test_inputs", "codegen", k), 
        os.path.join("test_inputs", "codegen", k + "-test.c").replace(".in", ".c"),
        os.path.join("test_inputs", "codegen", k).replace(".in", ".c"))

FLOW_TESTS = [f for f in os.listdir(os.path.join("test_inputs", "flow")) 
    if os.path.isfile(os.path.join("test_inputs", "flow", f))
    and f.endswith(".ai")]

for k in FLOW_TESTS:
    simple_test3("islflow", "islflowcmp", 
        os.path.join("test_inputs", "flow", k), 
        os.path.join("test_inputs", "flow", "test-" + k).replace(".ai", ".flow"),
        os.path.join("test_inputs", "flow", k).replace(".ai", ".flow"))

SCHEDULE_TESTS = [f for f in os.listdir(os.path.join("test_inputs", "schedule")) 
	if os.path.isfile(os.path.join("test_inputs", "schedule", f))
	and f.endswith(".sc")]

for k in SCHEDULE_TESTS:
    simple_test3("islschedule", "islschedulecmp", 
	    os.path.join("test_inputs", "schedule", k), 
	    os.path.join("test_inputs", "schedule", "test-" + k).replace(".sc", ".st"),
		os.path.join("test_inputs", "schedule", k).replace(".sc", ".st"))

simple_test("isltest")
simple_test("isltestimath")
simple_test("isltestint")
for k in BOUND_TESTS:
    simple_test2("islbound", "-T --bound=bernstein", k)
    simple_test2("islbound", "-T --bound=range", k)
