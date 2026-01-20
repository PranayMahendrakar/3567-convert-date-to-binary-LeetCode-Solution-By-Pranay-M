class Solution:
    def convertDateToBinary(self, date: str) -> str:
        parts = date.split('-')
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        return f"{bin(year)[2:]}-{bin(month)[2:]}-{bin(day)[2:]}"