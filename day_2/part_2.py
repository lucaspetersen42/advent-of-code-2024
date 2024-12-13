from day_2.part_1 import load_input, count_safe_reports


def count_safe_reports_with_tolerance(reports: list[list[int]]) -> int:
    n_safe_reports = 0

    for report in reports:
        possibilities = []

        for index in range(len(report)):
            report_copy = report.copy()
            report_copy.pop(index)
            possibilities.append(report_copy)

        n_safe_possibilities = count_safe_reports(reports=possibilities)
        if n_safe_possibilities > 0:
            n_safe_reports += 1

    return n_safe_reports


if __name__ == '__main__':
    reports = load_input()
    n_safe_reports = count_safe_reports_with_tolerance(reports=reports)
    print(f"Nº of Safe Reports: {n_safe_reports}")
