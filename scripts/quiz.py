def safe_division(numerator, denominator):
    if denominator > 1:
        result = numerator / denominator
    else:
        result = numerator / 1
    return result

    print(safe_division(5,0))