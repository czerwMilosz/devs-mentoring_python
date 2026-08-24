def create_week_dict() -> dict:
    week_dict = {"1": 'monday',
                 "2": 'tuesday',
                 "3": 'wednesday',
                 "4": 'thursday',
                 "5": 'friday',
                 "6": 'saturday',
                 "7": 'sunday'}
    return week_dict

def get_user_day(week:dict) -> str:
    while True:
        try:
            day = week[input("Enter a day number from 1 to 7: ")]
            return day
        except KeyError:
            print("That is not a valid day")

def get_user_day2(week:dict) -> str:
   while True:
       day = input("Enter a day number from 1 to 7: ")

       if day in week:
           return week[day]
       else:
           print("That is not a valid day")

def main():
    week = create_week_dict()
    day = get_user_day2(week)
    print(day)

if __name__ == "__main__":
    main()

