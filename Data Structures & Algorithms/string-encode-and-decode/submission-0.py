class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedL = "NEWWORD"
        for word in strs:
            temp = ""
            for let in word:
                temp+=(chr((ord(let)- 1) % 256))
            encodedL +=(temp + "NEWWORD")
        #print(encodedL)
        return encodedL

                

    def decode(self, s: str) -> List[str]:
        decodedL = []
        sL = s.split("NEWWORD")
        #print(sL)
        for word in sL[1:-1]:
            # if len(word) == 0 :
            #     continue
            temp = []
            for let in word:
                temp.append(chr((ord(let) + 1) % 256))
            decodedL.append("".join(temp))
        
        #print(decodedL)
        return decodedL
