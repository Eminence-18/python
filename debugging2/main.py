def unlock_achievement(before_xp, ach_xp, ach_name):
    new_player_xp = before_xp + ach_xp

    alert = f"ACHIEVEMENT UNLOCKED: {ach_name}"
    print(alert)
    return new_player_xp, unlock_achievement

def test():
    before_xp = 100
    ach_xp = 20
    ach_name= "speedster"


    return unlock_achievement(before_xp, ach_xp, ach_name)

if __name__ == "__main__":
    test()






