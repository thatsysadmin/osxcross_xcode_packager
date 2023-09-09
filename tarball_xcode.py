import subprocess
import sys

workspace = sys.argv[1] + "/workroot"

print("Tarballing Xcode.")
xcode_tarball_result = subprocess.check_output("tar -czvf Xcode.tar.gz /Applications/Xcode_15.0.app")
print(xcode_tarball_result)
print("Done.")
exit(0)
