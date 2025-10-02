import map
temperatures = [212, 32, 100]
print(list(map(lambda f: (f - 32) * 5.0/9.0, temperatures)))
numbers = [3,1,4,1,5,9,2,6,5,3,5]
print(sorted(numbers, reverse=True))
midterm = {'Carol' : 92, 'Alice' : 95, 'Bob' : 88, 'Eve': 100, 'Dave': 70}
sortedScores = sorted(midterm.items(), key=lambda x : x[1], reverse=True)
print(sortedScores)