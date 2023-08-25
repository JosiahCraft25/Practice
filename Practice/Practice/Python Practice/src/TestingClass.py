from time import sleep

#jc = Employee('josiah', 'craft', '11/17/2000', 'sd')

class Employee:
    is18 = 0
    active = 1
    payroll_hrs = 0
    
    def __init__(self,fname, lname, dob, title):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.title = title
    
    def over18(self):
        input("is user over 18? (y/n)")
        
        if ('y'):
            self.is18 = 1
        else:
            return
        
        
    def worked_shift(self, hours):
        payroll_hrs = self.payroll_hrs
        payroll_hrs += int(hours)
        txt = "........."
        if (payroll_hrs >= 40):
            print("Overtime detected deploying tactical strike drones: ")
            sleep(2)
            for i in txt:
                print(i, end='', flush=True)
                sleep(0.5)
            print("Error, no available drones for strike, please standby...")
            sleep(2)
            print ("""
            JUST KIDDING
                    _____________
                   /           ,.\
                  /           /  \\
            o    /           {    }\
             `.  \ ....       \  / /
               `. \ \\\\       `' /
                 \ \_____________/
                  \      \ \
                   \      \ \
                    \     _\ \________________________
                    (`\  /  \ \ ___         "-._       )
                     \ \/   /`-'  /,       /`-._"-._  /
                      `/    """"""'       /___ _"-._"-._
                      /___ __  _          `-._      '  /
                      \  XR 66-Roadkill       "-._ /  /
                     __\________________________  "  /
                   /    '//,  '//'               )__/
                  /       '///'    ,//'/,       /
                 (.---------------------------./
                  `:.                        //
                    `=======================''
                
            """)
        return