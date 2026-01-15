

def check_mount_rental(time_used, time_purchased):
    result = "no charges yet"
    if time_used >= time_purchased:
     result = "overtime charged"

    print(result)
    return result
