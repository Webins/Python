def eat(food, is_healthy):
    if isinstance(is_healthy,bool) == False:
        raise ValueError("Argument must be a boolean")

    if is_healthy:
        return f"I'm eating {food} because is healthy"
    
    return f"I'm eating {food} because is delicious"

def nap(num_hours):
    if num_hours > 2:
        return "I'm feeling refreshed. But I sleep too much"
    return f"I'm feeling refreshed after my 1 hour nap"
    pass