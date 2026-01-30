def get_player_record(player_id):

    try:
        player_id = int(player_id)
    except (ValueError, TypeError):
        print(f"player id not found:")



    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}


    raise Exception("player id not found")