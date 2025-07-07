
import streamlit as st
import pandas as pd
import datetime
from io import BytesIO

st.set_page_config(page_title="NEPSE Profit Analyzer", layout="centered")

st.title("📈 NEPSE Profit Analyzer")
st.markdown("Smart stock rotation tool to **maximize profit** and minimize risk.")

# Sample stock analysis data
data = {
    "Stock": ["UPPER", "NLO", "CBBL", "SHPC", "NICA"],
    "Status": ["BUY", "BUY", "HOLD", "HOLD", "SELL"],
    "Entry Price": [196, 292, 950, 385, 615],
    "Stop-Loss": [194, 280, 930, 374, 600],
    "Target Price": [204, 310, 1000, 410, 580],
    "Notes": [
        "Near support. Good short/mid term entry.",
        "Long-term undervalue. Hold or add.",
        "Wait for breakout or dip below 940.",
        "Good hydro stock. Buy near 380.",
        "Weak momentum. Consider exit soon."
    ]
}

df = pd.DataFrame(data)

# Show current stock suggestions
st.subheader("📊 Today's Stock Suggestions")
st.dataframe(df, use_container_width=True)

# Downloadable Excel file
def convert_df_to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='NEPSE Analysis')
    writer.save()
    processed_data = output.getvalue()
    return processed_data

excel_data = convert_df_to_excel(df)
st.download_button(
    label="📥 Download Stock Report (Excel)",
    data=excel_data,
    file_name=f"nepse_profit_report_{datetime.date.today()}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

st.info("Check back daily for updated recommendations.")
