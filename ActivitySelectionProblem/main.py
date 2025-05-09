from datetime import datetime
from typing import List, Tuple
from tabulate import tabulate

# --- Conversion Utilities ---


def convert_to_24h(time_str: str) -> datetime:
    return datetime.strptime(time_str, "%I:%M %p")


def format_time(dt: datetime) -> str:
    return dt.strftime("%I:%M %p")


# --- Parsing and Preprocessing ---


def parse_schedule(schedule: Tuple[str, str, str]) -> Tuple[str, datetime, datetime]:
    block, start_str, end_str = schedule
    return block, convert_to_24h(start_str), convert_to_24h(end_str)


def prepare_activities(
    raw_schedules: List[Tuple[str, str, str]]
) -> List[Tuple[str, datetime, datetime]]:
    return [parse_schedule(entry) for entry in raw_schedules]


# --- Activity Selection Greedy Search Algorithm ---


def select_non_overlapping_activities(
    activities: List[Tuple[str, datetime, datetime]]
) -> List[Tuple[str, str, str]]:
    selected = []
    sorted_activities = sorted(activities, key=lambda x: x[2])
    last_end_time = None

    for block, start, end in sorted_activities:
        if last_end_time is None or start >= last_end_time:
            selected.append((block, format_time(start), format_time(end)))
            last_end_time = end

    return selected


def activity_selection(
    raw_schedules: List[Tuple[str, str, str]]
) -> List[Tuple[str, str, str]]:
    activities = prepare_activities(raw_schedules)
    return select_non_overlapping_activities(activities)


# --- Program Entry Point ---

if __name__ == "__main__":
    schedules = [
        ("BSCS 2-2", "08:00 AM", "10:00 AM"),
        ("BSIT 1-3", "09:00 AM", "11:00 AM"),
        ("BSCS 2-5", "10:30 AM", "12:00 PM"),
        ("BSIS 1-2", "11:00 AM", "01:00 PM"),
        ("BSCS 3-5", "01:00 PM", "03:00 PM"),
        ("BSIT 2-1N", "02:00 PM", "04:00 PM"),
    ]

    all_table = [[block, start, end] for block, start, end in schedules]
    selected_table = activity_selection(schedules)

    print("📋 All Lab Time Slot Requests:")
    print(
        tabulate(
            all_table,
            headers=["Block/Section", "Start Time", "End Time"],
            tablefmt="grid",
        )
    )

    print("\n✅ Selected Lab Time Slots:")
    print(
        tabulate(
            selected_table,
            headers=["Block/Section", "Start Time", "End Time"],
            tablefmt="grid",
        )
    )
