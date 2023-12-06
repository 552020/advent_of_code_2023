#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <ctype.h>

#define MAX_LINES 1000
#define MAX_SEED_MAPS 100

typedef struct {
    int seed;
    int soil;
    int fertilizer;
    int water;
    int light;
    int temperature;
    int humidity;
    int location;
} SeedMap;

SeedMap seed_maps[MAX_SEED_MAPS];
int num_seed_maps = 0;

void extract_seeds(const char* line, SeedMap* seed_map_template) {
    if (strncmp(line, "seeds:", 6) == 0) {
        const char* seeds = line + 7;
        char* token;
        char* rest = (char*)seeds;
        while ((token = strtok_r(rest, " ", &rest))) {
            int seed = atoi(token);
            if (seed != 0) {
                SeedMap new_seed_map = *seed_map_template;
                new_seed_map.seed = seed;
                seed_maps[num_seed_maps++] = new_seed_map;
            }
        }
    }
}

void assign_map_values(const char* line, const char* key_src, const char* key_dest) {
    if (line[0] == '\0' || !isdigit(line[0])) return;

    int destination_range_start, source_range_start, range_length;
    sscanf(line, "%d %d %d", &destination_range_start, &source_range_start, &range_length);

    for (int i = 0; i < num_seed_maps; i++) {
        SeedMap* seed_map = &seed_maps[i];
        int* src_ptr = &seed_map->seed + (key_src[0] - 'a');
        int* dest_ptr = &seed_map->seed + (key_dest[0] - 'a');

        for (int idx = 0; idx < range_length; idx++) {
            if (*src_ptr == source_range_start + idx) {
                *dest_ptr = destination_range_start + idx;
                break;
            }
        }

        if (*dest_ptr == 0) *dest_ptr = *src_ptr;
    }
}

void process_lines(char lines[MAX_LINES][256], int num_lines) {
    SeedMap seed_map_template = {0};
    extract_seeds(lines[0], &seed_map_template);

    int in_section = 0;

    for (int i = 1; i < num_lines; i++) {
        char* line = lines[i];
        if (strcmp(line, "") == 0) continue;

        if (strncmp(line, "seed-to-", 8) == 0) {
            in_section = line[8];
            continue;
        }

        if (in_section) {
            char key_dest[2] = {in_section, '\0'};
            char key_src[2] = {in_section - 1, '\0'};
            assign_map_values(line, key_src, key_dest);
        }
    }
}

int find_lowest_location() {
    int lowest_location = INT_MAX;
    for (int i = 0; i < num_seed_maps; i++) {
        if (seed_maps[i].location < lowest_location) {
            lowest_location = seed_maps[i].location;
        }
    }
    return lowest_location == INT_MAX ? -1 : lowest_location;
}

int main() {
    char lines[MAX_LINES][256];
    FILE* file = fopen("input_files/input_one_test.txt", "r");
    int num_lines = 0;

    while (fgets(lines[num_lines], sizeof(lines[num_lines]), file)) {
        lines[num_lines][strcspn(lines[num_lines], "\n")] = 0;
        num_lines++;
    }
    fclose(file);

    process_lines(lines, num_lines);
    int lowest_location = find_lowest_location();
    printf("lowest_location: %d\n", lowest_location);

    return 0;
}
