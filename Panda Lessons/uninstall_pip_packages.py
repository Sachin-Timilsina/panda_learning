import os

packages = os.popen('pip freeze').read().splitlines()

for package in packages:
    os.system(f'pip uninstall -y {package.split("==")[0]}')