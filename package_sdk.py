import subprocess
import sys

workspace = sys.argv[1] + "/workroot"

print("Cloning osxcross")
osx_clone_result = subprocess.check_output("git clone https://github.com/tpoechtrager/osxcross.git", cwd=workspace, shell=True).decode()
print(osx_clone_result)

print("Packaging Xcode SDK")
sdk_package_result = subprocess.check_call("./osxcross/tools/gen_sdk_package.sh", cwd=workspace, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)
# print(sdk_package_result)

print("Moving SDK.")
print(subprocess.check_output("ls -a", cwd=workspace, shell=True).decode())
subprocess.check_output("mv *.sdk.tar.xz", cwd=workspace, shell=True)

print("Done.")
exit(0)
