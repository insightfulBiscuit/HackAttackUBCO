# -----------------------------------------------------------------------------

from Event import Event
from CalendarLogic import Calendar
from datetime import datetime

# ------------------------------------------------------------------------------------------------

def calculateUrgency(due_date):
# Calculate the difference in days between due date and current date in PST
  days_until_due = (due_date - calendar.current_time_pst).days

  # Define urgency based on days until due
  if days_until_due < 1:
      urgency = 10
  elif 1 <= days_until_due <= 3:
      urgency = 8
  elif 4 <= days_until_due <= 7:
      urgency = 5
  else:
      urgency = 2

  return urgency

# create event function
def createEvent():
  # user enters name of event
  name = input("\nEnter the name of Event: ")

  while True:
    try:
      due_date_str = input("Enter Due Date of Event (DD/MM/YYYY): ")
      due_date = datetime.strptime(due_date_str, "%d/%m/%Y").date()

      if (due_date < calendar.current_time_pst):
        print("Due date must be later than today's date. Please enter a valid future date.\n")
      else:
        break
    except ValueError:
        print("Invalid date format. Please enter date in DD/MM/YYYY format.\n")

  #prompts the user to enter the type of event
  while True:
    typeof = input("Enter type of Event (Academic, Wellbeing, Social): ").lower()
    if typeof in valid_event_type:
      break
    print("Invalid input. Please enter a valid event type.\n")

  while True:
    try:
      importance = int(input("Enter importance of Event (from 1-10): "))
      if (importance >= 1 and importance <= 10):
        break
      else:
        print("Invalid input. Please enter a number between 1 and 10.\n")
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 10.\n")

  #prompts the user to input the duration of the event
  while True:
    try:
      duration_hr = int(input("Enter duration of Event (in hours): "))
      if duration_hr >= 0:
        break
      else:
        print("Invalid input. Please enter a number greater than or equal to 0.\n")
    except ValueError:
      print("Invalid input. Please enter a number.\n")

  #prompts the user to input the location of the event
  location = input("Enter location of Event: ")

  #prompts the user to input the rest time they want after the event 
  while True:
    try:
      rest_time = int(input("Enter rest time for after the event (in hours): "))
      if rest_time >= 24 or rest_time < 0:
        print("Invalid input. Please enter a number less than 24.\n")
      else:
        break
    except ValueError:
      print("Invald input. Please enter a number.\n")

  while True:
      fluid = input("Is the event fluid? (yes/no): ")
      if fluid.lower() == "yes":
        fluid = True
        time = "-1"
        break
      elif fluid.lower() == "no":
        fluid = False
        try:
          time = int(input("Enter time of event (HH): "))
          if time >= 24 or time < 0:
            print("Invalid input. Please enter a number 0-24.\n")
          else:
            break
        except ValueError:
          print("Invalid input. Please enter a number.\n")

  return Event(name=name, due_date=due_date, time=time, typeof=typeof, importance=importance, duration_hr=duration_hr, location=location, fluid=fluid, urgency=calculateUrgency(due_date))

# ------------------------------------------------------------------------------------------------

valid_event_type = ('academic', 'wellbeing', 'social')

CREATE_CALENDAR = 1
MANAGE_EVENTS = 2
VIEW_CALENDAR = 3
EXIT = 4

calendar = Calendar()

print("Hello! Welcome to the Calendar App!")

while True:
  print("\n--------------\nMain Page\n--------------\n")
  print("1. Create Event\n2. Manage Events\n3. View Calendar\n4. Exit")
  while True:
    try:
      user_input = int(input("\nEnter an existing option: "))
      if (user_input != CREATE_CALENDAR and user_input != MANAGE_EVENTS and user_input!= VIEW_CALENDAR and user_input != EXIT):
        print("Invalid input. Please an existing option.")
      else:
        break
    except ValueError:
      print("Invalid input. Please an existing option.")

  if (user_input == CREATE_CALENDAR):
    calendar.addEvent(createEvent())
    print("\nEvent created successfully!\n")

  elif (user_input == MANAGE_EVENTS):
    print("\n**Option not yet developed**")
    
  elif (user_input == VIEW_CALENDAR):
    # print(calendar)
    calendar.displayInTerminal()
    print("\nPending UI integration")

  elif (user_input == EXIT):
    print("\nHave a nice Day!")
    break

  else:
    print("\nSomethings wrong.")
    break