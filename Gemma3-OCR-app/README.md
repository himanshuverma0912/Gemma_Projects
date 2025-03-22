# Gemma-3 OCR Web Application

This Streamlit web application utilizes the Gemma-3 Vision model (accessed via Ollama) to perform Optical Character Recognition (OCR) on uploaded images. It extracts readable text from images and presents it in a structured Markdown format.

## Features

* **Image Upload:** Allows users to upload images in PNG, JPG, or JPEG formats.
* **OCR Processing:** Uses the Gemma-3 Vision model to extract text from the uploaded image.
* **Structured Output:** Presents the extracted text in a clean, concise, and well-organized Markdown format.
* **Clear Results:** Displays the processed text directly in the application's main content area.
* **Clear Button:** Provides a button to clear the uploaded image and any displayed results.
* **User-friendly Interface:** Uses Streamlit to create an intuitive and easy-to-use interface.

## Prerequisites

Before running this application, ensure you have:

1.  **Python 3.7+ installed.**
2.  **Ollama installed and running with the `gemma3:12b` model pulled.** (See [Ollama documentation](https://ollama.ai/) for installation instructions.)
3.  **The following Python libraries installed:**

    ```bash
    pip install -r requirements.txt
    ```

## How to Run

1.  **Save the Python code:** Save the code as a `.py` file (e.g., `gemma3_ocr.py`).
2.  **Open a terminal:** Navigate to the directory where you saved the file.
3.  **Run the Streamlit app:**

    ```bash
    streamlit run gemma3_ocr.py
    ```

4.  **Open your browser:** Streamlit will provide a local URL (e.g., `http://localhost:8501`). Open this URL in your browser.

## How to Use

1.  **Upload an image:** In the sidebar, click "Choose an image..." and select an image file (PNG, JPG, or JPEG).
2.  **View the uploaded image:** The uploaded image will be displayed in the sidebar.
3.  **Click "Extract Text 🔍":** Click the button to send the image to the Gemma-3 Vision model for OCR processing.
4.  **View the results:** The extracted text, formatted in Markdown, will be displayed in the main content area.
5.  **Clear the results:** Click the "Clear 🗑️" button in the top right to remove the results and uploaded image.

## Code Flow Explanation

1.  **Import Libraries:** The application imports necessary libraries, including Streamlit, Ollama, Pillow, io, and base64.
2.  **Page Configuration:** The `st.set_page_config()` function sets the page title, icon, layout, and initial sidebar state.
3.  **Title and Description:** The application displays a title with an image and a brief description using `st.markdown()`.
4.  **Clear Button:** A clear button is implemented using `st.button()` and `st.session_state` to remove the OCR result and uploaded image.
5.  **Sidebar Upload:** A file uploader is created in the sidebar using `st.file_uploader()` to allow users to upload images.
6.  **Image Display:** If an image is uploaded, it is displayed in the sidebar using `st.image()`.
7.  **Extract Text Button:** An "Extract Text" button is created using `st.button()`. When clicked, the following occurs:
    * A spinner is displayed using `st.spinner()` to indicate processing.
    * The `ollama.chat()` function is called to send the image to the Gemma-3 model for OCR.
    * The model's response (extracted text) is stored in the `st.session_state['ocr_result']`.
    * Error handling is implemented using a `try...except` block to catch and display any errors during processing.
8.  **Result Display:** If `st.session_state['ocr_result']` exists, the extracted text is displayed in the main content area using `st.markdown()`. Otherwise, an info message is displayed.
9.  **Footer:** A footer message is displayed using `st.markdown()`.

## Notes

* Ensure Ollama is running and the `gemma3:12b` model is downloaded before running the application.
* The accuracy of the OCR results may vary depending on the image quality and complexity.
* Error handling is implemented to catch and display any errors during image processing.
* The application uses `st.session_state` to store the OCR result and persist it across reruns.