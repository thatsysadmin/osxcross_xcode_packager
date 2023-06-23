#!/bin/zsh
echo "Kernel / System info:"
uname -a
echo "Xcode version:"
xcodebuild -verson
echo "Runner HW information:"
system_profiler SPSoftwareDataType SPHardwareDataType
echo "Done."