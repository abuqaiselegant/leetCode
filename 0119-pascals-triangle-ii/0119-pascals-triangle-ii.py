class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize first row
        row = [1]
        
        # Generate each row up to rowIndex
        for i in range(rowIndex):
            # Create new row starting with 1
            newRow = [1]
            
            # Calculate middle elements
            for j in range(1, len(row)):
                newRow.append(row[j-1] + row[j])
                
            # Add final 1
            newRow.append(1)
            
            # Update row
            row = newRow
            
        return row