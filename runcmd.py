import subprocess

process = subprocess.Popen(['hostname','-I'],stdout=subprocess.PIPE, shell=True)

# p = subprocess.Popen(['date'], stdout=subprocess.PIPE)
print(process.communicate()[0].decode('utf-8'))
