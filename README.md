# Car Advertisement Data Analysis and Visualization

https://software-development-tools-zsfp.onrender.com

## Description
This project involves analyzing and visualizing a car advertisement dataset using various Python libraries such as pandas, streamlit, plotly.express, and altair. The goal is to perform an exploratory data analysis (EDA) and create an interactive web application dashboard to present the insights.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Git
- Virtual environment (optional but recommended)

### Installation
1. **Create a GitHub Account**: [Sign up for GitHub](https://github.com/join) if you don't have an account.

2. **Create a Repository**: Create a new repository on GitHub with a `README.md` file and a `.gitignore` file (choose Python template).

3. **Clone the Repository**: Clone your new repository to your local machine.
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

4. **Set Up Python Environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install pandas streamlit plotly.express altair
    ```

5. **Create a Render.com Account**: [Sign up for Render](https://render.com/) and link it to your GitHub account.

6. **Install VS Code**: [Download and install VS Code](https://code.visualstudio.com/).

7. **Open the Project in VS Code**: Open the project directory in VS Code.

8. **Set Python Interpreter**: In VS Code, set the Python interpreter to the one used by the virtual environment.

### Download the Data File
Download the car advertisement dataset (vehicles_us.csv) or find your own dataset in CSV format. Place the dataset in the root directory of the project.

### Exploratory Data Analysis (EDA)
1. **Create a Jupyter Notebook**: Create an `EDA.ipynb` notebook in the `notebooks` directory.
2. **Perform Analysis**: Conduct basic exploratory analysis and create histograms and scatterplots using plotly-express library.

### Develop the Web Application Dashboard
1. **Create app.py**: Create an `app.py` file in the root of the project directory.
2. **Import Libraries**: Import streamlit, pandas, and plotly.express in `app.py`.
3. **Read Dataset**: Load the CSV file into a Pandas DataFrame.
4. **Add Components**: Add at least one header, one histogram, one scatter plot, and one checkbox using Streamlit.

### Deploy to Render
1. **Create requirements.txt**:
    ```text
    pandas==2.0.3
    scipy==1.11.1
    streamlit==1.25.0
    altair==5.0.1
    plotly==5.15.0
    ```
2. **Create config.toml**:
    Create a `.streamlit` directory and add a `config.toml` file with the following content:
    ```toml
    [server]
    headless = true
    port = 10000

    [browser]
    serverAddress = "0.0.0.0"
    serverPort = 10000
    ```
3. **Link GitHub Repository**: On Render.com, create a new web service linked to your GitHub repository.
4. **Configure Build and Start Commands**:
    - Build Command: `pip install streamlit & pip install -r requirements.txt`
    - Start Command: `streamlit run app.py`
5. **Deploy**: Deploy the application and verify it at `https://<APP_NAME>.onrender.com/`.

## Usage
To run the application locally, use the following command:
```bash
streamlit run app.py
