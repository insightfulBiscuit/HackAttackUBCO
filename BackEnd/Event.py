class Event:
  # Initializer method to set up an event object with all necessary attributes.
  def __init__(self, name, due_date, time, typeof, importance, duration_hr, fluid, 
               reminder_time_hr=0, location="null", urgency=0):
      self.name = name  # Event name
      self.due_date = due_date  # Stored as DDMMYYYY
      self.time = time  # Time of the event
      self.typeof = typeof  # Type of the event (e.g., Academic, Wellbeing, Social)
      self.location = location  # Location of the event
      self.urgency = urgency  # Urgency of the event, on a scale of 0-10
      self.importance = importance  # Importance of the event, on a scale of 1-10
      self.precedence = self.urgency * self.importance  # Calculated precedence for sorting
      self.duration_hr = duration_hr  # Duration of the event in hours
      self.reminder_time = reminder_time_hr  # Reminder time for the event
      self.fluid = fluid

   # Representation method to output the details of an event instance.
  def __str__(self):
    return (f"Name: {self.name}\n, Due Date: {self.due_date}\n, Time: {self.time}\n, Type: {self.typeof}\n, Importance: {self.importance}\n, Duration: {self.duration_hr} hours\n, Reminder Time: {self.reminder_time}\n, Location: {self.location}\n, Urgency: {self.urgency}\n, Fluid: {self.fluid}\n, Precedence: {self.precedence}")