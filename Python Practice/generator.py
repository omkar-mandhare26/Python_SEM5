def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Example usage
for number in count_up_to(5):
    print(number)
