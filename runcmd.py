import subprocess
try:
    process = subprocess.Popen(['hostname -I'],stdout=subprocess.PIPE, shell=True)


    ipaddr = process.communicate()[0].decode('utf-8','ignore')
    print(ipaddr.strip())
    
except:
    print("fail")
