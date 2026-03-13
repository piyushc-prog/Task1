
with open("input.txt", "r") as f:
    text = f.read()

new_text = text.title()
space_count = new_text.count(" ")


with open("output.txt", "w") as f:
    f.write(new_text)

print("Total whitespaces:", space_count)
