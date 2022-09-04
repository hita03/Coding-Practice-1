class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        s=""
        li=address.split(".")
        for i in range(len(li)-1):
            print(i,li[i])
            s+=str(li[i])
            s+="[.]"
        
        i+=1
        s+=str(li[i])    
        return s    
                