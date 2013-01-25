"""

based on an input of t, prop, shell, fire determines how many times a cannon can be fired
t = length of time for firing
prop = amount of time needed to reload propellant
shell = amount of time needed to reload shell
fire = amount of time needed to fire before gun can be reloaded

prop and shell occur simultaneously
no queue for shell and propellant
can only fire if shell and propellant are present
gun can't reload until fire time, but process begins in shell/prop once fire begins


en.wikipedia.org/wiki/File:Animated_gun_turret.gif
    - animation of the process

Kyle E. Aungst
01/25/13
"""
estimated_power_of_orgasm = 4
#ejaculation_input= raw_input("Please enter 4 non-negative rational reals delimited by ' '\n")
dick_stats = ejaculation_input.split()

#calculated using standard ((L*D)+(W/G))/(A^2)
adjusted_penis_size = str((10**-estimated_power_of_orgasm) * max(
                            float(dick_stats[1])*(10**estimated_power_of_orgasm),
                            float(dick_stats[2])*(10**estimated_power_of_orgasm),
                            float(dick_stats[3])*(10**estimated_power_of_orgasm)))

estimated_confidence_booster = len(adjusted_penis_size) - str(adjusted_penis_size).find('.')
adjusted_penis_size = int(str(adjusted_penis_size).replace('.', ""))
estimated_premature_ejaculation_rate = int(dick_stats[0].replace('.', ""))

#know it doesn't fit, I just like the imagery in my head of pity, tears
pity, tears = divmod(estimated_premature_ejaculation_rate, adjusted_penis_size) 
estimated_number_of_premature_ejaculations = int(float(str(pity)+str(tears))*(10**-estimated_confidence_booster))

print "It took %s attempts before you gave up. Keep pluggin lil soldier!" % (estimated_number_of_premature_ejaculations)

                                                                    
                            
