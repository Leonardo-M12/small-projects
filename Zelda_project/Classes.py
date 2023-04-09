"""Contains the classes Location and Link.
"""

import time


class Location:
    """Defines a location in the game. Every location (which will be classes)
       will inherit from the Location class. Each location has:

       - Code name: the name with which the other classes 
         identify this location.

       - Description: what the user is shown about the place. 

       - Adjacent locations: a dictionary that contains 
         all the adjacent locations to the current one.

       - Story (if applicable): series of text that display some story.

       - Input function: function that acts when the user 
         is giving some input while Link is in this class. The function
         that actually starts the input is in main.
       
       Each class will have its own code, since they inherit from Location,
       but different code is needed (for example, in the Sacred Forest
       Meadow there is completely different code than in the Kokiri Forest,
       for example).

       Each location has a __repr__ method defined, since this is the name
       that will be shown to the user.
    """
    
    def __init__(self, *, code_name: str, description: str, adj_places: dict):
        self.code_name = code_name
        self.description = description
        self.adj_places = adj_places

    
    # It's better to treat these ones as class attributes, so they are 
    # shared by all subclasses of Location, and we don´t get in trouble
    # with instance attributes.
    right_way = "The intensity of the song increases."
    wrong_way = "The intensity of the song decreases."
    no_message = ''


class KokiriForest(Location):
    """The Kokiri Forest, where Link begins his adventure.
    """

    def __init__(self):
        super().__init__(
            code_name="KF",
            description="There is a wooden tunnel going north.",
            adj_places={
                "north": ("LW-1", self.no_message)
            }
        )

    def __repr__(self):
        return "Kokiri Forest"

    def intro(self):
        """Prints the narrative at the beginning of the game."""

        print("""
It was a day like any other in Hyrule, except for one thing. Link 
knew he had to launch into adventure again when he listened a strangely 
familiar song, as if it was calling him. His friend, Navi, who had met Link 
again after all what happened, decided to go with him.

They had to go to Kokiri Forest, and then head into the Lost Woods, which 
was the source of the song.
""")

        return None


class LostWoods1(Location):
    """The entrance to the Lost Woods.
    """

    def __init__(self):
        super().__init__(
            code_name="LW-1",
            description="""
There are wooden tunnels going north, south, east and west. A song playing 
in the background sounds familiar to Link.
""",
            adj_places={
                "north": ("KF", self.wrong_way),
                "south": ("KF", self.no_message),
                "east": ("LW-2", self.right_way),
                "west": ("KF", self.wrong_way)
            }
        )

    def __repr__(self):
        return "Lost Woods"


class LostWoods2(Location):

    def __init__(self):
        super().__init__(
            code_name="LW-2",
            description="""
There are wooden tunnels going north, south and west. There are more trees 
in the east direction, but they are down a cliff and seem unaccesible. 
A song playing in the background sounds familiar to Link.
""",
            adj_places={
                "north": ("LW-3", self.right_way),
                "south": ("KF", self.wrong_way),
                "west": ("LW-1", self.no_message)
            }
        )

    def __repr__(self):
        return "Lost Woods"


class LostWoods3(Location):

    def __init__(self):
        super().__init__(
            code_name="LW-3",
            description="""
To the north, there is a passage whose entrance is decorated with a stone 
frame. Also, there are wooden tunnels going south, east and west.
A song playing in the background sounds familiar to Link.
""",
            adj_places={
                "north": ("GC", self.no_message),
                "south": ("LW-2", self.no_message),
                "east": ("LW-4", self.right_way),
                "west": ("KF", self.wrong_way)
            }
        )

    def __repr__(self):
        return "Lost Woods"


class GoronCity(Location):

    def __init__(self):
        super().__init__(
            code_name="GC",
            description="""
Huge rocks block the road and you have no bombs.
However, you hear the sound of angry Gorons behind those rocks.
It seems better to go away by the passage at south.
""",
            adj_places={
                "south": ("LW-3", self.no_message)
            }
        )

    def __repr__(self):
        return "Goron City"


