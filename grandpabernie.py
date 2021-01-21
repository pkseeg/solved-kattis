from sys import stdin, stdout
lines = stdin.readlines()

trips = dict()
seen = set()

n = int(lines[0])
for i in range(1,n+1):
	place, year = lines[i].split()[0], int(lines[i].split()[1])
	if place not in trips:
		trips[place] = [year]
	else:
		trips[place].append(year)


m = int(lines[n+1])
for i in range(n+2,n+m+2):
	place, y = lines[i].split()[0], int(lines[i].split()[1])
	if place not in seen:
		trips[place].sort()
		seen.add(place)
	stdout.write(str(trips[place][y-1])+'\n')
stdout.flush()
