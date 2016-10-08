from datetime import datetime
import copy


def compare_dates(date1, date2):
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        return 0


def compare_end_dates(date1, date2):
    if date1 and date2:
        return compare_dates(date1, date2)
    elif date1:
        return -1
    elif date2:
        return 1
    else:
        return 0


def has_started(date):
    return date is not None and date < datetime.now()


def compare_start_dates(date1, date2):
    # (presence(1), presence(2), started(1), started(2)) -> result
    truth_table = [
        [(True, True, True, True), 0],
        [(True, True, True, False), -1],
        [(True, True, False, True), 1],
        [(False, True, False, True), 1],
        [(False, True, False, False), -1],
        [(True, False, True, False), -1],
        [(True, False, False, False), 1],
        [(False, False, False, False), 0],
    ]

    truth_test = (date1 is not None, date2 is not None, has_started(date1), has_started(date2))
    for t in truth_table:
        if truth_test == t[0]:
            return t[1]
    return compare_dates(date1, date2)


def compare_active(active1, active2):
    if active1 and active2:
        return 0
    if not active1 and not active2:
        return 0
    if active1:
        return -1
    if active2:
        return 1


def compare_presence(k1, k2):
    truth_test = (k1 is not None, k2 is not None)
    for t in Task.presence_comparator:
        if truth_test == t[0]:
            return t[1]


def compare_priority(priority1, priority2):
    if not priority1 and not priority2:
        return 0
    if priority1 and not priority2:
        return -1
    if not priority1 and priority2:
        return 1
    if priority1 > priority2:
        return -1
    if priority1 < priority2:
        return 1
    return 0


class Task:
    comparators = [
        ('active', compare_active),
        ('priority', compare_priority),
        ('daily', compare_presence),
        ('end', compare_end_dates),
        ('start', compare_start_dates),
        ('creation', compare_dates),
    ]

    presence_comparator = [
        [(True, True), 0],
        [(True, False), -1],
        [(False, True), 1],
        [(False, False), 0],
    ]


    def __init__(self, **kwargs):
        self.props = {}
        self.props.update(kwargs)
        if not self.props.has_key('creation'):
            self.props['creation'] = datetime.now()


    def __getitem__(self, item):
        if item == 'active':
            return self.is_active()
        try:
            return self.props[item]
        except:
            return None


    def __setitem__(self, key, value):
        if key != 'active':
            self.props[key] = value


    def __cmp__(self, other):
        for k, compare in Task.comparators:
            value = compare(self[k], other[k])
            if value != 0:
                return value
        return 0


    def is_active(self):
        if not self['start']:
            return True
        now = datetime.now()
        if self['start'] > now:
            return False
        if not self['daily']:
            return True
        if self['daily']['start'].hour > now.hour:
            return False
        if self['daily']['end'].hour < now.hour:
            return False
        if self['daily']['start'].minute > now.minute:
            return False
        if self['daily']['end'].minute < now.minute:
            return False
        return True


    def as_dict(self):
        ret = {}
        for k in self.props.keys():
            ret[k] = str(self[k])
        ret['active'] = self['active']
        return ret
