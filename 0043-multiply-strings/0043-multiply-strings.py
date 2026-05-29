class Solution:
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                product = int(num1[i]) * int(num2[j])

                position1 = i + j
                position2 = i + j + 1

                total = product + result[position2]

                result[position2] = total % 10
                result[position1] += total // 10

        answer = ""

        for num in result:
            if not (answer == "" and num == 0):
                answer += str(num)

        return answer