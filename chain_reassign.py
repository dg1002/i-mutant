with open("1dvf.pdb", 'r') as a:
    text = a.readlines()
new_text = []
for line in text:
    if len(line) > 3:
        if line[21] == "D":
            new_text.append("%sA%s"%(line[0:21],line[22:]))
        elif line[21] == "C":
            new_text.append("{0}A{1:>4}{2}".format(line[0:21], str(int(line[22:26].strip())+1000), line[27:]) )
        else:
            new_text.append(line)
    else:
        new_text.append(line)
with open("1dvf_new.pdb", 'w') as b:
    b.write("".join(new_text))


#with open("1bj1.pdb", 'r') as a:
#    text = a.readlines()
#new_text = []
#for line in text:
#    if len(line) > 3:
#        if line[21] == "V":
#            new_text.append("%sA%s"%(line[0:21],line[22:]))
#        elif line[21] == "W":
#            new_text.append("{0}A{1:>4}{2}".format(line[0:21], str(int(line[22:26].strip())+1000), line[27:]) )
#        else:
#            new_text.append(line)
#    else:
#        new_text.append(line)
#with open("1bj1_new.pdb", 'w') as b:
#    b.write("".join(new_text))
