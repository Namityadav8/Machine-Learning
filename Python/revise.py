def compress_string(s):
    if not s:
        return ""  # handle empty string

    result = ""
    count = 1
    prev = s[0]

    for char in s[1:]:
        if char == prev:
            count += 1
        else:
            result += prev + str(count)
            prev = char
            count = 1

    # Add the last group
    result += prev + str(count)
    return result

# Example usage
s = "aabbbbeeeeffggg"
compressed = compress_string(s)
print(compressed)
















s = "abcdecaecdeb"

count_dict = {}
for char in s:
    count_dict[char] = count_dict.get(char, 0) + 1

compressed = ''.join(f"{char}{count}" for char, count in count_dict.items())
print(compressed)

