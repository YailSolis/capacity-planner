# // is for whole numbers and divides as well 
# % is the spaces left over 
#/ this is just for division 
#  input() always hands back a string even when I type numbers, and int() crashes with a ValueError on junk like "thirty" — so this file checks before converting, like a toll road

def get_valid_ram(question):
    while True:
        answer = input(question)
        clean = answer.strip()
        if clean.isdigit():
            number = int(clean)
            if number > 0 and number < 24000:
                return number
            else:
                print("has to be between 1 and 24000")
        else: 
            print("thats not a nummber champ")
    
running = True
while running: 
    server_ram = get_valid_ram("how much ram is in here(GB)? ")
    vm_ram = get_valid_ram("how much ram does one vm need(gb)? ")
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
                
    answer = input("run again? (y/n) ").strip().lower()
    if answer == "y":
        pass
    elif answer == "n":
        running = False
    else:
        print("no no thats not a y/n")
        running = False 

           



