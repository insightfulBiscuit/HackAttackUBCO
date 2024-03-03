class Day:
  def __init__(self, date):
    self.TOTAL_TIME = 24
    self.date = date
    self.fluid_event_list = []
    self.non_fluid_event_list = []
    self.hours_in_day = [0] * 24
    self.usable_time = self.TOTAL_TIME

  def updateUsableTime(self):
    self.usable_time = 24
    
    for index, hours_in_day in enumerate(self.hours_in_day):
      if hours_in_day == 1:
        self.usable_time -= 1

  def addEvent(self, event):
    while True:
      self.updateUsableTime()
      # static event
      if not event.fluid and event.duration_hr < self.usable_time:
        for i in range(event.time, (event.duration_hr + event.time)):
          self.hours_in_day[i] = 1
          
        self.non_fluid_event_list.sort(key=lambda x: x.time, reverse=False)
        till = 0

        #sleep
        if len(self.non_fluid_event_list) == 0:
          if len(self.non_fluid_event_list) != 0:
            till = 8
            if self.non_fluid_event_list[0].time < 8:
              till = self.non_fluid_event_list[0].time-1
          else:
            till = 8
  
          for i in range(0, till):
            self.hours_in_day[i] = 1
  
        self.updateUsableTime()
      else:
        if len(self.non_fluid_event_list) == 0:
          if len(self.non_fluid_event_list) != 0:
            till = 8
            if self.non_fluid_event_list[0].time < 8:
              till = self.non_fluid_event_list[0].time-1
          else:
            till = 8
            
          for i in range(0, till):
            self.hours_in_day[i] = 1

          self.updateUsableTime()
          
        # fluid event
        if event.duration_hr <= self.usable_time:
          for i in range(0, len(self.hours_in_day)):
            if self.hours_in_day[i] == 0:
              event.time = i
              self.hours_in_day[i] = 1
              break
          self.fluid_event_list.append(event)
        
      self.updateUsableTime()
      break