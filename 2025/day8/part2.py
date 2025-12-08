from collections import defaultdict

def read_file(filename):
    with open(filename, encoding="utf-8") as file:
        lines = [line.split()[0] for line in file.read().split("\n")]
        return lines
    
def main():
    answer = 1
    filename = "input.csv"
    lines = read_file(filename)
    circuits = []
    for line in lines:
        x_coord, y_coord, z_coord = [int(x) for x in line.split(',')]
        circuits.append([x_coord, y_coord, z_coord])
    
    # get closest connections
    iterations = 0
    junction_distances = []
    evaluated_pairs = set()
    for i in circuits:
        for j in circuits:
            iterations += 1
            if i == j:
                continue
            if f"{i}{j}" not in evaluated_pairs and f"{j}{i}" not in evaluated_pairs:
                proposed_distance = ((i[0] - j[0])**2 + (i[1] - j[1])**2 + (i[2] - j[2])**2)**.5
                proposed_junctions = [i, j]
                junction_distances.append([proposed_distance, proposed_junctions])
                evaluated_pairs.add(f"{i}{j}")

    junction_distances.sort()
    i = 0
    final_circuits = []
    circuits_added = 0
    evaluated_pairs = []
    final_junction_1 = None
    final_junction_2 = None
    while i < 5943:
        _, candidate_junctions = junction_distances[i]

        circuit_to_add_to = []
        junction_1, junction_2 = candidate_junctions
        for new_junction in candidate_junctions:
            for circuit_index in range(len(final_circuits)):
                circuit = final_circuits[circuit_index]
                for junction in circuit:
                    if new_junction == junction:
                        if circuit_index not in circuit_to_add_to:
                            circuit_to_add_to.append(circuit_index)
        if [junction_1, junction_2] in evaluated_pairs or [junction_2, junction_1] in evaluated_pairs:
            pass
        elif i == 0 or len(circuit_to_add_to) == 0:
            final_circuits.append(candidate_junctions)
            circuits_added += 1
            evaluated_pairs.append(candidate_junctions)
            final_junction_1, final_junction_2 = junction_1, junction_2
        elif len(circuit_to_add_to) == 1:
            new_circuits = final_circuits[circuit_to_add_to[0]]
            for junction in candidate_junctions:
                if junction not in new_circuits:
                    new_circuits.append(junction)
            final_circuits[circuit_to_add_to[0]] = new_circuits
            circuits_added += 1
            evaluated_pairs.append(candidate_junctions)
            final_junction_1, final_junction_2 = junction_1, junction_2
        elif len(circuit_to_add_to) == 2:
            new_circuits = []
            combined_circuits = []
            for index in range(len(final_circuits)):
                if index not in circuit_to_add_to:
                    new_circuits.append(final_circuits[index])
                else:
                    for junction in final_circuits[index]:
                        combined_circuits.append(junction)
            # affected indexes
            for new_junction in candidate_junctions:
                if new_junction not in combined_circuits:
                    combined_circuits.append(new_junction)
            new_circuits.append(combined_circuits)
            final_circuits = new_circuits
            circuits_added += 1
            evaluated_pairs.append(candidate_junctions)
            final_junction_1, final_junction_2 = junction_1, junction_2
        i += 1

    lengths = [len(x) for x in final_circuits]
    lengths.sort(reverse=True)
    answer = final_junction_1[0] * final_junction_2[0]

    return answer

answer = main()
print(answer)
