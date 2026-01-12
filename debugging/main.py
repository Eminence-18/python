def take_magic_damage(health, resist, amp, spell_power):
    maximum_damage = spell_power * amp
    damage_dealt = maximum_damage - resist
    return health - damage_dealt


def test():
    health = 100
    resist = 5
    amp = 2
    spell_power = 20
    
    result = take_magic_damage(health, resist, amp, spell_power)
    print(f"Resulting health: {result}")


if __name__ == "__main__":
    test()

