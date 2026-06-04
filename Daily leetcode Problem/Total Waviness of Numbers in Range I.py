def total_wave_peak(num1,num2):
    ans = 0

    for x in range(num1,num2+1):
        s =str(x)

        for i in range(1,len(s)-1):
            if ((s[i] > s[i - 1] and s[i] > s[i + 1]) or (s[i] < s[i - 1] and s[i] < s[i + 1])):
                ans+=1
    return ans

if __name__ == "__main__":
    num1 = 120
    num2 = 130
    print(total_wave_peak(num1,num2))