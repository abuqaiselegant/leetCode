class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        # Generate each row
        for i in range(1, numRows):
            # Get previous row
            prev_row = result[-1]
            # Start new row with 1
            current_row = [1]
            
            # Calculate middle elements
            for j in range(1, i):
                current_row.append(prev_row[j-1] + prev_row[j])
            
            # End row with 1
            current_row.append(1)
            
            # Add to result
            result.append(current_row)
            
        return result

        