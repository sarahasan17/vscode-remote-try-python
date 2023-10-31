#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
# write 'hello world' to the console
import random
l=['rock','paper','scissor']
m=input()

while(m!='0'):
    s=random.choice(l)
    print('you choice: ',m)
    print('computer choice: ',s)
    if(s=='rock' and m=='paper'):
        print('you won')
    elif(s=='rock' and m=='rock'):
        print('tie')
    elif(s=='rock' and m=='scissor'):
        print('you lost')
    elif(s=='paper' and m=='rock'):
        print('you lost')
    elif(s=='paper' and m=='paper'):
        print('tie')
    elif(s=='paper' and m=='scissor'):
        print('you won')
    elif(s=='scissor' and m=='scissor'):
        print('tie')
    elif(s=='scissor' and m=='paper'):
        print('you lost')
    elif(s=='scissor' and m=='rock'):
        print('you won')
    else:
        print('invalid')
    m=input()

        
    
