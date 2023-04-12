import sys

#add the freqs class here


#myfreqs = freqs()

for line in sys.stdin:
   lline = line.lower().replace(',','') #replace commas
   lline = lline.replace('.','') #replace full stops
   lline = lline.replace('"','') #replace quotes
   lline = lline.replace('“','') #replace stylish quotes
   lline = lline.replace('!','')
   lline = lline.replace('?','')
   lline = lline.replace("'s",'')
   lline = lline.replace("\n",'')
   #split to words
   words = lline.split(" ")
   if "" in words:
       words.remove("")
   for w in words:
       print(w)
       #myfreqs.add_to_wordfr(w)

#myfreqs.print_res()
