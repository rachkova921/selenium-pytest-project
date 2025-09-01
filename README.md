# Selenium Pytest Project

This is a simple test automation project using **Selenium** and **Pytest**.

## 📂 Project structure
\`\`\`
selenium-pytest-project/
├── conftest.py          # Pytest configuration (browser fixture, language parameter)
├── requirements.txt     # Project dependencies
├── __init__.py          # Empty file for relative imports
├── test_main_page.py    # Example test
└── README.md            # Project description
\`\`\`

## ⚙️ Setup
1. Create a virtual environment:
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate   # Mac/Linux
   .\\venv\\Scripts\\activate    # Windows
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## ▶️ Run tests
To run the test with English interface:
\`\`\`bash
pytest -v --tb=line --language=en test_main_page.py
\`\`\`

You can also change the interface language:
\`\`\`bash
pytest -v --tb=line --language=ru test_main_page.py
\`\`\`
EOF
