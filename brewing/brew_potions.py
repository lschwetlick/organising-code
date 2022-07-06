from brewing import potion_class
from brewing import containers
from brewing import cooking
from brewing import inspection


def make_example_potion(name):

    print("creating example potion")
    my_potion = potion_class.Potion(name=name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)

    return my_potion


def make_python_expert_potion(name):
    """Cook an expert potion.

    Cook an expert potion according to the recipe provided by the function and
    let it simmer.

    Parameters
    ----------
    name : str
        Name of the potion to make.

    Returns
    -------
    potion_class.Potion
        Potion.
    """
    print("I am a Python Expert")
    my_potion = potion_class.Potion(name=name)
    my_potion.add_ingredients(['fish_eyes', 'tea_leaves', 'unicorn_hair'])
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=2)

    return my_potion


if __name__ == "__main__":
    my_name = 'GSN student'
    # my_potion = make_example_potion(my_name)
    my_potion = make_python_expert_potion(my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')


