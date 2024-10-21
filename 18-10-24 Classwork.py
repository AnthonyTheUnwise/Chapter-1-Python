"""
Anthony ;D
Testing how to test stuff lol
"""
Radius = float(input("Enter radius:"))
while Radius < 0:
    Radius = float(input("Invalid Input, Enter radius:"))
Volume = (4/3)*3.14*Radius**3
Volume = round(Volume, 2)
print("The volume is:", Volume)

#ID #Description             #Test data   #Expected  #Actual  #Passed
#   #                        #            #Result    #Result  #Y/N
#####################################################################
#1  #Regular data            # r = 6      #904.32    #904.319 # N
#2  #Irregularly large       # r = 4096   #287,705M  #287B... # Y
#3  #Irregularly small       # r = 0.0027 #0.0x7 824 #8.2406  # N
#4  #Negative                # r = -2     #3RR0R     #-33.493 # N
#5  #Decimal                 # r = 2.7    #82.40616  #82.4061 # Y
#6  #Nothing                 # r = 0      #0         #0       # Y
#7  #Text                    # r = hi     #3RR0R     #3RR0R   # Y

#ID #Description             #Test data   #Expected  #Actual  #Passed
#   #                        #            #Result    #Result  #Y/N
#####################################################################
#1  #Regular data            # r = 6      #904.32    #904.32  # Y
#2  #Irregularly large       # r = 4096   #287,705M  #287B... # Y
#3  #Irregularly small       # r = 0.0027 #0.0x7 824 #0.0     # N
#4  #Negative                # r = -2     #3RR0R     #3RR0R   # Y
#5  #Decimal                 # r = 2.7    #82.40616  #82.4061 # Y
#6  #Nothing                 # r = 0      #0         #0       # Y
#7  #Text                    # r = hi     #3RR0R     #3RR0R   # Y