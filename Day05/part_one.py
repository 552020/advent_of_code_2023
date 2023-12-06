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
        print("line.split(:)[1]: ", line.split(":")[1].strip())
        print(
            "line.split(:)[1].strip().split(" "): ",
            line.split(":")[1].strip().split(" "),
        )

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
                print("tmp: ", tmp)
                seed_maps.append(tmp)
    print("Exit extract_seeds")


def assign_map_values(line, seed_map, key):
    stripped = line.strip()
    if stripped == "":
        return
    if not stripped[0].isdigit():
        return False
    print("line: ", line)
    destination_range_start = int(line.split()[0].strip())
    source_range_start = int(line.split()[1].strip())
    range_length = int(line.split()[2].strip())
    for idx in range(range_length):
        for seed_map in seed_maps:
            if seed_map["seed"] == source_range_start + idx:
                seed_map[key] = destination_range_start + idx
    return True


def create_seed_maps(lines, seed_map):
    print("create_seed_maps")
    in_soil = False
    in_fertilizer = False
    in_water = False
    in_light = False
    in_temperature = False
    in_humidity = False
    in_location = False

    idx = 0
    extract_seeds(lines[0], seed_map)
    print("seed_maps: ", seed_maps)
    for i, line in enumerate(lines):
        print("line: ", line)
        if line.strip() == "":
            continue
        if line.strip() == "seed-to-soil map:":
            in_soil = True
            idx = -1
            continue
        if in_soil:
            print("in soil")
            print("line: ", line)
            if line.strip()[0].isdigit():
                idx += 1
                print("idx: ", idx)
                print("seed_maps[idx]: ", seed_maps[idx])
                assign_map_values(line, seed_maps[idx], "soil")
        if line.strip() == "soil-to-fertilizer map:":
            print("in soil to fertilizer")
            print("line: ", line)
            in_fertilizer = True
            in_soil = False
            idx = -1
            continue
        if in_fertilizer:
            if line.strip()[0].isdigit():
                idx += 1
                assign_map_values(line, seed_maps[idx], "fertilizer")
        if line.strip() == "fertilizer-to-water map:":
            in_water = True
            in_fertilizer = False
            idx = -1
            continue
        if in_water:
            if line.strip()[0].isdigit():
                idx += 1
                assign_map_values(line, seed_maps[idx], "water")
        if line.strip() == "water-to-light map:":
            in_light = True
            in_water = False
            idx = -1
            continue
        if in_light:
            if line.strip()[0].isdigit():
                idx += 1
                assign_map_values(line, seed_maps[idx], "light")
        if line.strip() == "light-to-temperature map:":
            in_temperature = True
            in_light = False
            idx = -1
            continue
        if in_temperature:
            if line.strip()[0].isdigit():
                idx += 1
                assign_map_values(line, seed_maps[idx], "temperature")
        if line.strip() == "temperature-to-humidity map:":
            in_humidity = True
            in_temperature = False
            idx = -1
            continue
        if in_humidity:
            if line.strip()[0].isdigit():
                idx += 1
                assign_map_values(line, seed_maps[idx], "humidity")
        if line.strip() == "humidity-to-location map:":
            in_location = True
            in_humidity = False
            idx = -1
            continue
        if in_location:
            if line.strip()[0].isdigit():
                idx += 1
                assign_map_values(line, seed_maps[idx], "location")
            in_location = False
        print("seed_maps[idx]:", seed_maps[idx])


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
    lowest_location = 0
    for seed_map in seed_maps:
        if seed_map["location"] > lowest_location:
            lowest_location = seed_map["location"]
    return lowest_location


def print_all_locations(seed_maps):
    for idx, seed_map in enumerate(seed_maps):
        print("idx: ", idx)
        # print("seed: ", seed_map["seed"])
        # print("soil: ", seed_map["soil"])
        # print("fertilizer: ", seed_map["fertilizer"])
        # print("water: ", seed_map["water"])
        # print("light: ", seed_map["light"])
        # print("temperature: ", seed_map["temperature"])
        # print("humidity: ", seed_map["humidity"])
        print("location: ", seed_map["location"])
        print("")


with open("input_files/input_one_test.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

create_seed_maps(lines, seed_map)
lowest_location = find_lowest_location(seed_maps)
print("lowest_location: ", lowest_location)
print_all_locations(seed_maps)
