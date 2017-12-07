import nester

cast = ["Palin", "Cleese", "Idle", "Jones", "Gilliam", "Chapman"]
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michalel", "John", "Terry", "Eric", "Jones"]]]

with open('print_lol.txt','w') as man_file:
	
    nester.print_lol(movies, indent=1, level=1, fh=man_file)
