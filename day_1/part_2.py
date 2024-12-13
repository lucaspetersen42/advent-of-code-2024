from day_1.part_1 import load_input


def calculate_similarity_score(left_list: list[int], right_list: list[int]) -> int:
    unique_left_numbers = set(left_list)
    count_by_number = {number: right_list.count(number) for number in unique_left_numbers}

    similarity_values = list(map(lambda id_: count_by_number.get(id_) * id_, left_list))
    similarity_score = sum(similarity_values)
    return similarity_score


if __name__ == '__main__':
    left_list, right_list = load_input()
    similarity_score = calculate_similarity_score(left_list=left_list, right_list=right_list)
    print(f"Similarity Score: {similarity_score}")
