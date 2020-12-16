def read_input_lines():
    with open("input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]


def create_rule_dict():
    lines = read_input_lines()
    rules = dict()
    for i in range(0, 20):
        line = lines[i]
        spl = [l.strip() for l in line.split(":")]
        name = spl[0]
        rule_set = spl[1]
        two_rule = [r.strip() for r in rule_set.split("or")]
        two_rule = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in two_rule]   
        rules[name] = two_rule
    return rules


def check_rule(rules, rule, x):
    r = rules[rule]
    flow, fhigh = r[0]
    slow, shigh = r[1]
    return flow <= x <= fhigh or slow <= x <= shigh


def part1():
    lines = read_input_lines()
    rules = create_rule_dict()
    start = 25 # start at nearby tickets
    invalid_tickets = []
    invalid_tickets_ids = []
    for i in range(start, len(lines)):
        field_values = [int(l) for l in lines[i].split(",")]
        for val in field_values:
            checks = [check_rule(rules, rule, val) for rule in rules]
            if not any(checks):
                invalid_tickets.append(val)
                invalid_tickets_ids.append(i - start)
    return sum(invalid_tickets), invalid_tickets_ids


def find_columns(rules, tickets, no_check_column, columns):  
    if len(rules) <= 1:
        return [list(rules.keys()).pop()]
    # Loop column wise and check where ALL check_rule is True
    column_matches = {}
    for i in range(len(tickets[0])):
        if i not in no_check_column:
            whole_column = [tickets[j][i] for j in range(len(tickets))]
            for rule in rules:
                checks = [check_rule(rules, rule, x) for x in whole_column]
                if all(checks):
                    if i not in column_matches:
                        column_matches[i] = []
                    column_matches[i].append(rule)
    column_matches_freq = {}
    for rule in rules:
        counter = 0
        column = -1
        for k in column_matches:
            if rule in column_matches[k]:
                counter += 1
                column = k
                continue
        column_matches_freq[rule] = (counter, column)
    freq = [(rule, column_matches_freq[rule][0], column_matches_freq[rule][1]) for rule in column_matches_freq]
    freq = sorted(freq, key=lambda x: x[1])
    rule, _, col = freq.pop(0)
    columns.append((rule, col))
    del rules[rule]
    no_check_column.append(col)
    find_columns(rules, tickets, no_check_column, columns)
    return columns


def part2():
    lines = read_input_lines()
    tickets = [[int(l) for l in lines[i].split(",")] for i in range(25, len(lines))]
    temp = []
    for i in range(len(tickets)):
        if i not in ids:
            temp.append(tickets[i])
    tickets = temp
    rules = create_rule_dict()
    my_ticket = [int(l) for l in lines[22].split(",")]
    tickets.append(my_ticket)
    columns = find_columns(rules, tickets, [], [])
    print(columns)
    departure_values = [my_ticket[c] for r, c in columns if "departure" in r]
    result = 1
    for val in departure_values:
        result *= val
    return result

s, ids = part1()
print(s)
print(part2())

