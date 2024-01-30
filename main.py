import argparse


def parse_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--byte", type=str, default="0x00")
    parser.add_argument("--minimum-length", type=int, default=5)
    args = parser.parse_args()
    return args


def main() -> None:
    args = parse_cli_args()
    with open(args.file, "rb") as in_fh:
        data = in_fh.read()

    target_byte = int(args.byte, 16)
    last_found = -1
    for index, byte in enumerate(data):
        # Skip ahead so we don't work within the same cave multiple times
        if index <= last_found:
            continue

        if byte == target_byte:  # Possibly at the start of a cave
            length = 1
            while index + length < len(data) and data[index + length] == target_byte:
                length += 1
            if length >= args.minimum_length:
                # Only display the caves of an interesting size
                print(index, length)

            # Skip ahead to the byte immediately following the cave
            last_found = index + length


if __name__ == "__main__":
    main()
