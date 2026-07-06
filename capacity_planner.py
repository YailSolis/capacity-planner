# // is for whole numbers and divides as well 
# % is the spaces left over 
#/ this is just for division 

#  input() always hands back a string even when I type numbers, and int() crashes with a ValueError on junk like "thirty" — so this file checks before converting, like a toll road
server = input("how much ram is in here(GB)?")
clean= server.strip()
if clean.isdigit(): # Input must prove it's a number before passing; otherwise the program crashes with a ValueError
    server_ram= int(clean) # this is where the int goes ealier it put it on line 4 and messed up everything. 
    if server_ram > 0  and server_ram < 24000:
        print(f"the  server has {server_ram}gb")
    # this 2nd input exists after you give a number to the first input if its not a number then this line never runs
        vm_server = input("how much ram does one vm need(gb)?")
        clean= vm_server.strip()
        if clean.isdigit()  : # this is the 2nd gate if and its like a toll road pay befor you go 
            vm_ram= int(clean)
            # this is 24000 because a vm has a cap and the vm cap has to match the server cap or zero vms would fit .
            if vm_ram > 0 and vm_ram < 24000:
                print(f"this is your new ram {vm_ram}gb")
                vms_that_fit = server_ram // vm_ram
                leftover = server_ram % vm_ram
                # we had to make the pennies from an float because it comes out slightly wrong to a intger because that will give us the exact number 
                vm_cost_pennies = 1460 
                total_pennies= vms_that_fit * vm_cost_pennies
                print("=== Provisioning Report ====") # remember that the first block is 13 count the characters and subtract if needed. 
                print(f"Server RAM:   {server_ram:>10}gb")
                print(f"VM size:     {vm_ram:>10}gb")
                print(f"VMs that fit:{vms_that_fit:>10}")
                print(f"Leftover RAM:{leftover:>10}gb")
                # this is where the pennies becomes dollars. 
                print(f"Monthly cost: ${total_pennies/100:>10.2f}")
            

           
            else:
                print("a vm cant be 0gb, the vm must be between 1gb and 24000gb") 

        else:
                print("This is not a number i know you like the number") # this is the first else if you type anything but a number
    else:
         print("a server cant be 0gb the server must be between 1gb and 24000gb ")
                   
                   
else:
    print("thats not gonna work here champ")
           



