

def load_input() -> tuple[[int], list[int]]:
    with open(r"input.txt", "r") as file:
        input_content = file.read()
        left_list = []
        right_list = []

        for row in input_content.split("\n"):
            left_id, _, right_id = row.partition("   ")
            left_list.append(int(left_id))
            right_list.append(int(right_id))

    return left_list, right_list


def find_total_distance_between_lists(left_list: list[int], right_list: list[int]) -> int:
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)
    distances = [abs(left_id - sorted_right_list[i]) for i, left_id in enumerate(sorted_left_list)]
    total_distance = sum(distances)
    return total_distance


if __name__ == "__main__":
    left_list, right_list = load_input()
    total_distance = find_total_distance_between_lists(left_list=left_list, right_list=right_list)
    print(f"Total Distance: {total_distance}")
