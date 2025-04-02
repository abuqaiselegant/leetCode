class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop")
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")

        rows =[first_row,second_row,third_row]
        result = []

        for word in words:
            word_lower = word.lower()

            #home_rows = None
            for row in rows:
                if word_lower[0] in row:
                    home_rows = row
                    break

            # if not home_rows:
            #     continue

            isValid = True
            for char in word_lower:
                if char not in home_rows:
                    isValid =False
                    break

            if isValid:
                result.append(word)
        return result


        
