# CIS 41A
# Ch.9, ex1 (extra credit)
# Saba Feilizadeh

# Coffee Chat Scheduler:
# Schedules 15-minute coffee chats between employees where each person meets
# everyone else exactly once.
# Uses round-robin tournament algorithm to generate weekly pairings with O(n)
# complexity per week.

# ------------------------------------------------------ 
class CoffeeChatScheduler:
    def __init__(self, employees):
        """
        Initialize a new coffee chat scheduler.

        Args:
            employees (list): List of employee names to schedule.

        Raises:
            ValueError: If number of employees is not even.
        """
        if len(employees) % 2 != 0:
            raise ValueError("Number of employees must be even!")
        self.employees = employees
        self.n = len(employees)
        self.weeks_needed = self.n - 1
        
    def generate_schedule(self):
        """
        Generate weekly meeting schedules for all employees.

        Returns:
            list: List of weekly schedules, where each schedule is a list of
                 tuples containing pairs of employees to meet.
        """
        # Create a copy of employees list to rotate
        circle = self.employees[:]
        
        weekly_schedules = []
        for week in range(self.weeks_needed):
            # Generate pairs for this week
            meetings = []
            for i in range(self.n // 2):
                # Pair first half with second half
                meeting = (circle[i], circle[self.n - 1 - i])
                meetings.append(meeting)
            
            weekly_schedules.append(meetings)
            
            # Rotate all elements except the first one
            circle = [circle[0]] + [circle[-1]] + circle[1:-1]
            
        return weekly_schedules
# ------------------------------------------------------ 
def print_schedule(schedules):
    """
    Print all weekly schedules in a readable format.

    Args:
        schedules (list): List of weekly schedules, where each schedule is a
                         list of tuples containing pairs of employees.
    """
    for week, meetings in enumerate(schedules, 1):
        print(f"\nWeek {week}:")
        for meeting in meetings:
            print(f"  {meeting[0]} & {meeting[1]} will have a coffee meeting")
# ------------------------------------------------------ 
def get_valid_employee_count():
    """Get and validate the number of employees from user input.

    Returns:
        int: A valid even number of employees (>= 2).
    """
    while True:
        try:
            n = int(input("Enter the number of employees (must be even): "))
            if n < 2:
                print("Error: Number must be at least 2!")
            elif n % 2 != 0:
                print("Error: Number must be even!")
            else:
                return n
        except ValueError:
            print("Error: Please enter a valid number!")

def main():
    # Get valid number of employees from user
    n = get_valid_employee_count()
    
    # Generate employee list
    employees = [f"employee_{i}" for i in range(1, n + 1)]
    
    scheduler = CoffeeChatScheduler(employees)
    weekly_schedules = scheduler.generate_schedule()
    print_schedule(weekly_schedules)
# ------------------------------------------------------ 
if __name__ == "__main__":
    main()
# ------------------------------------------------------ 
'''
========================================================
                       Output 1
========================================================
Enter the number of employees (must be even): 3
Error: Number must be even!
Enter the number of employees (must be even): 1
Error: Number must be at least 2!
Enter the number of employees (must be even): six 
Error: Please enter a valid number!
Enter the number of employees (must be even): 6

Week 1:
  employee_1 & employee_6 will have a coffee meeting
  employee_2 & employee_5 will have a coffee meeting
  employee_3 & employee_4 will have a coffee meeting

Week 2:
  employee_1 & employee_5 will have a coffee meeting
  employee_6 & employee_4 will have a coffee meeting
  employee_2 & employee_3 will have a coffee meeting

Week 3:
  employee_1 & employee_4 will have a coffee meeting
  employee_5 & employee_3 will have a coffee meeting
  employee_6 & employee_2 will have a coffee meeting

Week 4:
  employee_1 & employee_3 will have a coffee meeting
  employee_4 & employee_2 will have a coffee meeting
  employee_5 & employee_6 will have a coffee meeting

Week 5:
  employee_1 & employee_2 will have a coffee meeting
  employee_3 & employee_6 will have a coffee meeting
  employee_4 & employee_5 will have a coffee meeting

========================================================
                       Output 2
========================================================
Enter the number of employees (must be even): 4

Week 1:
  employee_1 & employee_4 will have a coffee meeting
  employee_2 & employee_3 will have a coffee meeting

Week 2:
  employee_1 & employee_3 will have a coffee meeting
  employee_4 & employee_2 will have a coffee meeting

Week 3:
  employee_1 & employee_2 will have a coffee meeting
  employee_3 & employee_4 will have a coffee meeting
'''