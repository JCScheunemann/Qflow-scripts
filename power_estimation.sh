#!/bin/tcsh -f
. ./sim_vars.sh
./project_vars.sh
./qflow_vars.sh
verbose='false'
aflag=''
bflag=''
files=''

while getopts 'abf:v' flag; do
  case "${flag}" in
    a) aflag='true' ;;
    b) bflag='true' ;;
    f) files="${OPTARG}" ;;
    v) verbose='true' ;;
    *) error "Unexpected option ${flag}" ;;
  esac
done

  
echo $aflag
echo $flag
echo $files
echo $(addspacers_options)