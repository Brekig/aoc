if __name__ == "__main__":
    dict_ = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
         "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    sum = 0
    with open('./input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            key = ""
            left = ""
            right = ""
            r = len(line)-1
            l = 0
            left_str = ""
            right_str = ""
            while (l < r):
                cl = line[l]
                cr = line[r]
                temp_l = left_str + cl
                temp_r = cr + right_str
                l_matches = [key for key in dict_ if temp_l in key]
                
                if l_matches:
                    left_str += cl
                else:
                    left_str = cl
                    
                r_matches = [key for key in dict_ if temp_r in key]
                if r_matches:
                    right_str = cr + right_str
                else:
                    right_str = cr
                if left_str in dict_ and left == "":
                    left = dict_[left_str]
                if right_str in dict_ and right == "":
                    right = dict_[right_str]    
                if cl.isdigit() and left == "":
                    left = cl
                if cr.isdigit() and right == "":
                    right = cr
                if left and right:
                    break
                if left:
                    r -= 1
                elif right:
                    l += 1
                else:
                    r -= 1
                    l += 1
            print(left, right)
            if not left:
                left = "0"
            if not right:
                right = "0"
            sum += int(left + right)
    print(sum)
            
