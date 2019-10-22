    
class phone_inter:
    def __init__(self, cdp_neig, separator):
        self.cdp_neig = cdp_neig
        self.separator = separator
    def find(self):
        data = self.cdp_neig
        lines = data.split('\n')
        for i in lines:
            if '#' in i and 'sho cdp n' in i:
                #print(i)
                devicelist = i.split('#')
                devicestring = devicelist[0]
                print('')
                print(self.separator * 30)
                print(devicestring)
                print(self.separator * 30)
                print('')
                print('config t')
                result = '' + '\n'             
                result += self.separator * 30 + '\n' 
                result += devicestring + '\n' 
                result += self.separator * 30 + '\n' 
                result += '' + '\n' 
                result += 'config t' + '\n' 
            if 'SEP' in  i:
                #print(i)
                interfacelist = i.split(" ")
                #print(interfacelist)
                interfacestring = 'interface ' + interfacelist[2] + ' ' + interfacelist[3]
                print(interfacestring)
                print('shut')
                print('no shut')
                result += interfacestring + '\n' 
                result += 'shut' + '\n' 
                result += 'no shut' + '\n' 
        return result

p = phone_inter(data, "~")
p.find()
fphone = p.find()
fphone