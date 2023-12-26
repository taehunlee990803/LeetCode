class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        kelvin = round(celsius + 273.15, 5)        
        fehr = round(celsius*1.80 + 32.00, 5)
        ans.append(kelvin)
        ans.append(fehr)
        return ans
3
