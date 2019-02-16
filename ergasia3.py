#python 2.7.15

arxeio = open("comments.py","r") #anoigw to arxeio se read mode
lines = arxeio.readlines() #apothikevw tis grammes se metavlhth
arxeio.close() #kleinw to arxeio

print "Onoma arxeiou: comments.py xwris sxolia"
for line in lines:
	if "#" in line:
		#elegxei an arxizei apo #
		l = line.strip()
		if l[0]!="#":
			#xwrizei th grammh se list items me vash to #
			tmp=line.split("#")
			#metraei posa ' kai " yparxoun prin
			count1 = tmp[0].count("'")
			count2 = tmp[0].count('"')
			
			if count1%2==1 or count2%2==1:
				print line
			else:
				print line.split("#")[0]
	else:
		print line
