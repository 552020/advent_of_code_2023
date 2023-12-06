#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

#define MAX_RANGES 100
#define MAX_CATEGORIES 7

typedef struct {
    int dest_start;
    int src_start;
    int length;
} MapRange;

int findMappedValue(int src, MapRange *map, int rangeCount) {
    for (int i = 0; i < rangeCount; i++) {
        if (src >= map[i].src_start && src < map[i].src_start + map[i].length) {
            return map[i].dest_start + (src - map[i].src_start);
        }
    }
    return src; // Return the same number if not found in the map
}

int main() {
    FILE *file = fopen("input_files/input_one_test.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    char line[256];
    int seeds[MAX_RANGES], seedCount = 0;
    MapRange maps[MAX_CATEGORIES][MAX_RANGES];
    int mapCounts[MAX_CATEGORIES] = {0};

    // Read seeds
    if (fgets(line, sizeof(line), file) != NULL) {
        char *token = strtok(line, " ");
        while (token != NULL) {
            seeds[seedCount++] = atoi(token);
            token = strtok(NULL, " ");
        }
    }

    // Read maps
    int currentMap = -1;
    while (fgets(line, sizeof(line), file)) {
        if (strstr(line, "map:") != NULL) {
            currentMap++;
        } else if (currentMap >= 0) {
            int dest, src, len;
            sscanf(line, "%d %d %d", &dest, &src, &len);
            maps[currentMap][mapCounts[currentMap]++] = (MapRange){.dest_start = dest, .src_start = src, .length = len};
        }
    }

    fclose(file);

    int minLocation = INT_MAX;
    for (int i = 0; i < seedCount; i++) {
        int value = seeds[i];
        for (int j = 0; j < MAX_CATEGORIES; j++) {
            value = findMappedValue(value, maps[j], mapCounts[j]);
        }
        if (value < minLocation) {
            minLocation = value;
        }
    }

    printf("Lowest location number: %d\n", minLocation);

    return 0;
}
