class Day:
    def __init__(self,date):
        self.date = date
        self.section = ''
        self.topic = ''
        self.readings = []
        self.assignments = []

    def lecture(self,section,topic=None):
        self.section = section
        self.topic = topic
        
    def reading(self,text,link=None):
        if link:
            self.readings.append('<a href="%s">%s</a>' % (link,text))
        else:
            self.readings.append(text)

    def assignment(self,text,link=None):
        if link:
            self.assignments.append('<a href="%s">%s</a>' % (link,text))
        else:
            self.assignments.append(text)

class Week:
    def __init__(self,number):
        self.number = number
        self.days = []

    def day(self,d):
        self.days.append(d)

class Schedule:
    def __init__(self):
        self.weeks = []
        self.current_week = None
        self.number = 1

    def week(self):
        self.current_week = Week(self.number)
        self.number += 1
        self.weeks.append(self.current_week)

    def day(self,date):
        d = Day(date)
        self.current_week.day(d)
        return d
