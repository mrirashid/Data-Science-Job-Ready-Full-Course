with open("buffering_file.txt", "w", encoding="utf-8") as f:
    for i in range(1_000_000):
        f.write(f"Line {i}\n")

with open("buffering_file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
