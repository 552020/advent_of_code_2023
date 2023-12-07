races = []
race = {
    "time": 0,
    "distance": 0,
}
results = []

counter = 0


def fill_race_dict(line, key):
    second_part = line.split(":")[1].strip().split()
    for idx, part in enumerate(second_part):
        if idx >= len(races):
            races.append(race.copy())
        races[idx][key] = int(part)


with open("input_files/input_one_test.txt", "r") as file:
    for line in file:
        copy = race.copy()
        if line.split(":")[0] == "Time":
            fill_race_dict(line, "time")
        if line.split(":")[0] == "Distance":
            fill_race_dict(line, "distance")

for idx, race in enumerate(races):
    print("idx: ", idx)
    print("counter: ", counter)
    time = races[idx]["time"]
    print("time: ", time)
    distance = races[idx]["distance"]
    print("distance: ", distance)
    # for el in range(time):
    # print("idx el: ", el)
    i = 0
    counter = 0
    while i < time:
        print("i: ", i)
        print("time : ", time)
        result = (time - i) * i
        print("result: ", result)
        if result > distance:
            print("result > distance: ", result)
            counter += 1
            print("counter: ", counter)
        i += 1
    results.append(counter)


print(races)
print(counter)
total = 1
for result in results:
    print("result: ", result)
    total *= result
print(total)
