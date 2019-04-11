import numpy as np

def c5read(fname):
" Reads the data from a channel 5 CTF file and returns a list with the euler angles at each point as an array"

    data_list=[]
    f=open(fname,'r')
    print 'Reading file...'
    for line in f:
        if line[0:2]=='XC':
            xdim=int(line.split()[1])   
            print xdim
            
        if line[0:2]=='YC':
            ydim=int(line.split()[1])
            print ydim
                 
        if re.match('\d\s',line) != None: 
            if int(line.split()[0]) == 2:
                eulers=line.split()[5:8] 
                for x in range(len(eulers)):
                    eulers[x]=float(eulers[x])
                data_list.append(np.array(eulers))
            else:
                eulers=line.split()[5:8]
                for x in range(len(eulers)):
                    eulers[x]=float('0.0')
                data_list.append(np.array(eulers)) 
    f.close()
    print 'Done!'

    #For creating an array from the list:
    #emap=np.array(data_list).reshape(ydim,xdim,3) 

    return data_list
