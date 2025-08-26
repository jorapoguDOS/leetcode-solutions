class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []

        for i in range(1, n+1):
            div_3 = i % 3
            div_5 = i % 5
            if div_3 != 0 and div_5 != 0:
                output.append(str(i))
            elif div_3 == 0:
                if div_5 != 0:
                    output.append("Fizz")
                else:
                    output.append("FizzBuzz")
            else:
                output.append("Buzz")

        return output