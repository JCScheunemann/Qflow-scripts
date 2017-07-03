#!/bin/tcsh -f
#------------------------------------------------------------
# project variables for project /home/jcscheunemann/Work/VLSI/Qflow
#------------------------------------------------------------

# Synthesis command options:
# -------------------------------------------
# set yosys_options = 
# set yosys_script = 
# set yosys_debug = 
# set abc_script = 
# set nobuffers = 
# set nofanout = 
# set fanout_options = 
set addspacers_options = "-stripe 5 100 PG -nostretch"

# Placement command options:
# -------------------------------------------
# set initial_density = 
# set graywolf_options = 

# Router command options:
# -------------------------------------------
# set route_layers = 
# set via_stacks = 
# set qrouter_options = 

# Minimum operating period of the clock (in ps)
 set vesta_options = "--period 3E2"

#------------------------------------------------------------

