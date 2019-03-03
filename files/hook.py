from time import sleep
import uiautomation as automation
import discord

if __name__ == '__main__':
    # sleep function designed to hook the omnibox URL
    sleep(3)
    control = automation.GetFocusedControl()
    controlList = []
    while control:
        controlList.insert(0, control)
        control = control.GetParentControl()
    if len(controlList) == 1:
        control = controlList[0]
    else:
        control = controlList[1]
    address_control = automation.FindControl(control, lambda c, d: isinstance(c,
                                                                              automation.EditControl) and "Address and search bar" in c.Name)
    URL = address_control.CurrentValue()
    # split the URL into a readable format
    sep = '/'
    split_URL = URL.split(sep, 1)[0]
    print(split_URL)

#find a suitable way of injecting into Discord
async def change_status(self):
    await client.change_presence(discord.Game(name=split_URL))
