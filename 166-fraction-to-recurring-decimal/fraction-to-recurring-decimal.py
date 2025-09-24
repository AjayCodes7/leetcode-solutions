class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        result = []

        neg = (numerator > 0) ^ (denominator > 0)

        if neg:
            result.append('-')

        num = abs(numerator)
        den = abs(denominator)

        result.append(str(num//den))
        rem = num % den

        if rem == 0:
            return "".join(result)
        
        result.append(".")


        decimal = {}

        while rem:
            decimal[rem] = len(result)

            rem *= 10

            result.append(str(rem//den))
            rem = rem % den

            if rem in decimal:
                result.insert(decimal[rem],"(")
                result.append(")")
                break
        return "".join(result)
