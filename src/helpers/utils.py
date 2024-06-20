from datetime import datetime


def wip_time(start_time: datetime):
    """Print the time taken since the start_time.

    Args:
        start_time (datetime): Start time of the process.
    """
    wip_time_in_seconds = (datetime.now() - start_time).total_seconds()
    print(f"Time taken: {wip_time_in_seconds} seconds ~ {wip_time_in_seconds / 60} minutes")
