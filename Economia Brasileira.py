n = int(raw_input())
votos = list(map(int,raw_input().split()))
q = (n/2)+1
if votos.count(0) >= q:
	print "Y"
else:
	print "N"
