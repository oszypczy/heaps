# Heaps readme file

This repository contains a Python implementation of a heap data structure and provides functions to analyze the performance of creating heaps and removing the root element.

## Usage

### Prerequisites

To run the code in this repository, you need to have Python installed on your system. The code is compatible with Python 3.x.

### Installation

1. Clone the repository to your local machine or download the source code files.
2. Make sure you have the required dependencies installed. You can install the dependencies by running the following command:
   ```
   pip install matplotlib
   ```
   
### Running the Code

The main functionality of the code is defined in the `main()` function of the `main.py` file. To execute the code, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you cloned or downloaded the repository.
3. Run the following command:
   ```
   python main.py
   ```

### Functionality

The code provides the following functionality:

1. Creating Heap Creation Time Graphs: The `get_creation_heap_graphs` function creates graphs to compare the creation times of heaps with different numbers of children. It generates three graphs, each representing a heap with 2-ary, 3-ary, and 4-ary nodes. The x-axis represents the collection size, and the y-axis represents the time taken to create the heap in seconds. The graphs are saved as image files in the `heap_graphs` directory.

2. Creating Heap Removal Time Graphs: The `get_remove_root_heap_graphs` function creates graphs to compare the removal times of the root element from heaps with different numbers of children. Similar to the creation graphs, it generates graphs for heaps with 2-ary, 3-ary, and 4-ary nodes. The x-axis represents the collection size, and the y-axis represents the time taken to remove the root element in seconds. The graphs are saved as image files in the `heap_graphs` directory.

### Customization

You can customize the code to suit your needs. Here are a few points to consider:

- You can modify the `main` function in `main.py` to control the collection size and enable or disable specific operations. Currently, it generates a list of random numbers and calls the creation and removal graph functions.

- The `Heap` class in the `heap.py` file provides the implementation of the heap data structure. You can modify this class to experiment with different heap configurations or functionalities.

### Running Tests

The repository also includes some tests implemented using pytest. To run the tests, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you cloned or downloaded the repository.
3. Run the following command:
   ```
   pytest
   ```

The tests will be executed, and the results will be displayed in the terminal.

## License

This code is released under the MIT License. You can find the details in the `LICENSE` file.

## Acknowledgments

The code in this repository was developed as a demonstration of the heap data structure implementation and performance analysis. It is not intended for production use but rather as a learning resource.
