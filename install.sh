#!/bin/bash

# USER INPUTS
CMSSW_release=CMSSW_12_2_0
CMSSW_release_name=    #Leave this blank if you don't know what it is.  It's just a marker in case you have multiple identical directories. No need for the underscore.
SCRAM_ARCH_name="amd64_gcc900" # Leave slc6/7 out

MACHINESPECS="$(uname -a)"
echo "Machine specifics: ${MACHINESPECS}"
declare -i FOUND_EL6=0
if [[ "${MACHINESPECS}" == *"el6"* ]]; then
  FOUND_EL6=1
else
  for evar in $(env); do
    if [[ "$evar" == *"SINGULARITY_IMAGE_HUMAN"* ]]; then
      # This means you are running in a condor job with a singularity image loaded.
      if [[ "$evar" == *"rhel6"* ]] || [[ "$evar" == *"slc6"* ]]; then
        FOUND_EL6=1
      fi
    fi
  done
fi

if [[ ${FOUND_EL6} -eq 1 ]]; then
  SCRAM_ARCH_name="slc6_${SCRAM_ARCH_name}"
else
  SCRAM_ARCH_name="slc7_${SCRAM_ARCH_name}"
fi

export SCRAM_ARCH=${SCRAM_ARCH_name}

if [[ -z ${CMSSW_release_name+x} ]]; then
  CMSSW_release_name="${CMSSW_release}"
else
  CMSSW_release_name="${CMSSW_release}_${CMSSW_release_name}"
fi

#--Here there be dragons----
export CMS_PATH=/cvmfs/cms.cern.ch
source /cvmfs/cms.cern.ch/cmsset_default.sh
scramv1 p -n ${CMSSW_release_name} CMSSW $CMSSW_release
cd ${CMSSW_release_name}/src
eval $(scramv1 runtime -sh)

# new upstream-only ignores user's cmssw, but makes cms-init much, much faster
git cms-init --upstream-only

#######################################
# No CMSSW packages beyond this point #
#######################################

# Loading LHC Computing Grid software stack release 103cuda. More stable/applicable than CMSSW. https://lcginfo.cern.ch/
#source /cvmfs/sft.cern.ch/lcg/views/LCG_103cuda/x86_64-centos7-gcc11-opt/setup.sh

# HexUtils
git clone https://github.com/lk11235/HexUtils.git

./HexUtils/JHUGenMELA/MELA/setup.sh
eval $(./HexUtils/JHUGenMELA/MELA/setup.sh env standalone)

# MELA Analytics
#git clone git@github.com:MELALabs/MelaAnalytics.git

scram b -j 16

# see comment in patchesToSource.sh
rm $CMSSW_BASE/lib/$SCRAM_ARCH/.poisonededmplugincache
