List = ["Daniel", "Boytraze", "Awodi", "Emmy"]
print("\nList containing muiltiple values: ")
print(List)

List2 = [["Geeks", "For"], ["Geeks"]]
print("\nMuilti-Dimentional List: ")
print(List2)
print(List2[0][1])

if List2[0][0:-1] == ['Geeks']:
    print("\nList correct")
    
elif List2[0][1] == 'For':
    print("Yay great guy!")
else:
    print("Wrong!")
    
    
print("Accessing element from the list")
print(List[0])
print(List[2])

print("Accessing element using the negetive indexing")

print(List[-1])
print(List[-3])