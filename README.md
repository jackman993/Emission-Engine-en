# Carbon Emission Calculator

Quick deployment package for Streamlit Cloud.

## Files

```
emission-app/
├── app.py              # Main entry
├── emission_calc.py    # Calculation engine
├── requirements.txt    # Dependencies
└── pages/
    └── Calculator.py   # Main calculator page
```

## Local Run

```bash
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push to GitHub
2. Go to share.streamlit.io
3. Connect repository
4. Main file: `app.py`
5. Deploy

Your app will be at: `https://your-username-emission-app.streamlit.app`

## Features

- ✅ Multi-region support (TW/US/EU/CN/JP)
- ✅ Quick mode (monthly bill)
- ✅ Detailed mode (full data)
- ✅ Scope 1, 2, 3 (minor) emissions
- ✅ Download report
