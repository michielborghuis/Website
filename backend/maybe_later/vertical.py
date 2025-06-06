import json

def read_network(filename: str) -> np.ndarray: # TODO
    with open(filename) as read_file:
        out = []
        data = json.load(read_file)
        size_in = int(data['layer1']['size_in'])
        size_out = int(data['layer1']['size_out'])
        for item in range(0, size_in):
            horizontal = []
            for value in range(0, size_out):
                try:
                    horizontal.append(data['layer1']['weights'][str(item+1)][str(value+1)])
                except:
                    horizontal.append("0")
            out.append(horizontal)
        return np.array(out)

print(read_network('example.json'))

# def run_network(filename: str, input_vector: np.ndarray) -> np.ndarray: # TODO
#     pass