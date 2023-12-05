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
        for seed in seeds:
            seed = seed.strip()
            if seed != "":
                print("seed: ")
                print(seed)
                tmp = seed_map.copy()
                tmp["seed"] = int(seed)
                seed_maps.append(tmp)

    return True


def extract_soil(line, seed_map):
    # print('line.split(":")[0].strip: ')
    # print(line.split(":")[0].strip())
    if line.split(":")[0].strip() == "seed-to-soil map":
        soils = line.split(":")[1].split(" ")
        print("soils: ")
        print(soils)
        for soil in soils:
            soil = soil.strip()
            if soil != "":
                print("soil: ")
                print(soil)

    return True


def create_seed_maps(lines, seed_map):
    for line in lines:
        extract_seeds(line, seed_map)
        extract_soil(line, seed_map)
        # print(line.split(":")[0])
        # if line.split(":")[0] == "seeds":
        #     seeds = line.split(":")[1].split(" ")
        #     for seed in seeds:
        #         seed = seed.strip()
        #         if seed != "":
        #             print("seed: ")
        #             print(seed)
        #             tmp = seed_map.copy()
        #             tmp["seed"] = int(seed)
        #             seed_maps.append(tmp)

    return True


with open("input_files/input_one.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

create_seed_maps(lines, seed_map)
# for line in lines:
# print(line)
# print(lines)
# print("seed_maps: ")
# print(seed_maps)
