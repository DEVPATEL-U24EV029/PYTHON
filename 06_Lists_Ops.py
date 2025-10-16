numbers=[16,22,44,55,43]
print("---elements in the list---")
for num in numbers:
    print (num);

total =sum(numbers)
largest=max(numbers)
smallest=min(numbers)

print (" list of operations")
print(f"sum of numbers {total}")
print (f"largest number {largest}")
print (f"smallest number {smallest}")
