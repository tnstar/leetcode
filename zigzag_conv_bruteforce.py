class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s;
        char_map = {}
        for i in range(nRows):
            char_map[i]=[]
        lower = 0
        upper = nRows-1
        len_str = len(s)
        next_row = 0
        n = len_str
        direction = "down"
        while n>0:
            print next_row,direction
            char_map[next_row].append(s[len_str-n])
            n -=1
            if direction == "down":
                print "down"
                next_row = next_row +1
            else:
                print "up"
                next_row = next_row -1
            if next_row >upper:
                next_row = upper-1
                direction = "up"
            elif next_row <lower:
                next_row = lower+1
                direction = "down"
        answer = ""
        for i in range(nRows):
            answer = answer + "".join(char_map[i])
        print answer
sol=Solution()
sol.convert("AB", 1)