class LostWoods4(Location):

    def __init__(self):
        super().__init__(
            code_name="LW-4",
            description="""
There are wooden tunnels going north, south, and west. There is a little 
pond with an underwater passage, but Link doesn't feel like diving right now.
A song playing in the background sounds familiar to Link.
""",
            adj_places={
                "north": ("LW-5", self.right_way),
                "south": ("KF", self.wrong_way),
                "west": ("LW-3", self.no_message)
            }
        )

    def __repr__(self):
        return "Lost Woods"


class LostWoods5(Location):

    def __init__(self):
        super().__init__(
            code_name="LW-5",
            description="""
There are wooden tunnels going north, south, east and west.
A song playing in the background sounds familiar to Link.
""",
            adj_places={
                "north": ("LW-6", self.right_way),
                "south": ("LW-4", self.no_message),
                "east": ("KF", self.wrong_way),
                "west": ("KF", self.wrong_way)  
            }
        )

    def __repr__(self):
        return "Lost Woods"


class LostWoods6(Location):

    def __init__(self):
        super().__init__(
            code_name="LW-6",
            description="""
There are wooden tunnels going north, south, east and west.
A song playing in the background sounds familiar to Link.
""",
            adj_places={
                "north": ("KF", self.wrong_way),
                "south": ("LW-5", self.no_message),
                "east": ("KF", self.wrong_way),
                "west": ("LW-7", self.right_way)
            }
        )

    def __repr__(self):
        return "Lost Woods"


class LostWoods7(Location):

    def __init__(self):
        super().__init__(
            code_name="LW-7",
            description="""
There are wooden tunnels going north, south, east and west.
A song playing in the background sounds familiar to Link.
""",
            adj_places={
                "north": ("SFM", self.right_way),
                "south": ("KF", self.wrong_way),
                "east": ("LW-6", self.no_message),
                "west": ("KF", self.wrong_way)
            }
        )

    def __repr__(self):
        return "Lost Woods"


class SacredForestMeadow(Location):
    """The last location in the map, where Link finishes his adventure.
       When Link arrives here, its code will be executed, and the game
       ends.
    """

    def __init__(self):
        super().__init__(
            code_name="SFM",
            description="""
A forest clearing, in which lies the Forest Temple.
The song playing in the background intensifies.
""",
            adj_places={
                "south": ("LW-7", self.no_message)
            }
        )

    def __repr__(self):
        return "Sacred Forest Meadow"

    def ending(self):
        """Prints the ending narrative."""

        print(
"""After some time, Link and Navi finally arrive to the Sacred Forest Meadow.
When they crossed the maze in there, they arrived to the Forest Temple, which
they already visited during their quest. 

No one was there.
""")

        time.sleep(5)

        print(
"""However, there was the source of the song, which they already had 
recognized: it was Saria's song.

Link remembered everything he lived with her, and he instantly felt sad.

\"Don't worry, Link. We will always be friends.\"

\"Continue being as strong as you are. Keep fighting, Hero of Time.
I will always be there to help you.\"

Link hadn't even finished processing Saria's words when a Darknut came from
inside the temple.
""")

        time.sleep(5)

        print(
"""With no other option, Link proceeded to fight it. But soon after destroying
its armor, a beam of green light came from the sky and hit the Darknut,
finishing it.

Link looked to the sky, and smiled.
""")

        time.sleep(5)

        print(
"""Then he remembered how he threw Saria's ocarina to the trash after he got
the Ocarina of Time.
"""
)
        return None


class Link:
    """The protagonist of the game. He is only able to move between
       places.
       Attributes:
       - Name: classes and the user will recognize him as "Link".
       - Location: Link's current location.
         NOTE: His current location is specified with the code name
         of each Location subclass.
         NOTE: When Link is instantiated first time, he appears
         in Kokiri Forest automatically.
    """

    def __init__(self):
        self.name = "Link"
        self.location = KokiriForest()