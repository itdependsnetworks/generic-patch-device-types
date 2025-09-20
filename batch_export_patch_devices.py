import subprocess

# List of device definitions: (manufacturer, model, part_number, mpo_cables, lc_labels, output_file)
devices = [
    ("Corning", "Corning 24LC", "Corning-24LC", 1, 24, "generic/Corning-24LC.yml"),
    ("Corning", "Corning144LC", "Corning-144LC", 6, 24, "generic/Corning-144LC.yml"),
    ("ADC", "ADC 24", "ADC-24", 1, 24, "generic/ADC-24.yml"),
    ("GENERIC PATCH", "Multilink 24LC", "Multilink-24LC", 1, 24, "generic/Multilink-24LC.yml"),
    ("GENERIC PATCH", "NOC-24LC x1 MPO Cassette", "NOC-24LC-X1-MPO-Cassette", 1, 24, "generic/NOC-24LC-X1-MPO-Cassette.yml"),
    ("GENERIC PATCH", "NOC-24LC x2 MPO Cassette", "NOC-24LC-X2-MPO-Cassette", 2, 24, "generic/NOC-24LC-X2-MPO-Cassette.yml"),
    ("GENERIC PATCH", "NOC-24LC x3 MPO Cassette", "NOC-24LC-X3-MPO-Cassette", 3, 24, "generic/NOC-24LC-X3-MPO-Cassette.yml"),
    ("GENERIC PATCH", "NOC-24LC x4 MPO Cassette", "NOC-24LC-X4-MPO-Cassette", 4, 24, "generic/NOC-24LC-X4-MPO-Cassette.yml"),
    ("GENERIC PATCH", "NOC-36LC x3 MPO Cassette", "NOC-36LC-X3-MPO-Cassette", 3, 36, "generic/NOC-36LC-X3-MPO-Cassette.yml"),
    ("GENERIC PATCH", "NOC-36LC x2 MPO Cassette", "NOC-36LC-X2-MPO-Cassette", 2, 36, "generic/NOC-36LC-X2-MPO-Cassette.yml"),
    ("GENERIC PATCH", "NOC-36LC x1 MPO Cassette", "NOC-36LC-X1-MPO-Cassette", 1, 36, "generic/NOC-36LC-X1-MPO-Cassette.yml"),
    ("GENERIC PATCH", "NOC-36LC x4 MPO Cassette", "NOC-36LC-X4-MPO-Cassette", 4, 36, "generic/NOC-36LC-X4-MPO-Cassette.yml"),
    ("Corning", "Corning12LC", "Corning-12LC", 1, 12, "generic/Corning-12LC.yml"),
    ("GENERIC PATCH", "NOC-12LC x1 MPO Cassette", "NOC-12LC-X1-MPO-Cassette", 1, 12, "generic/NOC-12LC-X1-MPO-Cassette.yml"),
    ("GENERIC PATCH", "NOC-12LC x2 MPO Cassette", "NOC-12LC-X2-MPO-Cassette", 2, 12, "generic/NOC-12LC-X2-MPO-Cassette.yml"),
]

for manufacturer, model, part_number, mpo_cables, lc_labels, output_file in devices:
    cmd = [
        "python", "export_patch_device.py",
        "--manufacturer", manufacturer,
        "--model", model,
        "--part_number", part_number,
        "--mpo_cables", str(mpo_cables),
        "--lc_labels", str(lc_labels),
        "--output_file", output_file
    ]
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
