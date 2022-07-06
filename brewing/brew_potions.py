import potion_class
import containers
import cooking
import inspection


def make_example_potion(name):

    print("creating example potion")
    my_potion = potion_class.Potion(name=name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)

    return my_potion


def make_python_expert_potion(name):
    print("I am a Python Expert")
    # todo: write this function!
    my_potion = potion_class.Potion(name=name)
    my_potion.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    my_potion.add_ingredients(["fish_eyes","unicorn_hair","tea_leaves"])
    cooking.simmer(my_potion, 2)

    return my_potion


if __name__ == "__main__":
    my_name = 'GSN student'
    my_potion = make_python_expert_potion(my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')


