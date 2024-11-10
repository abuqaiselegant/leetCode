class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score =[]
        for i in range(len(operations)):
            if operations[i] == "+":
                if i >=1:
                    score.append(score[-1]+score[-2])
                else:
                    score.append(score[-1])
            elif operations[i] =="C":
                score.remove(score[-1])
            elif operations[i]=="D":
                score.append(2*score[-1])
            else:
                score.append(int(operations[i]))
        print(score)
        return sum(score)