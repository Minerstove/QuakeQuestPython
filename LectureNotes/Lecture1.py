#Puzzle 1

# Assign values to variables There are correct values for these, look at the puzzle! 
name = "Rudolph"
kind = "reeindeer"
nose = "red"
quality = "glows"

# Print the puzzle with the correct values
print(f" My name is {name}. I'm a {kind}, and I have a very {nose} nose. If you ever saw it, you'd say it {quality}")
print(f"""If you take the 1st letter of my name, the 2nd letter of what I am,
and the last letter of this very word, you'll find that my favorite color is {name[0] + kind[1] + "d"}.""")

"""
# Puzzle 2
# KE =(1/2)*m*v**2
# change_in_KE = energy required to increase speed
"""
# KE =(1/2)*m*v**2
# change_in_KE = energy required to increase speed

m = 20000
v1 = 20
v2 = 100

# write code here
KE1 = (1/2)*m*v1**2
KE2 = (1/2)*m*v2**2
change_in_KE = KE2-KE1
change_in_KE = change_in_KE/1000
print(f"Amount of energy required: {change_in_KE} kilojoules")

# write code here
kj_per_liter = 38290
fuel_required = change_in_KE/kj_per_liter
print(f"Amount of fuel required: {fuel_required:.2f} liters")

# write code here
cost_per_liter = 60
total_cost = 60*fuel_required
print(f"Total cost: {total_cost:.2f} pesos")

#@title **Solution** to How to find a needle in a haystack?
toolbag  = list('12jasf0FD90ajamdfj[2*(N3nEI)n3nsdfND2-N)n1TjaEKmm#dfj[2*(Nh(FH#:)na[34gwnleafn432gnaplafnawfna;lfgla;fjadpfoajmwonaffagnaeroigjalskj2jaisfoinwe4e2ng]]')
haystack = list('jamdfjkladfsjklb23*naa2-napj-2n[2*(N3nEI)3.adsaf_=13ugnln4n;a;;nag*^TEasdf\0avaknsfND2N)n1Pja12jasf0FDdadf90aEKme#/dfj[2*asdfn1(Nh(FH#:)an9n3+"}|]')
needles = '|./-_'

# find the location of each of the 5 needles in the haystack .index()
n1_loc = haystack.index('|')
n2_loc = haystack.index('.')
n3_loc = haystack.index('/')
n4_loc = haystack.index('-')
n5_loc = haystack.index('_')

# get a tool from the toolbag using the locations of the needles: indexing
tool1 = toolbag[n1_loc]
tool2 = toolbag[n2_loc]
tool3 = toolbag[n3_loc]
tool4 = toolbag[n4_loc]
tool5 = toolbag[n5_loc]

# combine the tools into one mega tool: append
one_mega_tool = []
one_mega_tool.append(tool1)
one_mega_tool.append(tool2)
one_mega_tool.append(tool3)
one_mega_tool.append(tool4)
one_mega_tool.append(tool5)


# insert the secret tool G somewhere into the mega tool
# Might need to correct position of two letters ?
one_mega_tool.insert(3, 'G')
print(one_mega_tool)

# What is the one mega tool?
print('The one mega tool is <type-here>')

# Given a straight staircase
staircase = {
    'num_of_steps' : 22,
    'step_height': 0.15, # in meters
}

# Declare a dictionary for Paul with a
# volume of 0.075 cubic meter and same density as water: 998 kg/m^3
# -- start of code
paul = {
    'volume' : 0.075,
    'density' : 998
}
# -- end of code

# Calculate the height from the ground to the top of the staircase
# and add this item to the dictionary

# -- start of code
staircase['top_height'] = staircase['num_of_steps']*staircase['step_height']
# -- end of code
print(f"Height: {staircase['top_height']:.2f} meters")

# Calculate how heavy Paul is, and add this item to the dictionary
# -- start of code
paul['mass'] = paul['volume']*paul['density']
# -- end of code
print(f"Mass: {paul['mass']:.2f} kg")

# If we push Paul off the top of the staircase,
# how many seconds will it take for him to reach the floor?
# Note y = y_0 + v_0*t + 0.5*a*t**2
# -- start of code
t = (2*staircase['top_height']/9.8)**(1/2)
# -- end of code
print(f"Freefall time: {t:.3f} sec")

# What if we only want to print the time every two seconds?
# Use the previous timer code to write a timer that only prints every 2 seconds


numbers = [1,2,3,4,5,6,7,8,9,10]
sqrd_numbers = []
for i in numbers:
  square = i**2
  sqrd_numbers.append(square)
print(sqrd_numbers)

