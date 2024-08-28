# NY Times Article Analysis

This project involves scraping article headlines from the New York Times for specific months and years (e.g., October 1918) using the NY Times Archive API. The scraped data is then analyzed to gain insights such as word frequency, sentiment analysis, and the presence of specific keywords.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Data Collection](#data-collection)
4. [Data Analysis](#data-analysis)
5. [Results](#results)
6. [Future Work](#future-work)
7. [License](#license)

## Project Overview

This project is focused on collecting and analyzing headlines from the New York Times archives. The analysis includes word frequency counts, sentiment analysis, and the identification of specific keywords within the headlines. The project is divided into two main scripts: `data_collection.py` for scraping the data and `analysis.py` for performing the analysis.

## Installation

To run this project, you'll need to have Python installed along with the following Python libraries:

1. **requests** - For making HTTP requests to the NY Times API.
2. **vaderSentiment** - For performing sentiment analysis.
3. **re** - For regular expression operations (used for data cleaning).
4. **string** - For handling string operations.

You can install the required libraries using pip:

## Data Collection

The `data_collection.py` script is responsible for fetching article headlines from the New York Times API. Below is a brief overview of how the script works:

### Setting Parameters

- You specify the month, year, and your `api_key` for the NY Times API.
- The script constructs the API URL based on these parameters.

### Fetching Data

- The script sends an HTTP GET request to the NY Times API and retrieves the data in JSON format.

### Extracting Headlines

- The script parses the JSON response to extract article headlines.
- These headlines are saved in a text file (e.g., `titles_1918.txt`).


## Data Analysis

The `analysis.py` script performs various analyses on the collected data. Here's a breakdown of what the script does:

### Word Frequency Analysis

- Counts the most frequent words in the headlines from the specified files.
- Outputs the top 10 most frequent words.

### Keyword Frequency

- Calculates the frequency of specific keywords (e.g., "flu", "death", "virus") in the headlines.

### Sentiment Analysis

- Uses the `vaderSentiment` library to calculate the average sentiment score of the headlines. This score reflects whether the overall tone of the articles is positive, negative, or neutral.

### Dollar Amount Extraction

- Extracts and sums up any dollar amounts mentioned in the headlines, providing insight into the financial aspects discussed in the articles.

## Results

After running the analysis, the following insights were obtained:

- **Most Frequent Words:** The top 10 most frequently occurring words in the headlines for each specified year (e.g., 1918, 2020).
- **Keyword Mentions:** The fraction of headlines that include key terms such as "flu," "death," and "virus," offering insights into the prevalent topics during those periods.
- **Dollar Amounts:** The total sum of any dollar amounts mentioned in the headlines, which can give an idea of the financial discussions or impacts reported in the articles.
- **Sentiment Analysis:** The average sentiment score for the headlines, indicating whether the overall tone of the articles was positive, negative, or neutral.


