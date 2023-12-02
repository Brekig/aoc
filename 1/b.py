if __name__ == "__main__":
    dict_ = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", 
         "six": "6", "seven": "7", "eight": "8", "nine": "9", "1": "1", "2": "2", 
         "3": "3", "4": "4", "5": "5","6": "6", "7": "7", "8": "8", "9": "9"}
    sum = 0
    with open('./input.txt', 'r') as file:
        for i, line in enumerate(file):
            line = line.strip()
            key = ""
            left = ""
            right = ""
            r = len(line)-1
            l = 0
            left_str = ""
            right_str = ""
            while (True):
                if left and right:
                    break
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
                
                if left:
                    r -= 1
                elif right:
                    l += 1
                else:
                    r -= 1
                    l += 1
            print("Line nr: ", i, " | ", left, right)
            sum += int(left + right)
    print(sum)
            
