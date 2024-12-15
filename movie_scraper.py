# file path: movie_scraper.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from imdb_scraper import scrape_imdb  # Import the scrape_imdb function

class IMDbScraperGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up main window properties
        self.setWindowTitle("IMDb Scraper")
        self.setGeometry(100, 100, 900, 600)

        # Dropdown for choosing scrape option
        self.choice_box = QComboBox()
        self.choice_box.addItems(["Box Office Top 10", "Popular Movies"])

        # Button to trigger scrape
        self.scrape_button = QPushButton("Scrape IMDb")
        self.scrape_button.clicked.connect(self.run_scraper)

        # Table to display results
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(2)  # Start with 2 columns (Title, Rating)
        self.results_table.setHorizontalHeaderLabels(["Title", "Rating"])

        # Set custom font size for each item
        font = QFont()
        font.setPointSize(20)  # Set desired font size

        # Enable sorting by clicking on column headers
        self.results_table.setSortingEnabled(True)  

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.choice_box)
        layout.addWidget(self.scrape_button)
        layout.addWidget(self.results_table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_scraper(self):
        # Get user choice from the dropdown
        choice = self.choice_box.currentText()

        try:
            # Run the scraper function
            results = scrape_imdb(choice)

            # Update column headers based on the selected choice
            if choice == "Popular Movies":
                self.results_table.setColumnCount(5)  # 6 columns for Title, Rating, Year, Runtime, Age Rating, Link
                self.results_table.setHorizontalHeaderLabels(["Title", "Rating", "Year", "Runtime", "Age Rating"])
            else:
                self.results_table.setColumnCount(2)  # 3 columns for Title, Rating, Link
                self.results_table.setHorizontalHeaderLabels(["Title", "Rating"])

            # Set row count to match the number of results
            self.results_table.setRowCount(len(results))

            # Populate the table with data
            for row, data in enumerate(results):
                # Add title with hyperlink in the first column
                title_item = QTableWidgetItem(data[0])  # Movie Title
                title_item.setData(Qt.UserRole, data[2])  # IMDb URL (assuming it's the third element in the tuple)
                title_item.setForeground(Qt.blue)  # Blue text for hyperlink
                title_item.setToolTip("Click to open IMDb page")
                title_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)  # Enable selection and interaction
                self.results_table.setItem(row, 0, title_item)  # Add title with hyperlink

                # Add rating in the second column
                self.results_table.setItem(row, 1, QTableWidgetItem(data[1]))  # Add rating

                # Add other data based on choice
                if choice == "Popular Movies":
                    self.results_table.setItem(row, 2, QTableWidgetItem(data[3]))  # Add year
                    self.results_table.setItem(row, 3, QTableWidgetItem(data[4]))  # Add runtime
                    self.results_table.setItem(row, 4, QTableWidgetItem(data[5]))  # Add age rating

            self.results_table.setColumnWidth(0, 300)

            # Connect the table's cellDoubleClicked signal
            self.results_table.cellDoubleClicked.connect(self.open_link)

        except Exception as e:
            # Show an error message if something goes wrong
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")


    def open_link(self, row, column):
        if column == 0:  # If the clicked cell is in the title column
            item = self.results_table.item(row, column)
            if item and item.data(Qt.UserRole):  # Check if there's a URL stored
                import webbrowser
                webbrowser.open(item.data(Qt.UserRole))  # Open the IMDb link in a browser


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IMDbScraperGUI()
    window.show()
    sys.exit(app.exec_())
