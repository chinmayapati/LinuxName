import os,pwd,subprocess,sys

name = raw_input("Enter new PC name: ")

### Variables Setup
user = pwd.getpwuid( os.getuid() )[0]
home = "/home/"+ user

### File System I/O
fs = open( home + "/desktop1.po", 'w')
fs.write('msgid "Ubuntu Desktop"\nmsgstr "' + name + '"')
fs.close()

### Translation
os.chdir("/usr/share/locale/en/LC_MESSAGES/")
subprocess.call( ("sudo msgfmt -o unity.mo " + home + "/desktop1.po").split() )


print "You must Login again to bring changes into effect."
print "Make sure you save all your active works before logging out."
res = raw_input("Logout? (y/n) ")

### Final Work
try:
    if res in "y yes".split():
        cmd = "sudo pkill -KILL -u " + user
        subprocess.call( cmd.split() )
    else:
        exit(0)
except SystemError:
    print "System Error Occurred"
    print "mailto: chinmaya.cp@gmail.com"
finally:
    exit(0)