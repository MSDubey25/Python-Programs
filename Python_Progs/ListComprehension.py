h_letters=[]

for i in "human":
    h_letters.append(i)
print(h_letters)

word=[letter for letter in 'MAnikant']
print(word)

print("List using Lambda")
string=list(map(lambda x:x,'world'))
print(string)

number=[x for x in range(20) if x%2==0]
print(number)

num=[y for y in range(100) if y%2==0 if y%5==0]
print(num)

obj=['even' if i%2==0 else 'odd' for i in range(10)]
print(obj)

matrix=[[1,2],[3,4],[5,6],[7,8]]
transpose=[[row[i] for row in matrix] for i in range(2)]
print(transpose)



