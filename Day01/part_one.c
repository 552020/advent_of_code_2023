#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Just not to have to allocate a buffer of a random size*/
int find_max_line_length(char *file_str) {
  FILE *file;
  int c;
  int line_length;
  int max_line_length;

  line_length = 0;
  max_line_length = 0;

  file = fopen(file_str, "r");
  if (!file) {
    perror("Error opening file");
    exit(1);
  }
  while ((c = fgetc(file)) != EOF) {
    line_length++;
    if (c == '\n') {
      if (line_length > max_line_length) {
        max_line_length = line_length;
      }
      line_length = 0;
    }
    if (line_length > max_line_length) {
      max_line_length = line_length;
    }
  }
  return (max_line_length);
}

int extract_nbr_from_line(char *str) {
  int len;
  char nbr_str[3];
  int nbr;

  nbr_str[0] = '0';
  nbr_str[1] = '0';
  nbr_str[2] = '\0';

  len = strlen(str);
  for (int i = 0; i < len; i++) {
    if (isdigit(str[i])) {
      printf("isdigit: %c\n", str[i]);
      nbr_str[0] = str[i];
      break;
    }
  }
  for (int i = len - 1; i >= 0; i--) {
    if (isdigit(str[i])) {
      printf("isdigit: %c\n", str[i]);
      nbr_str[1] = str[i];
      break;
    }
  }

  nbr = atoi(nbr_str);
  return (nbr);
}

int main(int argc, char **argv) {

  FILE *input_file;
  int max_line_length;
  char *line;
  char *input_file_str = "input_files/input.txt";
  int nbr;
  int total;

  if (argc == 2) {
    input_file_str = argv[1];
  }

  total = 0;
  max_line_length = find_max_line_length(input_file_str);
  line = malloc(max_line_length + 1);
  if (line == NULL) {
    perror("Error allocating memory");
    return 1;
  }

  input_file = fopen(input_file_str, "r");
  if (input_file == NULL) {
    perror("Error opening file");
    free(line);
    return 1;
  }

  while (fgets(line, max_line_length + 1, input_file)) {
    printf("line: %s", line);
    nbr = extract_nbr_from_line(line);
    printf("total before: %d\n", total);
    total += nbr;
    printf("total after: %d\n", total);
  }
  free(line);
  fclose(input_file);

  printf("total: %i\n", total);

  return (0);
}