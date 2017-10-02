from alien import AlienNumberConverter, AlienNumberTestCase

if __name__ == '__main__':

    test_cases = []
    firstLineRead = False
    with open("A-large-practice.in") as f:
        for line in f:
            if firstLineRead:
                alien_number, source_language, target_language = line.strip().split(" ")
                test_cases.append(AlienNumberTestCase(alien_number, source_language, target_language))
            else:
                case_count = int(line.strip())
                firstLineRead = True

    print("There should be {0} test cases.".format(case_count));

    converter = AlienNumberConverter()
    output = []
    for test_case in test_cases:
        print(test_case)
        fu = converter.convert(test_case)
        print("[" + fu + "]")
        output.append(fu)

    count = 1
    with open('A-large-practice-output.txt', 'a') as output_file:
        for translated_alien_number in output:
            output_file.write("Case #{0}: {1}\n".format(count, translated_alien_number))
            count += 1
