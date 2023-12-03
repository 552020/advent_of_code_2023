#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int find_max_line_length(char *file_str);

void create_and_init_games(t_games *games) {
  FILE *input_file;
  int max_line_length;
  char *line;
  char *input_file_str = "input_files/input_one_test.txt";

  max_line_length = find_max_line_length(input_file_str);
  line = malloc(max_line_length + 1);
  if (line == NULL) {
    perror("Error allocating memory");
    exit(1);
  }
  input_file = fopen(input_file_str, "r");
  if (input_file == NULL) {
    perror("Error opening file");
    free(line);
    exit(1);
  }
  int i = 0;
  char *start_sets;
  while (fgets(line, max_line_length + 1, input_file)) {
    printf("%s", line);
    games->games_arr[i] = malloc(sizeof(t_game));
    games->games_arr[i]->game_id = i + 1;
    start_sets = strrchr(line, ':');
    games->games_arr[i]->sets_str = strdup(start_sets + 2);
    // printf("Game[%i]: Id: %d, Sets: %s", i, games->games_arr[i]->game_id,
    //    games->games_arr[i]->sets_str);
    i++;
  }
  games->games_arr[i] = NULL;
  free(line);
  fclose(input_file);
}

int main() {

  t_games games;

  int total;
  int i;
  int j;
  i = 0;
  total = 0;
  create_and_init_games(&games);
  while (games.games_arr[i]) {
    // printf("n: %d\n", i);
    create_sets_arr(games.games_arr[i]);
    create_sets_struct_arr(games.games_arr[i]);
    i++;
  }
  i = 0;
  while (games.games_arr[i]) {
    j = 0;
    while (games.games_arr[i]->sets_struct_arr[j]) {
      printf("sets_struct_arr[%d]: green: %d, blue: %d, red: %d\n", j,
             games.games_arr[i]->sets_struct_arr[j]->green,
             games.games_arr[i]->sets_struct_arr[j]->blue,
             games.games_arr[i]->sets_struct_arr[j]->red);
      j++;
    }
    i++;
  }
  i = 0;
  while (games.games_arr[i]) {
    // printf("i: %d\n", i);
    printf("****************************\n");
    printf("GAME ID: %d\n", games.games_arr[i]->game_id);
    // printf("sets_str: %s\n", games.games_arr[i]->sets_str);
    j = 0;
    while (games.games_arr[i]->sets_str_arr[j]) {
      //   printf("sets_str_arr[%d]: %s\n", j,
      //   games.games_arr[i]->sets_str_arr[j]);
      j++;
    }
    j = 0;
    while (games.games_arr[i]->sets_struct_arr[j]) {
      int flag = 0;
      printf("sets_struct_arr[%d]: green: %d, blue: %d, red: %d\n", j,
             games.games_arr[i]->sets_struct_arr[j]->green,
             games.games_arr[i]->sets_struct_arr[j]->blue,
             games.games_arr[i]->sets_struct_arr[j]->red);
      if ((games.games_arr[i]->sets_struct_arr[j]->green >= 13) &&
          (games.games_arr[i]->sets_struct_arr[j]->red >= 12) &&
          (games.games_arr[i]->sets_struct_arr[j]->blue >= 14)) {
        flag = 1;
        break;
      }
      if (flag == 0)
        total += games.games_arr[i]->game_id;
      flag = 0;
      ++j;
    }
    i++;
  }
  printf("total: %d", total);
  while (games.games_arr[i]) {
    j = 0;
    free(games.games_arr[i]->sets_str);
    while (games.games_arr[i]->sets_str_arr[j]) {
      free(games.games_arr[i]->sets_str_arr[j]);
      j++;
    }
    free(games.games_arr[i]->sets_str_arr);
    j = 0;
    while (games.games_arr[i]->sets_struct_arr[j]) {
      free(games.games_arr[i]->sets_struct_arr[j]);
      j++;
    }
    free(games.games_arr[i]->sets_struct_arr);
    free(games.games_arr[i]);
  }

  return (0);
}
