def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 0
    filename = "input.csv"
    passwords = read_file(filename)[0].split(',')
    invalid_ids = []
    for p in passwords:
        min, max = p.split('-')
        min, max = int(min), int(max)

        # max + 1 because range is [inclusive, exclusive)
        for code in range(min, max + 1):
            str_code = str(code)
            identified_invalid_code = False
            for divider in range(2, len(str_code)+1):
                if identified_invalid_code == True:
                    continue
                if len(str_code) % divider == 0:
                    code_list = []
                    segment_length = len(str_code) // divider
                    index = 0

                    for _ in range(divider):
                        current_segment = ''
                        for segment_index in range(segment_length):
                            current_segment += str_code[index]
                            index += 1
                            if segment_index == segment_length - 1:
                                code_list.append(current_segment)
        
                    all_equal = True
                    for segment_index in range(1, len(code_list)):
                        previous_segment = code_list[segment_index - 1]
                        current_segment = code_list[segment_index]
                        if current_segment != previous_segment:
                            all_equal = False
                    
                    starts_with_zero = True if code_list[0][0] == 0 else False

                    if all_equal and not starts_with_zero:
                        answer += int(code)
                        identified_invalid_code = True
                        invalid_ids.append(code)

    return answer

answer = main()
print(answer)
