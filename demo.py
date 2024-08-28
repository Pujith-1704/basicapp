import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Text elements
st.header("Streamlit UI Elements")
st.subheader("Explore different UI components")
st.text("Simple text display")
st.markdown("**Markdown** formatting")
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.code('print("Hello, World!")')

# Input Widgets
if st.button("Click me"):
    st.write("Button clicked!")
option = st.radio("Choose one:", ['A', 'B', 'C'])
st.write(f"You chose: {option}")
if st.checkbox("Check me"):
    st.write("Checked!")
selectbox_option = st.selectbox("Pick one:", ['Item 1', 'Item 2', 'Item 3'])
st.write(f"Selected: {selectbox_option}")
multiselect_options = st.multiselect("Pick multiple:", ['A', 'B', 'C'])
st.write(f"Selected: {multiselect_options}")
slider_value = st.slider("Slide me:", 0, 100, 50)
st.write(f"Slider value: {slider_value}")
text_input = st.text_input("Enter text:")
st.write(f"Input: {text_input}")
number_input = st.number_input("Pick a number:", 0, 100, 10)
st.write(f"Number: {number_input}")
date_input = st.date_input("Pick a date:")
st.write(f"Date: {date_input}")
color = st.color_picker("Pick a color:")
st.write(f"Color: {color}")

# Data Display
df = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'])
st.dataframe(df)
st.table(df.head())
st.json({"name": "Streamlit", "type": "Demo"})

# Media
st.image("image.jpg", caption="Sample Image")
st.audio("audio.mp3")
st.video("video.mp4")

# Charts/Plots
st.line_chart(df)
st.bar_chart(df)

# Matplotlib plot
fig, ax = plt.subplots()
ax.plot(df.index, df['A'], label="Line")
ax.legend()
st.pyplot(fig)

# Layout
col1, col2 = st.columns(2)
col1.write("Column 1")
col2.write("Column 2")

# Sidebar
st.sidebar.header("Sidebar")
st.sidebar.selectbox("Sidebar select:", ['Option 1', 'Option 2'])

# State
st.write("State Management Example")

# Simulating a counter state
st.write("Counter Example")
counter = 0  # Placeholder for a counter
st.write(f"Counter: {counter}")

# Simulating session state for more advanced use cases
st.write("Session State Example")
st.write("Session state can maintain data across interactions.")
st.write("Example: User input, preferences, or progress in a form.")

# Control Flow
st.write("Control Flow Elements")

# Spinner
st.write("Spinner Example")
with st.spinner("Loading..."):
    st.write("This message is displayed while loading.")

# Stop execution example (streamlit stops execution after this)
st.write("Execution will stop after the next statement.")
# st.stop()  # Uncomment to stop execution at this point

# Display success message
st.success("Operation Successful")

# Display error message
st.error("An error occurred.")

# Display warning message
st.warning("This is a warning.")

# Display info message
st.info("This is an informational message.")


# Other
st.write("Other Streamlit Features")

# Display an exception message
st.write("Exception Handling Example")
try:
    raise RuntimeError("This is an example exception.")
except RuntimeError as e:
    st.exception(e)

# Display a balloon animation
st.write("Balloon Animation Example")
st.balloons()

# Display a notification toast
st.write("Notification Toast Example")
st.toast("This is a notification toast!")
