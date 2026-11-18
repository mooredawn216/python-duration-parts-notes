

def solve(value):
    return {"days": value//86400, "hours": value%86400//3600, "minutes": value%3600//60, "seconds": value%60} if isinstance(value, int) and value >= 0 else (_ for _ in ()).throw(ValueError("nonnegative integer required"))
