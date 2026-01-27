def get_most_common_enemy(enemies_dict):
    if not enemies_dict:
        return None
    return max(enemies_dict, key=enemies_dict.get)

