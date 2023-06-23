#!/bin/zsh
echo "Kernel / System info:"
uname -a
echo "Xcode version:"
xcodebuild -version
echo "Software Update history"
softwareupdate --history
echo "Runner HW information:"
system_profiler SPSoftwareDataType SPHardwareDataType
echo "Done."