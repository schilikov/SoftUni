starth = int(input())
startm = int(input())
arriveh = int(input())
arrivem = int(input())

if 0 <= ((60 * starth + startm)-(60 * arriveh + arrivem)) <= 30:
    print("On time")
    if ((60 * starth + startm)-(60 * arriveh + arrivem)) > 0:
        print(f"{((60 * starth + startm)-(60 * arriveh + arrivem))} minutes before the start.")

elif ((60 * starth + startm)-(60 * arriveh + arrivem)) > 30:
    print("Early")
    if ((60 * starth + startm)-(60 * arriveh + arrivem)) < 60:
        print(f"{((60 * starth + startm)-(60 * arriveh + arrivem))} minutes before the start.")
    else:
        hours = ((60 * starth + startm)-(60 * arriveh + arrivem)) // 60
        minutes = ((60 * starth + startm)-(60 * arriveh + arrivem)) % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours before the start.")
        else:
            print(f"{hours}:{minutes} hours before the start.")

elif ((60 * starth + startm)-(60 * arriveh + arrivem)) < 0:
    print("Late")
    if abs(((60 * starth + startm)-(60 * arriveh + arrivem))) < 60:
        print(f"{abs(((60 * starth + startm)-(60 * arriveh + arrivem)))} minutes after the start")
    else:
        hours = abs(((60 * starth + startm)-(60 * arriveh + arrivem))) // 60
        minutes = abs(((60 * starth + startm)-(60 * arriveh + arrivem))) % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start.")
        else:
            print(f"{hours}:{minutes} hours after the start.")