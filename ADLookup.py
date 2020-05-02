class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not isinstance(group, Group):
        return False
    found = _is_user_in_group(user, group)
    return found
    # First see if user is part of the users list in that group

def _is_user_in_group(user, group):
    if user in group.users:
        return True
    else:
        for sub_group in group.groups:
            found = is_user_in_group(user, sub_group)
            if found:
                return True
            else:
                continue
        return False

def test1():
    students = Group("students")
    physics = Group("physics")
    quantum = Group("quantum")
    relativity = Group("relativity")
    students.add_group(physics)
    physics.add_group(relativity)
    physics.add_group(quantum)
    biology = Group("Biology")
    molecular = Group("molecular")
    virus = Group("virus")
    anatomy = Group("anatomy")
    molecular.add_group(virus)
    biology.add_group(molecular)
    biology.add_group(anatomy)
    students.add_group(biology)
    sports = Group("sports")
    students.add_group(sports)
    students.add_user("Fred")
    students.add_user("Tom")
    students.add_user("Mary")
    physics.add_user("Jeff")
    physics.add_user("Kate")
    quantum.add_user("Max")
    relativity.add_user("Albert")
    relativity.add_user("Richard")
    biology.add_user("Margaret")
    biology.add_user("Tom")
    anatomy.add_user("Oli")
    anatomy.add_user("John")
    virus.add_user("Elizabeth")

    assert(is_user_in_group("Fred", students) is True)
    assert(is_user_in_group("Jeremy", students) is False)
    assert(is_user_in_group("Max", physics) is True)
    assert(is_user_in_group("Max", students) is True)
    assert(is_user_in_group("Max", quantum) is True)
    assert(is_user_in_group("Max", biology) is False)
    assert(is_user_in_group("Richard", physics) is True)
    assert(is_user_in_group("Albert", relativity) is True)
    assert(is_user_in_group("Tom", students) is True)
    assert(is_user_in_group("Mary", students) is True)
    assert(is_user_in_group("Jeff", physics) is True)
    assert(is_user_in_group("Kate", biology) is False)
    assert(is_user_in_group("Oli", biology) is True)
    assert(is_user_in_group("Oli", molecular) is False)
    assert(is_user_in_group("Oli", anatomy) is True)
    assert(is_user_in_group("John", sports) is False)
    assert(is_user_in_group("Tom", students) is True)
    assert(is_user_in_group("Tom", biology) is True)
    assert(is_user_in_group("Tom", anatomy) is False)
    assert(is_user_in_group("Elizabeth", students) is True)
    assert(is_user_in_group("Elizabeth", biology) is True)
    assert(is_user_in_group("Elizabeth", virus) is True)
    assert(is_user_in_group("Elizabeth", anatomy) is False)
    assert(is_user_in_group("Elizabeth", 'karate') is False)
    assert(is_user_in_group("Kate", sports) is False)

def test2():
    students = Group("students")
    physics = Group("physics")
    quantum = Group("quantum")
    relativity = Group("relativity")
    students.add_group(physics)
    physics.add_group(relativity)
    physics.add_group(quantum)
    biology = Group("Biology")
    molecular = Group("molecular")
    virus = Group("virus")
    anatomy = Group("anatomy")
    molecular.add_group(virus)
    biology.add_group(molecular)
    biology.add_group(anatomy)
    students.add_group(biology)
    sports = Group("sports")
    students.add_group(sports)
    students.add_user("Fred")
    students.add_user("Tom")
    students.add_user("Mary")
    physics.add_user("Jeff")
    physics.add_user("Kate")
    quantum.add_user("Max")
    relativity.add_user("Albert")
    relativity.add_user("Richard")
    biology.add_user("Margaret")
    biology.add_user("Tom")
    anatomy.add_user("Oli")
    anatomy.add_user("John")
    virus.add_user("Elizabeth")
    teachers = Group("teachers")
    mathematics = Group("mathematics")
    spanish = Group("spanish")
    teachers.add_group(mathematics)
    teachers.add_group(spanish)
    teachers.add_user("Dumbledore")
    teachers.add_user("Snape")
    mathematics.add_user("Mcgonagall")
    spanish.add_user("Sprout")

    assert(is_user_in_group("Dumbledore", teachers) is True)
    assert(is_user_in_group("Sprout", students) is False)
    assert(is_user_in_group("Snape", physics) is False)
    assert(is_user_in_group("Harry", students) is False)
    assert(is_user_in_group("Mcgonagall", teachers) is True)
    assert(is_user_in_group("Mcgonagall", mathematics) is True)
    assert(is_user_in_group("Sprout", mathematics) is False)
    assert(is_user_in_group("Sprout", spanish) is True)
    assert(is_user_in_group("Tom", teachers) is False)
    assert(is_user_in_group("Sprout", teachers) is True)

def test3():
    students = Group("students")
    physics = Group("physics")
    quantum = Group("quantum")
    relativity = Group("relativity")
    students.add_group(physics)
    physics.add_group(relativity)
    physics.add_group(quantum)
    biology = Group("Biology")
    molecular = Group("molecular")
    virus = Group("virus")
    anatomy = Group("anatomy")
    molecular.add_group(virus)
    biology.add_group(molecular)
    biology.add_group(anatomy)
    students.add_group(biology)
    sports = Group(None)
    students.add_group(sports)
    students.add_user("Fred")
    students.add_user("Tom")
    students.add_user("Mary")
    physics.add_user("Jeff")
    physics.add_user("Kate")
    quantum.add_user("Max")
    relativity.add_user("Albert")
    relativity.add_user("Richard")
    biology.add_user("Margaret")
    biology.add_user("Tom")
    anatomy.add_user("Oli")
    anatomy.add_user("John")
    virus.add_user("Elizabeth")
    teachers = Group(12345)
    mathematics = Group("mathematics")
    spanish = Group("spanish")
    teachers.add_group(mathematics)
    teachers.add_group(spanish)
    teachers.add_user("Dumbledore")
    teachers.add_user("Snape")
    mathematics.add_user("Mcgonagall")
    spanish.add_user("Sprout")
    
    assert(is_user_in_group(None, teachers) is False)
    assert(is_user_in_group(123, students) is False)
    assert(is_user_in_group([1,2,3], physics) is False)
    assert(is_user_in_group("Harry", students) is False)
    assert(is_user_in_group("Mcgonagall", teachers) is True)
    assert(is_user_in_group("Mcgonagall", mathematics) is True)
    assert(is_user_in_group("Sprout", mathematics) is False)
    assert(is_user_in_group("Sprout", spanish) is True)
    assert(is_user_in_group("Tom", teachers) is False)
    assert(is_user_in_group("Sprout", teachers) is True)

test1()
test2()
test3()