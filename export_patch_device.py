import argparse
import yaml

def generate_patch_device_yaml(manufacturer, model, part_number, mpo_cables, lc_labels, output_file):
    data = {
        'manufacturer': manufacturer,
        'model': model,
        'part_number': part_number,
        'u_height': 1,
        'is_full_depth': False,
        'front-ports': [],
        'rear-ports': []
    }

    # Generate front-ports
    for mpo in range(1, mpo_cables + 1):
        for lc in range(1, lc_labels + 1):
            data['front-ports'].append({
                'name': f'mpo{mpo}-{lc}',
                'type': 'lc',
                'rear_port': f'mpo{mpo}',
                'rear_port_position': lc
            })

    # Generate rear-ports
    for mpo in range(1, mpo_cables + 1):
        data['rear-ports'].append({
            'name': f'mpo{mpo}',
            'type': 'mpo',
            'positions': lc_labels
        })

    with open(output_file, 'w') as f:
        yaml.dump(data, f, sort_keys=False)


def main():
    """
    Parses command-line arguments to export a patch device YAML file.
    Arguments:
        --manufacturer (str): The manufacturer name (required).
        --model (str): The model name (required).
        --part_number (str): The part number (required).
        --mpo_cables (int): The number of MPO cables (required).
        --lc_labels (int): The number of LC labels (required).
        --output_file (str): The output YAML file path (required).
    Example usage:
        python export_patch_device.py \
            --manufacturer "GENERIC PATCH" \
            --model "NOC-24LC x4 MPO Cassette" \
            --part_number "NOC-24LC-X4-MPO-Cassette" \
            --mpo_cables 4 \
            --lc_labels 24 \
            --output_file "generic/NOC-24LC-X4-MPO-Cassette.yml"
    """
    parser = argparse.ArgumentParser(description='Export patch device YAML file.')
    parser.add_argument('--manufacturer', required=True)
    parser.add_argument('--model', required=True)
    parser.add_argument('--part_number', required=True)
    parser.add_argument('--mpo_cables', type=int, required=True)
    parser.add_argument('--lc_labels', type=int, required=True)
    parser.add_argument('--output_file', required=True)
    args = parser.parse_args()

    generate_patch_device_yaml(
        manufacturer=args.manufacturer,
        model=args.model,
        part_number=args.part_number,
        mpo_cables=args.mpo_cables,
        lc_labels=args.lc_labels,
        output_file=args.output_file
    )

if __name__ == '__main__':
    main()
