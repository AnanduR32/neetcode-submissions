class Solution:

    def encode(self, strs: List[str]) -> str:
        output:str = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        
        class Logic:
            def __init__(self):
                self.reset()
            def reset(self)-> None:
                self.__digit = 0
                self.__string = ''
                self.__isReading = False

            @property
            def digit(self)->int:
                return self.__digit
            
            def insertDigitInOnesPlace(self, char)->None:
                self.__digit = self.__digit * 10 + int(char)

            @property
            def string(self)->str:
                return self.__string
            
            def appendCharToString(self, char)->None:
                self.__string += char

            @property
            def isReading(self)->bool:
                return self.__isReading
            
            def setReadingStatus(self, status)->None:
                self.__isReading = status


        output = []
        logic = Logic()
        count = 0
        for char in s:
            if char.isdigit() and not logic.isReading:
                logic.insertDigitInOnesPlace(char)
            elif char == '#' and not logic.isReading:
                logic.setReadingStatus(True)
            else:
                logic.appendCharToString(char)
                count += 1
            
            if count == logic.digit and logic.isReading:
                output.append(logic.string)
                logic.reset()
                count = 0

        return output
                