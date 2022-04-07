import glob
import json

ranks = [
    {
        "Name": "420Boi",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Abbot the Astro Boy",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Albus the Astro Boy",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Alfredo the Astro Boy",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Alien Boy 1",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Alien Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Andy the Astro Boy",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Angel Dove Dio",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Anthony",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Antonio Saia",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Antonious the Astro Boy",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Antony the Astro Boy",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Arbok the Astro Boy",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Archer the Astro Boy",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Arthur the Astro Boy",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Atlantian Boy 1",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Azlan the Astro Boy",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Baby Huey",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Baffle the Buccaneer",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Baker",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Balthazar the Buccaneer",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Barabas",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Barbosa",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Barfo the Clown",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Bart",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Batman",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Beepo The Clown",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Bert",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Biff the Buccaneer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Bill the Buccaneer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Blake",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Bloodbath McGrath",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Bluebeard",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Boneless Joe",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Bones",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Boris the Buccaneer",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Borrasco",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Bounty Hunters Space Guild",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Bozo the Buccaneer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Bran",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Brandon the Buccaneer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Branson",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Brisco the Buccaneer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Britton",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Bryan",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Bryson",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Bulwark",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Byron",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Calvin",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Chad",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Christopher",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Connor",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Crimson Wraith",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Cyber Villainz",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Cynova Genesis",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Dante the War Weary",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Death Wraith",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Deep Sea Diver Dan",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Deep Sea Diver David",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Deep Sea Diver Dax",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Deep Sea Diver Dick",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Deep Sea Diver Dill",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Deep Sea Diver Dom",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Deep Sea Diver Doug",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Deep Sea Diver Doyle",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Deep Sea Diver Draven",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Deep Sea Diver Dylan",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Demon Bird Damian.kpg",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Demon Wraith",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Dilbert the Dry",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Doge Track",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Donatello",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Dystopian Wraith",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "EcoBots",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Edward Scissorhands",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Egbert the Earthbound",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Empty Wraith",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Ezio",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Farthing the Frog Pirate",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Fathoms the Frog Pirate",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Filbert the Flame",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Finn",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Finneas the Frog Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Fisk the Frog Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Fjord",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Flerkin the Flame Wizard",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Flip the Frog Pirate",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Flit the Frog Pirate",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Floki",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Florida Man 1",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Florida Man 2",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Florida Man Hippie Man",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Florida Man Serial Killer",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Flynn the Frog Pirate",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Founders Halo Spartan",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Francesco the Frog Pirate",
        "trait": "Legendary",
        "rank": 2
    },
    {
        "Name": "Frank the Frog Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Franken Boy",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Freddy Krueger",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Frig the Frog Pirate",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Galley the Great White",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Gelly the Ghost",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Georgie Porgie",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Gerald the Ghost",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Geraldo the Ghost",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Geralt the Ghost",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Gey the Goblin",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Gilbert the Grey",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Gilmer the Great White",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Giuseppe the Wise",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Glenn the Ghost",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Glib the Goblin",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Glitter Beard Cold Summer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Glitter Beard Endless Summer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Glitter Beard Noir Summer",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Glitter Beard Toxic Summer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Glitter Beard Zombie Summer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Glowboy the Ghost",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Gnash the Great White",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Gnasher the Goblin",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Gob the Goblin",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Godfrey the Grizzled",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Gold Mobster",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Gold Pirate",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Goo Man 1",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Goo Man 2",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Goo Man 3",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Goo Man 4",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Goo Man 5",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Goo Man Rainbow",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Goop the Great White",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Grape Wraith",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Greg the Great White",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Gregory the Gracious",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Grimace the Ghost",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Grimer the Ghost",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Grimley the Ghast",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Grimm the Goblin",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Grog the Goblin",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Gruff the Goblin",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Grug the Goblin",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Gucci the Ghost",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Guk the Goblin",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Gus the Ghost",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Guy the Ghost",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Gym the Goblin",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Hollywood Hogan",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Horvath the Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Hulkamania Hogan",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Hytham",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Ishmael",
        "trait": "Legendary",
        "rank": 1
    },
    {
        "Name": "Iupati",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Ivan",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Ivar",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Jimboy the Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Kahn the Knight",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Kasper the Knight",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Kavinsky the Knight",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Keith the Knightjpg",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Kevin the Knight",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Killjoy the Knight",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Kilmer",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Kilroy the Knight",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Kip the Knight",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Klimt",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Klugh the Knight",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Koffey the Knight",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Kramer",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Kraven",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Kyle",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Lad the Lynx",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Lancelot the Lynx",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Laser Bird Lance",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Lav the Lynx",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Lavar the Lynx",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Leonardo",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Lex the Lynx",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Link the Lynx",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Lion Cat",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Lou the Lynx",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Lucipurr the Lynx",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Lucky the Lynx",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Luke the Lynx",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Marky the Macaw",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Match Hogan",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Maui",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Michael Myers",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Michaelangelo",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Monke Crew",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Nemo",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Neo Bird Neo",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Nyan Cat",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "O the Tentacle",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "O'Hara the Otter",
        "trait": "Legendary",
        "rank": 2
    },
    {
        "Name": "O'Leary the Otter",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "O'Malley",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Octagon the Tentacle",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Octahedron the Octopus",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Octavius the Otter",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Octopus 1",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Oculus the Tentacle",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Office Space Octopus 1",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Office Space Octopus 2",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Office Space Octopus 3",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Office Space Octopus 4",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Office Space Octopus 5",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Ofram the Tentacle",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Ogg the Tentacle",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Olaf the Tentacle",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Oliver the Otter",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Ooze the Octopus",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Oppenheim the Tentacle",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Orel the Oriole",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Oren the Tentacle",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Orfi the Octopus",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Orville the Tentacle",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Oscar the Otter",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Osgar the Tentacle",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Osmo the Otter",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Oswald the Otter",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Othello the Otter",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Otto the Otter",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Ottoman the Otter",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Oui the Octopus",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Pancake Astronaut",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Panda Patrol",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Parakeet Pete",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Pascal the Pidgeon",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Paulo the Paladin",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Peacock Paulie",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Peter the Paladin",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Pietro the Paladin",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Pip the Paladin",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Pirate Parrot Gaston",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Pirate Parrot Pascal",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Pirate Parrot Paul",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Pirate Parrot Petey",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Plague Doctor 1",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Plague Doctor 2",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Plague Doctor 3",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Plague Doctor Bloody",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Plague Doctor Crimson",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Plague Doctor Gold",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Plague Doctor Green Screen",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Plague Doctor Silver",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Pogo the Paladin",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Prince the Paladin",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Prog the Paladin",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Prometheus the Paladin",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Prospector the Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Puck the Paladin",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Puritan Plague Doctor 1",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Puritan Plague Doctor 2",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Puritan Plague Doctor 3",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Puritan Plague Doctor Paul",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Puritan Plague Doctor Pete",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Pyre the Paladin",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Raphael",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Rasco the Raven Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Remley the Raven Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Retro Wraith",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Riley the Raven Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Robot Mafia Club",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Rolando the Raven Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Rosco",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Royal Lion",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Sam the Skeleton",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Samuel the Alien",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Sandy Claws",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Sarfu the Skeleton",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Scabard the Skeleton",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Scott the Alien",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Seagull Sam",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Sean the Skeleton",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Sewer Wraith",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Shizen Oroshi",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Sid the Skeleton",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Silent Bob",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Silver Mobster",
        "trait": "Mythic",
        "rank": 3
    },
    {
        "Name": "Silver Pirate",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Skelly the Skeleton",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Skull the Skeleton",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Skyler the Alien",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Sniper Dao",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Solizen Wizard",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Sonny",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Souza the Skeleton",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Stan",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Steve the Alien",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "SteveOh the Clown",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Suchīmusōdo",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Suffolk the Skeleton",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Sulyman the Skeleton",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Sven",
        "trait": "Legendary",
        "rank": 1
    },
    {
        "Name": "Swamp Wraith",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Taco Cat",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "The Daku Reaper",
        "trait": "Rare",
        "rank": 4
    },
    {
        "Name": "The Doctor",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "The Dude",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "The Invisible Person",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "The Mummy",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "The Scream Ghoul",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Travis the Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Turnt Up Tikis",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Tyrell the Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "U~ōtāsōdo",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "UBIK Angel",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "UBIK Devil",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Ulysses the Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Vito",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Volstead",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Waldo Noir",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Waldo",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Whisker the Howling Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Whistler the Howling Pirate",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Wilbert the White",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Wilhelm the Howling Pirate",
        "trait": "Epic",
        "rank": 3
    },
    {
        "Name": "Willie the Howling Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Windhand the Howling Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Wolfheart the Howling Pirate",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Wolfram the Howling Pirate",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Wombat the Howling Pirate",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Wovenhand the Howling Pirate",
        "trait": "Mythic",
        "rank": 3
    },
    {
        "Name": "Wraith",
        "trait": "Legendary",
        "rank": 4
    },
    {
        "Name": "Wylie the Howling Pirate",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Xin Dragon",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Yukidaruma",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Yume Glitterflys",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Zaysan Raptors",
        "trait": "Mythic",
        "rank": 4
    },
    {
        "Name": "Zombee",
        "trait": "Rare",
        "rank": 2
    },
    {
        "Name": "Zombi",
        "trait": "Mythic",
        "rank": 3
    },
    {
        "Name": "Zombi3",
        "trait": "Uncommon",
        "rank": 1
    },
    {
        "Name": "Zombie Horde",
        "trait": "Legendary",
        "rank": 4
    }
]


def write_json(rank_info, rank_data, new_image_name, filename):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside attributes
        file_data['name'] = rank_info["Name"]
        file_data["image"] = new_image_name
        file_data["attributes"].append({
            "trait_type": "Rank",
            "value": rank_info["trait"]
        })
        file_data["properties"]["files"].append(rank_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
        print("DONE 1>>", file_data["attributes"])


for i in range(len(ranks)):
    print('START AT {n}'.format(n=i))
    write_json(ranks[i], {
        "uri": "{n}.png".format(n=i),
        "type": "image/png"
    }, "{n}.png".format(n=i), "fixed-json/{n}.json".format(n=i))
    # break
