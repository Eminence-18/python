def main():
 for i in [1, 2, 3, 4, 5]:
     try:
            print(get_player_record(i))
     except Exception as e:
            print(f"player{i}not found: {e}")



# Don't edit below this line


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    if player_id == 5:
        return {"name": "Gandalf", "level": 5000}
    raise Exception("player id not found")


main()