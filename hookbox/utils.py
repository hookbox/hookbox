import datetime

def get_now():
  return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
