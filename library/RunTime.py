"""
Ryan A. Colyer

Report process runtime.

"""

from datetime import datetime


class RunTime:
  def __init__(self):
    self.Start()

  def Start(self):
    self.start = datetime.now()

  def End(self):
    self.end = datetime.now()

  def Duration(self):
    return self.end - self.start

  def DurationStr(self):
    tlst = str(self.Duration()).split(':')
    return tlst[0] + 'h ' + tlst[1] + 'm ' + '{0:.2f}s'.format(float(tlst[2]))

  def SinceStart(self):
    self.End()
    return self.DurationStr()

