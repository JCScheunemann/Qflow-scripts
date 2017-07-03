#!/bin/tcsh -f
#-------------------------------------------
# qflow exec script for project /home/jcscheunemann/Work/VLSI/Qflow
#-------------------------------------------

/usr/local/share/qflow/scripts/synthesize.sh /home/jcscheunemann/Work/VLSI/Qflow mux || exit 1
/usr/local/share/qflow/scripts/placement.sh -d /home/jcscheunemann/Work/VLSI/Qflow mux || exit 1
/usr/local/share/qflow/scripts/vesta.sh /home/jcscheunemann/Work/VLSI/Qflow mux || exit 1
/usr/local/share/qflow/scripts/router.sh /home/jcscheunemann/Work/VLSI/Qflow mux || exit 1
/usr/local/share/qflow/scripts/placement.sh -f -d /home/jcscheunemann/Work/VLSI/Qflow mux || exit 1
/usr/local/share/qflow/scripts/router.sh /home/jcscheunemann/Work/VLSI/Qflow mux || exit 1 $status
/usr/local/share/qflow/scripts/cleanup.sh /home/jcscheunemann/Work/VLSI/Qflow mux || exit 1
/usr/local/share/qflow/scripts/display.sh /home/jcscheunemann/Work/VLSI/Qflow mux || exit 1
