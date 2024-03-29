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
        seeds = line.split(":")[1].strip().split(" ")
        for seed in seeds:
            seed = seed.strip()
            if seed != "":
                tmp = seed_map.copy()
                tmp["seed"] = int(seed)
                seed_maps.append(tmp)


def assign_map_values(line, key_src, key_dest):
    stripped = line.strip()
    if stripped == "":
        return
    if not stripped[0].isdigit():
        return
    destination_range_start = int(line.split()[0].strip())
    source_range_start = int(line.split()[1].strip())
    range_length = int(line.split()[2].strip())
    for seed_map in seed_maps:
        update_flag_key = f"{key_dest}_updated"
        if not seed_map.get(update_flag_key):
            seed_map[update_flag_key] = False
        for idx in range(range_length):
            if seed_map[key_src] == source_range_start + idx:
                seed_map[key_dest] = destination_range_start + idx
                seed_map[update_flag_key] = True
                break
        if seed_map[update_flag_key] == False:
            seed_map[key_dest] = seed_map[key_src]


def create_seed_maps(lines, seed_map):
    print("create_seed_maps")
    in_soil = False
    in_fertilizer = False
    in_water = False
    in_light = False
    in_temperature = False
    in_humidity = False
    in_location = False

    extract_seeds(lines[0], seed_map)
    print("seed_maps: ", seed_maps)
    for line in lines:
        print("line: ", line)
        if line.strip() == "":
            continue
        if line.strip() == "seed-to-soil map:":
            in_soil = True
            continue
        if in_soil:
            print("in soil")
            print("line: ", line)
            assign_map_values(line, "seed", "soil")
        if line.strip() == "soil-to-fertilizer map:":
            print("in soil to fertilizer")
            print("line: ", line)
            in_fertilizer = True
            in_soil = False
            continue
        if in_fertilizer:
            assign_map_values(line, "soil", "fertilizer")
        if line.strip() == "fertilizer-to-water map:":
            in_water = True
            in_fertilizer = False
            continue
        if in_water:
            assign_map_values(line, "fertilizer", "water")
        if line.strip() == "water-to-light map:":
            in_light = True
            in_water = False
            continue
        if in_light:
            assign_map_values(line, "water", "light")
        if line.strip() == "light-to-temperature map:":
            in_temperature = True
            in_light = False
            continue
        if in_temperature:
            assign_map_values(line, "light", "temperature")
        if line.strip() == "temperature-to-humidity map:":
            in_humidity = True
            in_temperature = False
            continue
        if in_humidity:
            assign_map_values(line, "temperature", "humidity")
        if line.strip() == "humidity-to-location map:":
            in_location = True
            in_humidity = False
            continue
        if in_location:
            assign_map_values(line, "humidity", "location")
            in_location = False
        print("seed_maps: ", seed_maps)


def print_seed_map_dict(seed_map):
    print("seed: ", seed_map["seed"])
    print("soil: ", seed_map["soil"])
    print("fertilizer: ", seed_map["fertilizer"])
    print("water: ", seed_map["water"])
    print("light: ", seed_map["light"])
    print("temperature: ", seed_map["temperature"])
    print("humidity: ", seed_map["humidity"])
    print("location: ", seed_map["location"])


def find_lowest_location(seed_maps):
    lowest_location = -1
    for idx, seed_map in enumerate(seed_maps):
        if lowest_location == -1:
            lowest_location = seed_map["location"]
        else:
            if seed_map["location"] < lowest_location:
                lowest_location = seed_map["location"]
    return lowest_location


with open("input_files/input_one_test.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

create_seed_maps(lines, seed_map)
lowest_location = find_lowest_location(seed_maps)
print("lowest_location: ", lowest_location)
