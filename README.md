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

```bash
pip install requests vaderSentiment
