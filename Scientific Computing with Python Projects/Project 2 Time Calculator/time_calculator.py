def add_time(start, duration, d=None):

  [startinput, period] = start.split()
  [sh, sm] = startinput.split(':')
  [dh, dm] = duration.split(':')
  if d != None:
    day = d.capitalize()
  [sh, sm, dh, dm] = [int(sh), int(sm), int(dh), int(dm)]
  week = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}

  # how many days are added to the start time?
  days = 0
  if dh >= 24:
    durdays = int(dh/24)
    days += durdays
    dh -= durdays * 24

  newh = sh + dh
  newm = sm + dm

  # add 1h if total minutes > 59min
  if newm > 59:
    plush = 1
    newh += plush
    newm = newm%60

  # if hours surpass 11:59 switch format to 12, 1, 2, 3, etc, again
  if sh <= 12 and newh >= 12:
    newh -= 12
    if newh == 0:
      newh = 12

  # period switch when the hours surpass 11:59
    if sh == 12 and dh == 0 and dm != 0:
      period = period
    else:
      if period == 'AM':
        period = 'PM'
      else:
        period ='AM'
        days += 1

  #convert into correct string format
  newh = str(newh)
  newm = str(newm)
  if len(newm) == 1:
    newm = '0' + newm
  
  # get the right day the correct day, if more than 24h are added to the start time
  if d != None:
    days_converted = days%7
    index = week[day] + days_converted
    if index > 7:
      index -= 7
    print(index)
    day = list(week.keys())[list(week.values()).index(index)]

  #construct the return string depending on input
  if days == 0:
    if d != None:
      new_time = newh + ':' + newm + f' {period}' + f', {day}'
    else:
      new_time = newh + ':' + newm + f' {period}'
  else:
    if days == 1:
      days = 'next day'
    else:
      days = str(days) + ' days later'
    if d != None:
      new_time = newh + ':' + newm + f' {period}' + f', {day}' + f' ({days})'
    else:
      new_time = newh + ':' + newm + f' {period}' + f' ({days})'
    
  return new_time

# print(add_time("2:59 AM", "24:00", "saturDay"))