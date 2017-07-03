#!/usr/bin/tcsh
#-------------------------------------------
# qflow exec script for project /home/lsd/Work/Qflow-scripts
#-------------------------------------------

/usr/lib/qflow/scripts/synthesize.sh /home/lsd/Work/Qflow-scripts mux
/usr/lib/qflow/scripts/placement.sh -d /home/lsd/Work/Qflow-scripts mux
/usr/lib/qflow/scripts/vesta.sh /home/lsd/Work/Qflow-scripts mux
/usr/lib/qflow/scripts/router.sh /home/lsd/Work/Qflow-scripts mux
/usr/lib/qflow/scripts/placement.sh -f -d /home/lsd/Work/Qflow-scripts mux
/usr/lib/qflow/scripts/router.sh /home/lsd/Work/Qflow-scripts mux $status
/usr/lib/qflow/scripts/cleanup.sh /home/lsd/Work/Qflow-scripts mux
/usr/lib/qflow/scripts/display.sh /home/lsd/Work/Qflow-scripts mux
