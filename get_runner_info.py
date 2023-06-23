import subprocess
import sys

print("Fetching system inforamtion.")
system_info = subprocess.check_output("uname -a", shell=True)
xcode_version = subprocess.check_output("xcodebuild -version")
softwareupdate_history = subprocess.check_output("softwareupdate --history")
runner_information = subprocess.check_output("system_profiler SPSoftwareDataType SPHardwareDataType")

print("Kernel/System information:")
print(system_info)
print("Xcode version:")
print(xcode_version)
print("Software Update hsitory")
print(softwareupdate_history)
print("HW information")
print(runner_information)

print("Writing to logfile.")
log = open(sys.argv[1], "w")
log.write("Kernel/System information:\n")
log.write(system_info)
log.write("Xcode version:\n")
log.write(xcode_version)
log.write("Software Update history:\n")
log.write(softwareupdate_history)
log.write("HW information:\n")
log.write(runner_information)
log.close()

print("Done.")