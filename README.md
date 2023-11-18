
# ![img](./img/capstone-analytics-header.png)

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/christinedbaxter/analyticsCapstone?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/christinedbaxter/analyticsCapstone)
![GitHub pull requests](https://img.shields.io/github/issues-pr/christinedbaxter/analyticsCapstone)
![GitHub](https://img.shields.io/github/license/christinedbaxter/analyticsCapstone)
![contributors](https://img.shields.io/github/contributors/christinedbaxter/analyticsCapstone)
![codesize](https://img.shields.io/github/languages/code-size/christinedbaxter/analyticsCapstone)

# Current Status

In Progress

# Project Overview

This project explores the complex relationship between atmospheric pressure changes and migraine occurrences. The study utilizes extensive weather and health data to investigate whether there is a significant correlation between annual average sea-level pressure and migraine frequency in various geographic locations.

# Business Issues

The study addresses the need for understanding migraine triggers, particularly the role of weather conditions. The aim is to aid in developing predictive tools for individuals suffering from migraines and to enhance health strategies for mitigating the impact of migraines.

# Installation and Setup

In this section, provide detailed instructions on how to set up the project on a local machine. This includes any necessary dependencies, software requirements, and installation steps. Make sure to include clear and concise instructions so that others can easily replicate your setup.

## Codes and Resources Used

- **Editor Used:**  Visual Studio Code
- **Python Version:** 3.8.5

## Python Packages Used

In this section, I include all the necessary dependencies needed to reproduce the project, so that the reader can install them before replicating the project. I categorize the long list of packages used as -

- **General Purpose:** General purpose packages like `urllib, os, request`, and many more.
- **Data Manipulation:** Packages used for handling and importing dataset such as `pandas, numpy` and others.
- **Data Visualization:** Include packages which were used to plot graphs in the analysis or for understanding the ML modelling such as `seaborn, matplotlib` and others.
- **Machine Learning:** This includes packages that were used to generate the ML model such as `scikit, tensorflow`, etc.

# Data

## Source Data

- **Weather Dataset [Servera 2023]**: Contains over 27 million data points from daily weather patterns.
- **Migraine Dataset [IHME 2019]**: Comprises 1.4 million data points from the Global Burden of Disease study.

## Data Acquisition

- Utilized a custom Python script (`raw_data.py`) for streamlined data loading.
- Loaded several key datasets including city, country, weather, and migraine data.
- Ensured the integrity and structure of the data by displaying sample rows from each dataset.
- Initial datasets include:
  - **City Data**: Information about various cities.
  - **Country Data**: Details pertaining to different countries.
  - **Weather Data**: Meteorological information relevant to the study.
  - **Migraine Data**: Dataset containing migraine incidence and related details.

## Data Preprocessing

- Performed comprehensive data examination and preprocessing to ensure data quality.
- Implemented rigorous checks for missing values and zero counts to identify and handle data anomalies.
- Utilized advanced Python libraries like `seaborn`, `folium`, and `missingno` for data visualization and analysis.
- Applied custom functions for data conversion and manipulation, enhancing the accuracy and relevance of the analysis.

## Data Quality Checks

- Conducted an initial assessment of the datasets to identify missing values and potential data issues.
- Employed statistical methods to understand data distributions and identify outliers.

## Data Cleaning and Transformation

- Implemented strategies to handle missing values, including imputation techniques.
- Transformed and normalized key data fields for consistency and better analysis.

# Data Analysis

- Conducted in-depth analysis using the `migraine_weather` DataFrame, a combined dataset derived from migraine and weather data.
- Utilized advanced statistical techniques to explore and understand the characteristics of the dataset.
- Performed a comprehensive overview of the data, including type-checking and null value identification.

## Descriptive Analysis

- Generated descriptive statistics to understand the distribution and central tendencies of the data.
- Checked for null values and anomalies in the dataset to ensure data integrity.

## Analytical Techniques Employed

- Applied various statistical methods to identify patterns and relationships within the data.
- Employed visualization tools like `matplotlib` and `seaborn` for a clearer understanding of data trends.

# Code structure

Explain the code structure and how it is organized, including any significant files and their purposes. This will help others understand how to navigate your project and find specific components.

Here is the basic suggested skeleton for your data science repo (you can structure your repository as needed ):

```bash
├── data
│   ├── data1.csv
│   ├── data2.csv
│   ├── processed
│       ├── migraine_weather.csv
|       └── weather_city_country.csv
├── data_acquisition.ipynb
├── data_preprocessing.ipynb
├── data_analysis.ipynb
├── Img
│   ├── Capstone-analytics-header.png
├── LICENSE
├── README.md
└── .gitignore
```

# Results and evaluation

## Exploratory Analysis and Modeling

- The study initially found no significant correlation between average sea-level pressure and migraine occurrences.
- Further analysis revealed a significant relationship between pressure variability and migraine frequency.

### Univariate Analysis

- Conducted univariate analysis to understand the distribution of the data.
- Utilized various visualization tools like `matplotlib` and `seaborn` to generate graphs and charts.

### Statistical Analysis

- Performed statistical analysis to identify patterns and relationships within the data.
- Conduct correlation analysis between sea-level pressure and migraine occurrences.
- Perform hypothesis testing to determine if the observed correlation is statistically significant.
- Explore regression analysis if appropriate, considering other variables that may affect migraines.

---

## Data Visualization and Presentation

Various visualization tools were used, including Python libraries like Matplotlib, Folio, and Seaborn.


# Future work

Future research could focus on the identified significant weather factors, especially pressure changes and precipitation, to develop predictive models for migraine occurrences based on weather patterns.

# GitHub Versioning/Workflow

By adhering to the workflow discussed below, the project maintains a high level of code integrity, streamlines collaboration, and enables seamless tracking of project milestones.

## Branching Strategy

1. **Initialization**: Created an initial `develop` branch as the base for development.
2. **Feature Branches**: For each major stage of the project, a dedicated feature branch was created off of the `develop` branch.

## Commit and Merge Workflow

1. **Commit Changes**: After the completion of each stage, all changes were committed to the respective feature branch.
2. **Code Reviews and Merges**: The feature branch was then merged into the `develop` branch post-review.
3. **Creating New Feature Branches**: A new feature branch was created from the updated `develop` branch for the next stage of the project.
4. **Final Merge**: Upon completion of all stages, the `develop` branch was merged into the `main` branch through a pull request.

---

# Issues and Questions

- List of known issues and questions for further investigation.

For any issues with the code or data, please use the [GitHub Issues template](./.github/ISSUE_TEMPLATE.md) provided in the repository. For general questions or discussions, feel free to reach out via the contact methods listed above.

---

We welcome contributions to ________________! To contribute, please follow these steps:

1. Fork the ______ repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m "Add your commit message"`
4. Push your changes to the branch: `git push origin feature/your-feature-name`
5. Submit a [pull request](./.github/PULL_REQUEST_TEMPLATE.md)

Please make sure to follow our [Contributing Guidelines](CONTRIBUTING.md) for detailed information on the contribution process and code standards.

---

# Acknowledgments/References

Acknowledge any contributors, data sources, or other relevant parties who have contributed to the project. This is an excellent way to show your appreciation for those who have helped you along the way.

- Header Image by graphicINmotion/#189360493 – stock.adobe.com, modified by me in Adobe Express.
- [README Template](https://medium.datadriveninvestor.com/how-to-write-a-good-readme-for-your-data-science-project-on-github-ebb023d4a50e-)
Verma, P. (2023). How to write a good readme for your data science project on GitHub.
- [Badges](https://shields.io/)
- Special thanks to OpenAI's ChatGPT for providing valuable insights and guidance on various technical aspects of this project.

# License

Specify the license under which your code is released. Moreover, provide the licenses associated with the dataset you are using. This is important for others to know if they want to use or contribute to your project.

For this github repository, the License used is [MIT License](https://opensource.org/license/mit/).
