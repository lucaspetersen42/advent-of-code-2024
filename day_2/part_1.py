

def load_input() -> list[list[int]]:
    with open("input.txt", "r") as file:
        input_content = file.read()
        reports_rows = input_content.split("\n")
        reports = [[int(level) for level in row.split(" ")] for row in reports_rows]

    return reports


def count_safe_reports(reports: list[list[int]]) -> int:
    n_safe_reports = 0

    for report in reports:
        is_report_safe = True
        curr_level = report[0]
        is_ascending = curr_level < report[1]
        is_descending = curr_level > report[1]

        for level in report[1:]:
            if is_ascending:
                if not (3 >= (level - curr_level) >= 1):
                    is_report_safe = False
                    break

            elif is_descending:
                if not (3 >= (curr_level - level) >= 1):
                    is_report_safe = False
                    break

            else:
                is_report_safe = False
                break

            curr_level = level

        if is_report_safe:
            n_safe_reports += 1

    return n_safe_reports


if __name__ == "__main__":
    reports = load_input()
    n_safe_reports = count_safe_reports(reports=reports)
    print(f"Nº of Safe Reports: {n_safe_reports}")
