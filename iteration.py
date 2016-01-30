books = ["Tale of Two Cities", "Harry Potter", "Lord of the Rings"]
nums = range(0, 50)

for n in nums:
    for b in books:
        if n % 10 == 0:
            print(b)
