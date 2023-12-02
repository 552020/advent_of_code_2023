#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int	find_max_line_length(char *file_str)
{
	FILE	*file;
	int		c;
	int		line_length;
	int		max_line_length;

	line_length = 0;
	max_line_length = 0;
	file = fopen(file_str, "r");
	if (!file)
	{
		perror("Error opening file");
		exit(1);
	}
	while ((c = fgetc(file)) != EOF)
	{
		line_length++;
		if (c == '\n')
		{
			if (line_length > max_line_length)
			{
				max_line_length = line_length;
			}
			line_length = 0;
		}
		if (line_length > max_line_length)
		{
			max_line_length = line_length;
		}
	}
	return (max_line_length);
}

typedef struct s_nbr
{
	int		value;
	char	*pos;
}			t_nbr;

typedef enum e_dir
{
	BACKWARDS,
	FORWARDS
}			t_dir;

t_nbr	find_nbr_as_string_if_any(char *str, t_dir direction)
{
	t_nbr	nbr_str;
	int		i;
	char	*cur_ptr;
	char	*prev_ptr;
	int		direction_condition;
	char	*ints[] = {"one", "two", "three", "four", "five", "six", "seven",
			"eight", "nine", NULL};

	cur_ptr = NULL;
	prev_ptr = NULL;
	nbr_str.pos = NULL;
	nbr_str.value = 0;
	i = 0;
	while (ints[i])
	{
		if (direction == BACKWARDS)
		{
			prev_ptr = cur_ptr;
			cur_ptr = strstr(str, ints[i]);
			while (cur_ptr != NULL)
			{
				prev_ptr = cur_ptr;
				cur_ptr = strstr(prev_ptr + 1, ints[i]);
			}
			cur_ptr = prev_ptr;
		}
		else if (direction == FORWARDS)
		{
			cur_ptr = strstr(str, ints[i]);
			if (nbr_str.pos == NULL)
				nbr_str.pos = cur_ptr;
		}
		if (direction == BACKWARDS)
			direction_condition = cur_ptr > nbr_str.pos;
		else if (direction == FORWARDS)
		{
			direction_condition = cur_ptr <= nbr_str.pos;
		}
		if (direction_condition && cur_ptr != NULL)
		{
			if (nbr_str.pos == NULL)
				nbr_str.pos = cur_ptr;
			nbr_str.pos = cur_ptr;
			nbr_str.value = i + 1;
		}
		i++;
	}
	return (nbr_str);
}

t_nbr	find_nbr_as_digit_if_any(char *str, t_dir direction)
{
	t_nbr	nbr_dgt;
	int		len;
	char	atoi_str[2];
	int		i;

	nbr_dgt.value = 0;
	nbr_dgt.pos = NULL;
	len = strlen(str);
	if (direction == FORWARDS)
	{
		i = 0;
		while (i < len)
		{
			if (isdigit(str[i]))
			{
				atoi_str[0] = str[i];
				atoi_str[1] = '\0';
				nbr_dgt.pos = &str[i];
				nbr_dgt.value = atoi(atoi_str);
				break ;
			}
			i++;
		}
	}
	else if (direction == BACKWARDS)
	{
		for (int i = len - 1; i >= 0; i--)
		{
			if (isdigit(str[i]))
			{
				atoi_str[0] = str[i];
				atoi_str[1] = '\0';
				nbr_dgt.pos = &str[i];
				nbr_dgt.value = atoi(atoi_str);
				break ;
			}
		}
	}
	return (nbr_dgt);
}

int	find_nbr_as_digit_or_string(char *str)
{
	t_dir	direction;
	t_nbr	str_nbr_first;
	t_nbr	dgt_nbr_first;
	t_nbr	str_nbr_second;
	t_nbr	dgt_nbr_second;
	int		first_nbr;
	int		second_nbr;
	int		ret;

	first_nbr = 0;
	second_nbr = 0;
	direction = FORWARDS;
	str_nbr_first = find_nbr_as_string_if_any(str, direction);
	dgt_nbr_first = find_nbr_as_digit_if_any(str, direction);
	// printf("find_nbr_as_digit_or_string\n");
	if (str_nbr_first.pos == NULL || ((str_nbr_first.pos > dgt_nbr_first.pos)
			&& dgt_nbr_first.pos != NULL))
		first_nbr = dgt_nbr_first.value;
	if (str_nbr_first.pos == NULL)
		first_nbr = dgt_nbr_first.value;
	else if (dgt_nbr_first.pos == NULL)
		first_nbr = str_nbr_first.value;
	else if (str_nbr_first.pos < dgt_nbr_first.pos)
		first_nbr = str_nbr_first.value;
	else if (str_nbr_first.pos > dgt_nbr_first.pos)
		first_nbr = dgt_nbr_first.value;
	direction = BACKWARDS;
	str_nbr_second = find_nbr_as_string_if_any(str, direction);
	dgt_nbr_second = find_nbr_as_digit_if_any(str, direction);
	if (str_nbr_second.pos == NULL)
		second_nbr = dgt_nbr_second.value;
	else if (dgt_nbr_second.pos == NULL)
		second_nbr = str_nbr_second.value;
	else if (str_nbr_second.pos < dgt_nbr_second.pos)
		second_nbr = dgt_nbr_second.value;
	else if (str_nbr_second.pos > dgt_nbr_second.pos)
		second_nbr = str_nbr_second.value;
	ret = first_nbr * 10 + second_nbr;
	return (ret);
}

int	extract_nbr_from_line(char *str)
{
	int		len;
	char	nbr_str[3];
	int		nbr;

	nbr_str[0] = '0';
	nbr_str[1] = '0';
	nbr_str[2] = '\0';
	len = strlen(str);
	for (int i = 0; i < len; i++)
	{
		if (isdigit(str[i]))
		{
			nbr_str[0] = str[i];
			break ;
		}
	}
	for (int i = len - 1; i >= 0; i--)
	{
		if (isdigit(str[i]))
		{
			nbr_str[1] = str[i];
			break ;
		}
	}
	nbr = atoi(nbr_str);
	return (nbr);
}

int	main(int argc, char **argv)
{
	FILE *input_file;
	int max_line_length;
	char *line;
	char *input_file_str = "input_files/input_part_two.txt";
	int nbr;
	int total;

	if (argc == 2)
	{
		input_file_str = argv[1];
	}

	total = 0;
	max_line_length = find_max_line_length(input_file_str);
	line = malloc(max_line_length + 1);
	if (line == NULL)
	{
		perror("Error allocating memory");
		return (1);
	}

	input_file = fopen(input_file_str, "r");
	if (input_file == NULL)
	{
		perror("Error opening file");
		free(line);
		return (1);
	}
	int i = 1;
	while (fgets(line, max_line_length + 1, input_file))
	{
		printf("%d: ", i);
		printf("line: %s", line);
		nbr = find_nbr_as_digit_or_string(line);
		printf("nbr: %d\n", nbr);
		total += nbr;
		i++;
	}
	free(line);
	fclose(input_file);

	printf("Total Sum: %i\n", total);

	return (0);
}