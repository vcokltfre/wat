from sys import argv


def main() -> None:
    if len(argv) != 2:
        print("Usage: wat <filename>")
        exit(1)

    with open(argv[1]) as f:
        data = f.readlines()

    new = []
    n = "69".zfill(len(str(len(data))))

    for line in data:
        line = line.strip('\n')
        new.append(f"{n} | {line}")

    print("\n".join(new))
