# orbithangar-installer
A python script to install Orbiter addons and its dependencies found in orbithangar.com
Just paste the addon's url and it will download+extract the addon and also all the other orbithangar addons mentioned in its decription page. This process repeats recursively.     


Limitations : 
1) Only orbithangar addon urls are currently supported. If an addon dependency is not hosted on orbithangar, you still have to download/install that dependency manually.
2) Some addons may have special installation steps (modifying a config file for example), which this script can't do. 
3) Other edge cases (an addon is mentioned in the description but that's not actually a dependency.    

