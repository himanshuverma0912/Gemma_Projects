import streamlit as st  # Import the Streamlit library for creating web applications.
import ollama  # Import the Ollama library for interacting with local language models.
from PIL import Image  # Import the Pillow (PIL) library for image processing.
import io  # Import the io module for working with input/output streams.
import base64  # Import the base64 module for encoding/decoding data.

# Page configuration
st.set_page_config(  # Configure the Streamlit page.
    page_title="Gemma-3 OCR",  # Set the page title.
    page_icon="🔎",  # Set the page icon.
    layout="wide",  # Set the layout to wide.
    initial_sidebar_state="expanded"  # Set the initial sidebar state to expanded.
)

# Title and description in main area
st.markdown("""
    # <img src="data:image/png;base64,{}" width="50" style="vertical-align: -12px;"> Gemma-3 OCR
""".format(base64.b64encode(open("./assets/gemma3.png", "rb").read()).decode()), unsafe_allow_html=True) # Display a title with an image.

# Add clear button to top right
col1, col2 = st.columns([6,1]) # Create two columns for layout.
with col2: # Place the clear button in the second column.
    if st.button("Clear 🗑️"): # Create a clear button.
        if 'ocr_result' in st.session_state: # Check if 'ocr_result' exists in the session state.
            del st.session_state['ocr_result'] # Delete 'ocr_result' from the session state.
        st.rerun() # Rerun the Streamlit app to clear the results.

st.markdown('<p style="margin-top: -20px;">Extract structured text from images using Gemma-3 Vision!</p>', unsafe_allow_html=True) # Display a description.
st.markdown("---") # Display a horizontal line.

# Move upload controls to sidebar
with st.sidebar: # Create a sidebar for upload controls.
    st.header("Upload Image") # Display a header in the sidebar.
    uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg']) # Create a file uploader for images.
    
    if uploaded_file is not None: # Check if a file has been uploaded.
        # Display the uploaded image
        image = Image.open(uploaded_file) # Open the uploaded image.
        st.image(image, caption="Uploaded Image") # Display the uploaded image in the sidebar.
        
        if st.button("Extract Text 🔍", type="primary"): # Create an extract text button.
            with st.spinner("Processing image..."): # Display a spinner while processing.
                try:
                    response = ollama.chat( # Send the image to the Gemma-3 model for OCR.
                        model='gemma3:12b', # Specify the Gemma-3 model.
                        messages=[{ # Create a list of messages for the model.
                            'role': 'user', # Set the role to user.
                            'content': """Analyze the text in the provided image. Extract all readable content
                                            and present it in a structured Markdown format that is clear, concise, 
                                            and well-organized. Ensure proper formatting (e.g., headings, lists, or
                                            code blocks) as necessary to represent the content effectively.""", # Define the prompt for the model.
                            'images': [uploaded_file.getvalue()] # Pass the uploaded image data to the model.
                        }]
                    )
                    st.session_state['ocr_result'] = response.message.content # Store the OCR result in the session state.
                except Exception as e: # Handle any errors during processing.
                    st.error(f"Error processing image: {str(e)}") # Display an error message.

# Main content area for results
if 'ocr_result' in st.session_state: # Check if 'ocr_result' exists in the session state.
    st.markdown(st.session_state['ocr_result']) # Display the OCR result in the main area.
else:
    st.info("Upload an image and click 'Extract Text' to see the results here.") # Display an info message.

# Footer
st.markdown("---") # Display a horizontal line.
st.markdown("Made with ❤️ using Gemma-3 Vision Model") # Display a footer message.