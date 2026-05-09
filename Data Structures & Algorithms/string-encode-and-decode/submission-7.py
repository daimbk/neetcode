class Solution:

    def encode(self, strs: List[str]) -> str:
        msg = ""
        
        if len(strs) == 0:
            return msg

        for word in strs:
            n = len(word)
            msg += str(n) + "#" + word

        return msg

    def decode(self, s):
        strLength = len(s)

        decoded = []
        n = 0

        if strLength == 0:
            return decoded

        i = 0
        val = s[i]
        while i != strLength:
            n = 0
            while val != '#':
                n = (n * 10) + int(val)
                if (i + 1) < strLength:
                    i = i + 1
                    val = s[i]

            decoded.append(s[(i + 1):(i+n+1)])
            if (i + n + 1) < strLength:
                i = i + n + 1
                val = s[i]
            else:
                i = strLength

        return decoded