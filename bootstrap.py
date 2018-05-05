#!/usr/bin/env python
import subprocess, os
# Check if Ansible installation - install if not 
print("Checking Ansible installation")
apt_list = subprocess.Popen(['apt', 'list', '--installed'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
try:
    grep_apt = subprocess.check_output(['grep', '-i', 'ansible/'], stdin=apt_list.stdout)
    print("- Ansible already installed!")
except:
    print("- Ansible not found - installing ...")
    print("- apt-get update")
    os.system('sudo apt-get update > /dev/null')
    print("- apt-get install")
    os.system('sudo apt-get install {} -y > /dev/null'.format(packages))
    print("- Ansible installed!")