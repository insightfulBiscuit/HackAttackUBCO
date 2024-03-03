from datetime import datetime, timedelta
import copy
import Day as day

class Calendar:
  def __init__(self):
    self.current_time_pst = (datetime.utcnow() - timedelta(hours=8)).date()
    self.day_list = []
    self.fluid_events = []
    self.non_fluid_events = []

  def displayInTerminal(self, ):
    print("\n--------------\nCalendar\n--------------\n")
    for day in self.day_list:
      for static in day.non_fluid_event_list:
        print("Static Event: " + str(static))
      for fluid in day.fluid_event_list:
        print("Fluid Event: " + str(fluid))

  def resetDaysList(self):
    self.day_list = []
    for i in range (30):
      self.day_list.append(day.Day(self.current_time_pst + timedelta(days=i)))      

  def updateCalendar(self, event):
    self.resetDaysList()
    for index1, event in enumerate(self.non_fluid_events):
      for index2, day in enumerate(self.day_list):
          if str(event.due_date) == str(day.date):
              self.day_list[index2].addEvent(event)
              self.day_list[index2].usable_time -= event.duration_hr

    self.fluid_events.sort(key=lambda x: x.precedence, reverse=True)

    for index1, event in enumerate(self.fluid_events):
      for index2, day in enumerate(self.day_list):
        if (self.day_list[index1].usable_time >= 1):
          self.day_list[index2].addEvent(event)
          try:
            self.day_list[index2].usable_time -= 1
            self.day_list[index2+1].hours_in_day[self.day_list[index2+1].hours_in_day.index(0)]
          except ValueError:
            self.day_list[index2+1].hours_in_day[self.day_list[index2+1].hours_in_day.index(0)] = 1
            self.day_list[index2+1].hours_in_day[self.day_list[index2+1].hours_in_day.index(0)]
          break

  def addEvent(self, event):
    if not event.fluid:
      self.non_fluid_events.append(event)
    else:
      for i in range(0, event.duration_hr):
        tempEvent = copy.deepcopy(event)
        tempEvent.duration_hr = 1
        self.fluid_events.append(tempEvent)

    self.updateCalendar(event)
