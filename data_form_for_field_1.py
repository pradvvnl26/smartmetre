import streamlit as st
import pandas as pd
import zipfile

st.set_page_config(page_title="Consumer Search", layout="centered")

st.title("Genus Daily Billing Status")

# =========================================
# READ CSV FROM RAR
# =========================================
zip_path = "data_for_web_from.zip"

with zipfile.ZipFile(zip_path) as z:
    
    csv_file = z.namelist()[0]

    with z.open(csv_file) as f:
        
        df = pd.read_csv(f, low_memory=False)


search = st.text_input("**Search WFM_CONSUMER_NO/ WFM_METER_NO / CCB_ACCT_ID / CCB_METER_NO**")
# st.markdown("**Search Consumer Number / RMS ACC / RMS MTR**")
# search = st.text_input("")

if search:

    search = str(search).strip()

    result = df[
        (df["Consumer Number"].astype(str).str.strip() == search) |
        (df["Scan New Meter Serial No"].astype(str).str.strip() == search) |
        (df["ACCT_ID"].astype(str).str.strip() == search) |
        (df["METER_BADGE_NO"].astype(str).str.strip() == search)
    ]

    if not result.empty:

        row = result.iloc[0]

        st.subheader("**Consumer Details**")

        st.markdown("""
        <style>
        input[disabled] {
            color: green !important;
            font-weight: bold !important;
        }
        </style>
        """, unsafe_allow_html=True)


        st.markdown("**WFM_COSNUMER_NO**")
        st.text_input("WFM_COSNUMER_NO", row["Consumer Number"], disabled=True, label_visibility="collapsed")

        st.markdown("**WFM_METER_NO**")
        st.text_input("WFM_METER_NO", row["Scan New Meter Serial No"], disabled=True, label_visibility="collapsed")

        st.markdown("**CCB_ACCT_ID**")
        st.text_input("CCB_ACCT_ID", str(row["ACCT_ID"]).replace(".0", ""), disabled=True, label_visibility="collapsed")

        # st.markdown("**CCB_ACCT_ID**")
        # st.text_input("CCB_ACCT_ID", int(row["ACCT_ID"]), disabled=True, label_visibility="collapsed")

        st.markdown("**CCB_SERIAL_NO**")
        st.text_input("CCB_SERIAL__NO", row["SERIAL_NBR"], disabled=True, label_visibility="collapsed")

        st.markdown("**CCB_METER_BADGE_NO**")
        st.text_input("CCB_METER_BADGE_NO", row["METER_BADGE_NO"], disabled=True, label_visibility="collapsed")

        st.markdown("**CCB_LOAD_IN_KW**")
        st.text_input("CCB_LOAD_IN_KW", str(row["LOAD_IN_KW"]).replace(".0", ""), disabled=True, label_visibility="collapsed")

        st.markdown("**L1_STATUS**")
        st.text_input("L1_STATUS", row["L1 Approval Status"], disabled=True, label_visibility="collapsed")

        st.markdown("**L1_STATUS_DATE**")
        st.text_input("L1_STATUS_DATE", row["L1 Approval Date"], disabled=True, label_visibility="collapsed")

        st.markdown("**L2_STATUS**")
        st.text_input("L2_STATUS", row["L2 Approval Status"], disabled=True, label_visibility="collapsed")

        st.markdown("**L2_STATUS_DATE**")
        st.text_input("L2_STATUS_DATE", row["L2 Approval Date"], disabled=True, label_visibility="collapsed")

        st.markdown("**MCO_STATUS**")
        st.text_input("MCO_STATUS", row["mco done or not"], disabled=True, label_visibility="collapsed")

        st.markdown("**BILLING_PROFILE_STATUS**")
        st.text_input("BILLING_PROFILE_STATUS", row["billing profile available or not"], disabled=True, label_visibility="collapsed")

        st.markdown("**METER_STATUS**")
        st.text_input("METER_STATUS", row["communication status"], disabled=True, label_visibility="collapsed")

        st.markdown("**READ_STATUS**")
        st.text_input("READ_STATUS", row["read share status"], disabled=True, label_visibility="collapsed")

        st.markdown("**BILLED_STATUS**")
        st.text_input("BILLED_STATUS", row["billing status"], disabled=True, label_visibility="collapsed")

        st.markdown("**MCO_ERROR_STATUS**")
        st.text_input("MCO_ERROR_STATUS", row["mco error remark"], disabled=True, label_visibility="collapsed")

        st.markdown("**METER_CHANGE**")
        st.text_input("METER_CHANGE", row["O & M Meter"], disabled=True, label_visibility="collapsed")

        st.markdown("**MC_L2_STATUS**")
        st.text_input("MC_L2_STATUS", row["O & M L2 Status"], disabled=True, label_visibility="collapsed")

        st.markdown("**MC_L2_STATUS_DATE**")
        st.text_input("MC_L2_STATUS_DATE", row["O & M L2 Approval Date"], disabled=True, label_visibility="collapsed")
    
    
    else:
        st.error("Record Not Found")

st.markdown(
    """
    <div style='text-align: right;
                color: gray;
                font-size: 14px;
                margin-top: 40px;'>
        Designed by <b>Mr Amit</b>
    </div>
    """,
    unsafe_allow_html=True
)

