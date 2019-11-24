from sys import argv
from os.path import exists

script, d_txt, a_txt = argv        #input the name of the text
                                   #the first.txt have information and the second will be "copy"

print("Copying from %s to %s" % (d_txt,a_txt))  #Print the phrase

#Open the text and read
i_f = open(d_txt)
in_f = i_f.read()       #copy the information (read and save the information)

print("The input is %d bytes long" % len(d_txt))    #Print how many bytes are

print("Does the output file exist? %r" % exists(a_txt))   #so if exists the second text (if you write the name)
print("Hit RETURN to continue.")                          #Select an option
print("If not, hit CTRL-C to abort.")
input()

o_f = open(a_txt, 'w')             #open the archive
o_f.write(in_f)                    #write the text how a copy

print("Alright, all done")

#close everywhere
o_f.close()
i_f.close()
