# The Music Prescription - Streamlit Application

## Overview

**The Music Prescription** is a Streamlit-based web application that explores the relationship between music preferences and mental health. The app allows users to interact with a dataset on music preferences, analyze trends, and visualize the impact of different music genres on various mental health conditions.

## Features

1. **Data Cleaning and Preprocessing:**
   - **Loading Data:** The application reads in a CSV file (`mxmh_survey_results.csv`) containing survey results about music preferences and mental health.
   - **Data Cleaning:** Unnecessary columns such as `Timestamp` and `Permissions` are dropped, and missing values in critical columns are handled. The `BPM` (Beats Per Minute) column is filled with the median where data is missing.
   - **Outlier Handling:** Outliers in the `Age`, `BPM`, and `Hours per day` columns are filtered out based on a calculated upper and lower limit.

2. **Custom Styling:**
   - The application includes custom CSS (`designing.css`) to enhance the appearance of the app.

3. **Interactive Visualizations:**
   - Users can select from various visualization options to explore the relationship between music and mental health.
   - **Primary Streaming Service:** Displays the distribution of the primary streaming services used by participants.
   - **Impact of Music on Mental Health:** A pie chart showing how participants perceive the impact of music on their mental health.
   - **Favorite Genre:** A bar chart displaying the most popular music genres among participants.
   - **Influence of Favorite Genre on Mental Health:** Line charts showing the relationship between favorite genres and mental health conditions such as Insomnia, OCD, Depression, and Anxiety.
   - **Dependency of Genre and Various Factors on Mental Health:** Multiple bar charts visualizing how factors like age, hours of music per day, and specific mental health conditions relate to favorite music genres.

## Dataset Description

The dataset used in this project is sourced from a survey that examines the relationship between music listening habits and mental health. The dataset contains the following columns:

- **Age:** The age of the participant.
- **Primary streaming service:** The primary music streaming service used by the participant (e.g., Spotify, Apple Music).
- **While working:** Indicates whether the participant listens to music while working.
- **Instrumentalist:** Whether the participant plays a musical instrument.
- **Composer:** Whether the participant composes music.
- **Foreign languages:** Indicates the participant's knowledge of foreign languages.
- **Music effects:** The participant's perception of the impact of music on their mental health.
- **Fav genre:** The participant's favorite music genre (e.g., Rock, Pop, Classical).
- **BPM:** Beats Per Minute of the participant's favorite music.
- **Hours per day:** The number of hours per day the participant spends listening to music.
- **Insomnia:** Indicates whether the participant has insomnia.
- **OCD:** Indicates whether the participant has Obsessive-Compulsive Disorder (OCD).
- **Depression:** Indicates whether the participant has depression.
- **Anxiety:** Indicates whether the participant has anxiety.

This dataset serves as the foundation for the visualizations and analysis provided by the application, allowing users to explore how music preferences may correlate with mental health conditions.

## File Structure

- **app.py:** The main Python script containing the Streamlit application code.
- **mxmh_survey_results.csv:** The CSV dataset used for analysis.
- **designing.css:** Custom CSS file to style the application.
- **README.md:** Documentation for the project.

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/music-prescription.git
   cd music-prescription
