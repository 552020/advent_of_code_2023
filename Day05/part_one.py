# pylint: disable-all

lines = []
seed = []
destination_range_start = 0
source_range_start = 0
range_length = 0
seed_maps = []
seed_map = {
    "seed": 0,
    "soil": 0,
    "fertilizer": 0,
    "water": 0,
    "light": 0,
    "temperature": 0,
    "humidity": 0,
    "location": 0,
}


def extract_seeds(line, seed_map):
    if line.split(":")[0] == "seeds":
        seeds = line.split(":")[1].split(" ")
        seeds_len = len(seeds)
        print("seeds_len: ")
        print(seeds_len)
        for idx, seed in enumerate(seeds):
            seed = seed.strip()
            print("idx: ", idx)
            if seed != "":
                print("seed: ")
                print(seed)
                tmp = seed_map.copy()
                tmp["seed"] = int(seed)
                seed_maps.append(tmp)
    print("Exits extract_seeds")


def assign_map_values(line, seed_map, key):
    if line.strip() == "":
        return
    destination_range_start = int(line.split()[0].strip())
    source_range_start = int(line.split()[1].strip())
    range_length = int(line.split()[2].strip())
    for idx in range(range_length):
        for seed_map in seed_maps:
            if seed_map["seed"] == source_range_start + idx:
                seed_map[key] = destination_range_start + idx


def create_seed_maps(lines, seed_map):
    print("create_seed_maps")
    in_soil = False
    in_fertilizer = False
    in_water = False
    in_light = False
    in_temperature = False
    in_humidity = False
    in_location = False

    for line in lines:
        extract_seeds(line, seed_map)
        if line.strip() == "seed-to-soil map:":
            in_soil = True
            continue
        if in_soil:
            assign_map_values(line, seed_map, "soil")
        if line.strip() == "seed-to-fertilizer map:":
            in_fertilizer = True
            in_soil = False
            continue
        if in_fertilizer:
            assign_map_values(line, seed_map, "fertilizer")
        if line.strip() == "seed-to-water map:":
            in_water = True
            in_fertilizer = False
            continue
        if in_water:
            assign_map_values(line, seed_map, "water")
        if line.strip() == "seed-to-light map:":
            in_light = True
            in_water = False
            continue
        if in_light:
            assign_map_values(line, seed_map, "light")
        if line.strip() == "seed-to-temperature map:":
            in_temperature = True
            in_light = False
            continue
        if in_temperature:
            assign_map_values(line, seed_map, "temperature")
        if line.strip() == "seed-to-humidity map:":
            in_humidity = True
            in_temperature = False
            continue
        if in_humidity:
            assign_map_values(line, seed_map, "humidity")
        if line.strip() == "seed-to-location map:":
            in_location = True
            in_humidity = False
            continue
        if in_location:
            assign_map_values(line, seed_map, "location")
            in_location = False


def find_lowest_location(seed_maps):
    lowest_location = 0
    for seed_map in seed_maps:
        if seed_map["location"] > lowest_location:
            lowest_location = seed_map["location"]
    return lowest_location


with open("input_files/input_one.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

create_seed_maps(lines, seed_map)
lowest_location = find_lowest_location(seed_maps)
print("lowest_location: ", lowest_location)
