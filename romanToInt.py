def romanToInt(s):
    summary = 0
    previous = s[0]
    table = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000}
    for i in s:
        if i in table:
            if table[previous] < table[i]:
                summary = summary - (table[previous]*2)
            summary = summary + table[i]
        previous = i
    return summary


inp = "MCMXCIV"
print(romanToInt(inp))
