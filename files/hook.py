from time import sleep #import libraries
import uiautomation as automation
import discord #discord library, perhaps doesn't need to be used

if __name__ == '__main__': #hardcode the string
    # sleep function designed to hook the omnibox URL
    sleep(3) #after 3 seconds, if none can be found, kill the script
    control = automation.GetFocusedControl() #hook onto the focused window
    controlList = [] 
    while control: #begin loop
        controlList.insert(0, control) #begin list
        control = control.GetParentControl() #get parent object within the window
    if len(controlList) == 1: #fetch the URL
        control = controlList[0] #begin boolean check 
    else:
        control = controlList[1] # #if parent object is selected
    address_control = automation.FindControl(control, lambda c, d: isinstance(c, #find Chrome elements within the EXE for the omnibox
                                                                              automation.EditControl) and "Address and search bar" in c.Name) #utilise automation library for hooking into the omnibox
    URL = address_control.CurrentValue() #return into a new variable
    # split the URL into a readable format
    sep = '/' #once the / is found within the URL, split from the viewable portion
    split_URL = URL.split(sep, 1)[0] #open into a new variable since strings are immutable, and format into a separation
    print(split_URL) #display output

#find a suitable way of injecting into Discord
async def change_status(self):
    await client.change_presence(discord.Game(name=split_URL))
