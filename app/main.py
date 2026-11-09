import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from ultralytics import YOLO
from PIL import Image

from app.sensors.distance_sensor import simulate_distance

st.set_page_config(
    page_title="Assistive Navigation Simulator",
    layout="wide"
)

st.title("Assistive Navigation Simulator")
st.caption("AI-powered obstacle detection and navigation")

@st.cache_resource
def load_model():
    return YOLO("yolo11n.pt")

model = load_model()

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    results = model(image, conf=0.15)

    result = results[0]
    detected_objects = result.boxes

    annotated_image = result.plot()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image)

    with col2:
        st.subheader("Object Detection")
        st.image(annotated_image)

    st.metric("Detected Objects", len(detected_objects))

    st.subheader("Detection Results")

    for box in detected_objects:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        object_name = model.names[class_id]

        st.write(
            f"{object_name} — Confidence: {confidence:.2f}"
        )
        distance = simulate_distance()

        st.write(
            f"{object_name} | "
            f"Confidence: {confidence:.2f} | "
            f"Distance: {distance} m"
        )

else:
    st.info("Upload an image to begin detection.")
