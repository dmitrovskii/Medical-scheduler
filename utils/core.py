"""
Development, debug and other features
"""


def route(action_name, action_map):
    """
    Execute a function from dictionary or return boolean
    """
    func = action_map.get(action_name)
    if func: 
        func()
        return True
    else: 
        return False


