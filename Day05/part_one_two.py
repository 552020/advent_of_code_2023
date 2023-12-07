# pylint: disable-all

lines = []
seeds_list = []
maps = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": [],
}
destination_range_start = 0
source_range_start = 0
range_length = 0


def extract_seeds(line):
    if line.split(":")[0] == "seeds":
        seeds = line.split(":")[1].strip().split(" ")
        print("seeds: ", seeds)
        for seed in seeds:
            print("seed: ", seed)
            seed.strip()
            if seed != "":
                seeds_list.append(int(seed))
    print("seeds_list: ", seeds_list)


def extract(line, key):
    if line == "":
        return
    list = []
    destination_range_start = int(line.split()[0].strip())
    source_range_start = int(line.split()[1].strip())
    range_length = int(line.split()[2].strip())
    list[0] = destination_range_start
    list[1] = source_range_start
    list[2] = range_length
    maps[key].append(list)


def extract_dest_source_range_wrapper(lines):
    for line in lines:
        if line == "":
            continue
        if line == "seed-to-soil map:":
            extract(line, "seed-to-soil")
        return destination_range_start, source_range_start, range_length
    return 0, 0, 0


def assign_map_values(line, key_src, key_dest):
    stripped = line.strip()
    if stripped == "":
        return
    if not stripped[0].isdigit():
        return
    # print("line: ", line)
    destination_range_start = int(line.split()[0].strip())
    # print("destination_range_start: ", destination_range_start)
    source_range_start = int(line.split()[1].strip())
    # print("source_range_start: ", source_range_start)
    range_length = int(line.split()[2].strip())
    # print("range_length: ", range_length)
    for seed_map in seed_maps:
        update_flag_key = f"{key_dest}_updated"
        if not seed_map.get(update_flag_key):
            seed_map[update_flag_key] = False
        # matched = False
        for idx in range(range_length):
            if seed_map[key_src] == source_range_start + idx:
                # matched = True
                # print("Matched: ")
                # print("key_src: ", key_src)
                # print("key_dest: ", key_dest)
                # print("seed_map[key_src]: ", seed_map[key_src])
                # print("source_range_start + idx: ", source_range_start + idx)
                # print("seed_map[key_dest] before: ", seed_map[key_dest])
                seed_map[key_dest] = destination_range_start + idx
                # print("seed_map[key_dest] after: ", seed_map[key_dest])
                seed_map[update_flag_key] = True
                break
        # if not matched:
        if seed_map[update_flag_key] == False:
            # print("Not matched: ")
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
            # idx = -1
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
    # print("Exit create_seed_maps")


def find_lowest_location(seed_maps):
    lowest_location = 0
    for seed_map in seed_maps:
        if seed_map["location"] > lowest_location:
            lowest_location = seed_map["location"]
    return lowest_location


with open("input_files/input_one_test.txt", "r") as file:
    for line in file:
        lines.append(line.strip())


# create_seed_maps(lines, seed_map)
extract_seeds(lines[0])
# lowest_location = find_lowest_location(seed_maps)
# print("lowest_location: ", lowest_location)
# print_all_locations(seed_maps)
