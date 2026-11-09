
import streamlit as st

st.set_page_config(
    page_title="Assistive Navigation Simulator",
    page_icon="",
    layout="wide"
)

st.title("Assistive Navigation Simulator")
st.caption("AI-powered obstacle detection and navigation")

st.divider()

# Navigation status
col1, col2, col3 = st.columns(3)

col1.metric("Detected Objects", 0)
col2.metric("Risk Level", "Safe")
col3.metric("Navigation", "Ready")

st.divider()

# Main interface
left, right = st.columns(2)

with left:
    st.subheader("Environment")
    st.info("Upload an image to begin obstacle detection.")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Environment")

with right:
    st.subheader("Navigation Analysis")

    st.write("**Sensor Fusion**")
    st.info("Waiting for sensor data")

    st.write("**Risk Zones**")
    st.info("No obstacles detected")

    st.write("**Navigation Recommendation**")
    st.info("Waiting for environment analysis")
