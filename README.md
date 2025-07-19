# PyFinance Dashboard 💰📊

An interactive **Streamlit-based personal budget tracker** that helps users visualize their income, expenses, and savings using CSV data.

## 🌟 Features
- 📁 Upload your own `.csv` budget data (or use the sample)
- 📊 Visual breakdown of expenses by category
- 💰 Key metrics: Total Income, Total Expenses, and Net Savings
- 📈 Dynamic charts built with Plotly
- 🧠 Modular design with custom utility functions

## 🛠️ Tech Stack
- Python
- Streamlit
- Pandas
- Plotly
- Custom utility module (`budget_utils.py`)

## 📁 Project Structure
PyFinance/
├── app.py # Streamlit frontend
├── budget_utils.py # Helper functions for data analysis
├── data/
│ └── sample_data.csv # Sample input
├── requirements.txt
└── README.md

perl
Copy
Edit

## 🚀 How to Run
Install dependencies:

```bash
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
