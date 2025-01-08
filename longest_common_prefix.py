class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #check if string is empty
        if not strs:
            return ""
        #sort the string lexicograhically , so that we can first and last strings
        strs.sort()

        #create an empty list to store common characters
        common_prefix=[]
        last_string, first_string = strs[0], strs[-1]

        #compare the characters of first and last string ,if match not found stop loop
        for i in range(len(last_string)):
            if i <= len(first_string) and first_string[i]==last_string[i]:
                common_prefix.append(first_string[i])
            else:
                break
        #join the characters
        return "".join(common_prefix)
        
