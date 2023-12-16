
def first_star():
    with open("aoc_day1_input.txt", 'r') as fancy_calibration_fh:
        sum_calibration_values = 0
        for line in fancy_calibration_fh:
            fwd_line = line.strip()
            # print(fwd_line)

            first_digit = ""
            second_digit = ""
            for i in range(len(fwd_line)):
                if fwd_line[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                    first_digit = fwd_line[i]
                    break
            for i in range(len(fwd_line) - 1, -1, -1):
                if fwd_line[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                    second_digit = fwd_line[i]
                    break

            calibration_value = first_digit + second_digit
            # print(calibration_value)
            sum_calibration_values += int(calibration_value)

        print(sum_calibration_values)


def second_star():
    print("this is harder!")
    string_digits_3 = ["one", "two", "six"]
    string_digits_4 = ["four", "five", "nine"]
    string_digits_5 = ["three", "seven", "eight"]
    with open("aoc_day1_input.txt", 'r') as fancy_calibration_fh:
        sum_calibration_values = 0
        for fancy_calibration_line in fancy_calibration_fh:
            fancy_calibration = fancy_calibration_line.strip()
            # print(fancy_calibration)

            first_digit = 0
            second_digit = 0

            for i in range(len(fancy_calibration)):
                if fancy_calibration[i:i+3] in string_digits_3:
                    digit_str = fancy_calibration[i:i+3]
                    if digit_str == "one":
                        digit = 1
                    elif digit_str == "two":
                        digit = 2
                    elif digit_str == "six":
                        digit = 6

                    if first_digit == 0:
                        first_digit = digit

                    second_digit = digit

                elif fancy_calibration[i:i+4] in string_digits_4:
                    digit_str = fancy_calibration[i:i+4]
                    if digit_str == "four":
                        digit = 4
                    elif digit_str == "five":
                        digit = 5
                    elif digit_str == "nine":
                        digit = 9

                    if first_digit == 0:
                        first_digit = digit

                    second_digit = digit

                elif fancy_calibration[i:i+5] in string_digits_5:
                    digit_str = fancy_calibration[i:i+5]
                    if digit_str == "three":
                        digit = 3
                    elif digit_str == "seven":
                        digit = 7
                    elif digit_str == "eight":
                        digit = 8

                    if first_digit == 0:
                        first_digit = digit

                    second_digit = digit

                elif fancy_calibration[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                    digit = int(fancy_calibration[i])
                    if first_digit == 0:
                        first_digit = digit

                    second_digit = digit

            # print(first_digit)
            # print(second_digit)
            calibration_value = str(first_digit) + str(second_digit)
            # print(calibration_value)
            sum_calibration_values += int(calibration_value)

        print(sum_calibration_values)


first_star()
second_star()
