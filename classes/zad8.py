from datetime import datetime, timezone
first_case = {
    "name": "first_case",
    "created_task": "2021-10-26T19:48:12+00:00",
    "end_task": None
}

second_case = {
    "name": "second_case",
    "created_task": "2021-09-26T19:48:12+00:00",
    "end_task": "2021-10-26T19:48:12+00:00"
}

class Case:
    def __init__(self, data:dict):
        self.name: str = data["name"]
        self.created_task: datetime = datetime.fromisoformat(
            data["created_task"]
        )
        if data["end_task"] is not None:
            self.end_task: datetime | None = datetime.fromisoformat(
                data["end_task"]
            )
        else:
            self.end_task: datetime | None = None

    def retrieve_seconds(self):
        if self.end_task is None:
            return (datetime.now(timezone.utc) - self.created_task).total_seconds()
        else:
            return (self.end_task - self.created_task).total_seconds()





def main():
    case1 = Case(first_case)
    case2 = Case(second_case)
    print(f"First Case: {round(case1.retrieve_seconds(),2)}")
    print(f"Second Case: {case2.retrieve_seconds()}")


if __name__ == "__main__":
    main()

