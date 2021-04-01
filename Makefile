# This makefile should run the lab and generate all the necessary
# outputs.
#
# Changes to this file will not be propogated to the server.

default: code.out

# Anything list here will be deleted with `make clean`
CLEANUP=*.out

# Standard rules for a bunch of stuff, including compiling, cleaning,
# testing, etc.  In particular, it knows how to make code.exe from
# code.cpp by compiling in main.cpp
#
# All the inputs are copied into the build/ directory.  By default,
# they are copied from ./, but setting LAB_SUBMISSION_DIR will cause
# them to be copied from there.  runlab sets
# LAB_SUBMISSION_DIR=solution to run the solution.
include $(ARCHLAB_ROOT)/cse141.make

# Here you can define your own options that students can set in
# config.env that will translate into more complex configurations
# without giving them full control.
# For instance, you could let them choose a compiler and set CC, CXX,
# and LD appropriately.

ifeq ($(salutation),short)
SALUTATION=hi
endif
ifeq ($(salutation),long)
SALUTATION=hello
endif
ifeq ($(salutation),formal)
SALUTATION=greetings
endif

export SALUTATION

# CMD_LINE_ARGS gets passed to the executable built from their
# code. Libarchlab gets the first crack at parsing the command line,
# so these configure what performance counters to look for.
ifeq ($(DEVEL_MODE),yes)
        # DEVEL_MODE is set to yes, when they run their code locally.
        # This means that libarchlab can't access the performance
        # counters, so you shouldn't ask for any or their executabel
        # won't run.
	CMD_LINE_ARGS=--stat runtime=ARCHLAB_WALL_TIME $(EXTRA_OPTIONS)
else
        # This is what gets run on the server.
	CMD_LINE_ARGS=--stat-set default.cfg $(EXTRA_OPTIONS)
endif

