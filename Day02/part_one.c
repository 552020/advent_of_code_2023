#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int find_max_line_length(char *file_str);

typedef struct s_set {
  int blue;
  int green;
  int red;

} t_set;

typedef struct s_game {
  int game_id;
  char *sets_str;
  int sets_str_arr_len;
  char **sets_str_arr;
  t_set **sets_struct_arr;

} t_game;

typedef struct s_games {
  t_game *games_arr[101];

} t_games;

void create_sets_arr(t_game *game) {
  char *start;
  //   char *end;
  char *cur;
  int str_len;
  int arr_len;
  // printf("create_sets_arr\n");
  //   printf("sets_str: %s", game->sets_str);

  str_len = 0;

  arr_len = 1;
  cur = strchr(game->sets_str, ';');
  while (cur) {
    arr_len++;
    cur = strchr(cur + 1, ';');
  }
  game->sets_str_arr_len = arr_len;

  //   printf("arr_len: %d\n", arr_len);
  game->sets_str_arr = malloc(sizeof(char *) * (arr_len + 1));
  if (!game->sets_str_arr) {
    // free memory;
    exit(1);
  }
  game->sets_struct_arr = malloc(sizeof(t_set *) * (arr_len + 1));
  if (!game->sets_struct_arr) {
    // free memory
    exit(1);
  }
  game->sets_struct_arr[arr_len] = NULL;
  int i = 0;
  start = game->sets_str;
  cur = strchr(game->sets_str, ';');
  while (cur) {
    game->sets_str_arr[i] = malloc(cur - start + 1);
    if (!game->sets_str_arr[i]) {
      // free memory
      exit(1);
    }
    memcpy(game->sets_str_arr[i], start, cur - start);
    game->sets_str_arr[i][cur - start] = '\0';
    start = cur + 1;
    while (isspace(*start))
      start++;
    cur = strchr(cur + 1, ';');
    printf("%s\n", game->sets_str_arr[i]);
    i++;
  }
  if (cur == NULL) {
    str_len = strlen(start);
    game->sets_str_arr[i] = malloc(str_len + 1);
    if (!game->sets_str_arr[i]) {
      // free memory
      exit(1);
    }
    memcpy(game->sets_str_arr[i], start, str_len);
    game->sets_str_arr[i][str_len] = '\0';
    printf("%s\n", game->sets_str_arr[i]);
  }
  game->sets_str_arr[i] = NULL;
}

void free_sets_str_arr(t_game *game) {
  int i;
  i = 0;
  while (game->sets_str_arr[i]) {
    free(game->sets_str_arr[i]);
    i++;
  }
  free(game->sets_str_arr);
}

void create_sets_struct_arr(t_game *game) {
  int i;

  printf("creat_sets_struct_arr\n");

  i = 0;
  while (game->sets_str_arr[i]) {
    char *start;
    char *cur;
    char *colors[4] = {"green", "blue", "red", NULL};
    int j;
    j = 0;

    game->sets_struct_arr[i] = malloc(sizeof(t_set));

    while (colors[j]) {
      printf("i: %d", i);
      start = game->sets_str_arr[i];
      cur = strstr(start, colors[j]);
      if (cur) {
        cur -= 2;
        if (isdigit(*cur))
          cur--;
        if (strncmp(colors[j], "green", 5) == 0)
          game->sets_struct_arr[i]->green = atoi(cur++);
        else if (strncmp(colors[j], "red", 3) == 0)
          game->sets_struct_arr[i]->red = atoi(cur++);
        else if (strncmp(colors[j], "blue", 4) == 0)
          game->sets_struct_arr[i]->blue = atoi(cur++);

      } else
        game->sets_struct_arr[i]->green = 0;
      j++;
    }
    i++;
  }
}

void create_and_init_games(t_games *games) {
  FILE *input_file;
  int max_line_length;
  char *line;
  char *input_file_str = "input_files/input_one.txt";

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
    printf("Game[%i]: Id: %d, Sets: %s", i, games->games_arr[i]->game_id,
           games->games_arr[i]->sets_str);
    i++;
  }
  games->games_arr[i] = NULL;
  free(line);
  fclose(input_file);
}

int main() {

  t_games games;
  int i;
  int j;
  i = 0;
  create_and_init_games(&games);
  while (games.games_arr[i]) {
    printf("n: %d\n", i);
    create_sets_arr(games.games_arr[i]);
    create_sets_struct_arr(games.games_arr[i]);
    i++;
  }
  i = 0;
  while (games.games_arr[i]) {
    printf("i: %d", i);
    i++;
  }
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
