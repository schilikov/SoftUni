for hours in range(24):
    for min in range(60):
        if hours < 10:
            if min < 10:
                print(f"0{hours}:0{min}")
            else:
                print(f"0{hours}:{min}")
        else:
            if min < 10:
                print(f"{hours}:0{min}")
            else:
                print(f"{hours}:{min}")