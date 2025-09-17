This project converts a CSV file containing daily revenue data into a SQLite database. The application reads the `daily_revenue.csv` file, processes the data, and stores it in a database named `demo.db`.

## Project Structure

```
csv-to-sqlite
├── src
│   ├── main.py        # Entry point of the application
│   └── utils.py       # Utility functions for CSV and SQLite operations
├── daily_revenue.csv   # CSV file containing daily revenue data
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

## Requirements

To run this project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

1. Place the `daily_revenue.csv` file in the project root directory.
2. Run the application using the following command:

```
python src/main.py
```

3. After running the application, a SQLite database named `demo.db` will be created in the project root directory containing the data from the CSV file.

## License

This project is open-source and available under the MIT License.
