import os

def sh(command):
	os.system(command)

def run():
	sh("git clone https://github.com/blubrackets/pilot")
	sh("cd pilot")
	sh("python3 setup.py install")
	print("All done!")

if __name__ == '__main__':
	run()
