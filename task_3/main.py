import re
import sys

def parse_log_line(log_line) -> dict:
    pattern = r"^(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<message>.+)$"
    match = re.match(pattern, log_line)
    if match:
        return {
            "datetime": match.group("datetime"),
            "level": match.group("level"),
            "message": match.group("message")
        }
    
    return None

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    logs.append(parse_log_line(line))
    except FileNotFoundError:
        print("Файл не знайдено.")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    level = level.upper()
    return [log for log in logs if log["level"] == level]

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        lvl = log["level"]
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до лог-файлу.")
        return

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered = filter_logs_by_level(logs, level)
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in filtered:
            print(f"{log['datetime']} - {log['message']}")

if __name__ == "__main__":
    main()
