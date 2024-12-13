import math


def load_input() -> str:
    with open("input.txt", "r") as file:
        input_content = file.read()
    return input_content


def unjumble_mess(corrupted_memory: str) -> int:
    # I commit to a regex-free solution, for reasons of Alan Pallu.
    corrupted_memory_pieces = corrupted_memory.split("mul(")

    raw_muls = []

    for piece in corrupted_memory_pieces:
        last_char_type = "x"
        collected_chars = ["("]
        is_valid_piece = False

        for char in piece:
            if last_char_type == "x":
                if char.isnumeric():
                    collected_chars.append(char)
                    last_char_type = "x"
                elif char == ",":
                    collected_chars.append(char)
                    last_char_type = "sep"
                else:
                    break

            elif last_char_type == "y":
                if char.isnumeric():
                    collected_chars.append(char)
                elif char == ")":
                    collected_chars.append(char)
                    is_valid_piece = True
                    break
                else:
                    break

            elif last_char_type == "sep":
                if char.isnumeric():
                    collected_chars.append(char)
                    last_char_type = "y"
                else:
                    break

        if is_valid_piece:
            raw_muls.append("".join(collected_chars))

    muls = list(map(eval, raw_muls))
    muls_results = list(map(math.prod, muls))
    return sum(muls_results)


if __name__ == "__main__":
    corrupted_memory = load_input()
    multiplication_result = unjumble_mess(corrupted_memory=corrupted_memory)
    print(f"Multiplication Result: {multiplication_result}")
