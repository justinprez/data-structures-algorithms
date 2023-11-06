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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not user:
        return False
    elif user in group.get_users():
        return True
    else:
        for subgroup in group.get_groups():
            if is_user_in_group(user, subgroup):
                return True
    return False


## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1
print(is_user_in_group('sub_child_user', parent))  # True

## Test Case 2
print(is_user_in_group('', parent))  # False

## Test Case 3
parent.add_user('parent_user')
print(is_user_in_group('parent_user', parent))  # True

## Test Case 4
print(is_user_in_group('parent_user', child))  # False

## Test Case 5
grandchild = Group("grandchild")
grandchild_user = "grandchild_user"
grandchild.add_user(grandchild_user)
child.add_group(grandchild)

print(is_user_in_group('grandchild_user', parent))  # True