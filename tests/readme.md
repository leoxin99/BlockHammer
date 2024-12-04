# BlockHammer Simulation

This repository contains the BlockHammer simulation using Ramulator. Follow the instructions below to set up and run the simulation.

## Prerequisites

- Git
- Git LFS
- C++ Compiler (e.g., g++)
- Python 3.x
- Required Python packages: pandas, matplotlib, seaborn

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/leoxin99/BlockHammer.git
   cd BlockHammer
   ```

2. **Build the Ramulator environment:**

   Navigate to the `ramulator` directory and build the project:

   ```bash
   cd ramulator
   make
   ```

## Configuration

1. **Edit Configuration:**

   Modify the `configs/DDR4-config.cfg` file to set your desired simulation parameters.

2. **Set Up Environment:**

   Ensure all dependencies are installed and environment variables are set if needed.

## Running the Simulation

1. **Execute the simulation:**

   Run the simulation script:

   ```bash
   bash tests/test_blockhammer.sh
   ```

2. **Collect Results:**

   Use the `collect_results.py` script to parse and collect simulation results:

   ```bash
   python collect_results.py ./datadir
   ```

3. **Generate Plots:**

   Use the `plot.py` script to generate plots from the results:

   ```bash
   python tests/plot.py
   ```

## Troubleshooting

- Ensure all dependencies are installed.
- Check file paths and permissions if errors occur.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Based on the work by A. Giray Yaglikci et al., "BlockHammer: Preventing RowHammer at Low Cost by Blacklisting Rapidly-Accessed DRAM Rows," HPCA 2021.enting RowHammer at Low Cost by Blacklisting Rapidly-Accessed DRAM Rows," HPCA 2021.