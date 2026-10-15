import streamlit as st

from pdf_service import extract_text_from_pdf
from ai_service import ask_gemini


st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄"
)

st.title("📄 AI Document Assistant")

st.write(
    "Upload a PDF and ask questions about its content."
)

uploaded_file = st.file_uploader(
    "Choose a PDF document",
    type=["pdf"]
)

question = st.text_input(
    "Ask a question about your document"
)


# Step 1: Extract text from the uploaded PDF
if uploaded_file is not None:

    file_key = f"{uploaded_file.name}:{uploaded_file.size}"

    st.write("Uploaded file:", uploaded_file.name)

    if st.button("Extract PDF Text"):

        try:
            pdf_bytes = uploaded_file.getvalue()

            extracted_text, page_count = (
                extract_text_from_pdf(pdf_bytes)
            )

            st.session_state["pdf_key"] = file_key
            st.session_state["pdf_text"] = extracted_text
            st.session_state["page_count"] = page_count

            # Clear any answer from the previous document
            st.session_state.pop("ai_answer", None)
            st.session_state.pop("answer_question", None)

        except Exception:
            st.error(
                "Unable to read this PDF. "
                "Please try another PDF file."
            )


# Step 2: Display extracted text and ask Gemini
if (
    uploaded_file is not None
    and st.session_state.get("pdf_key")
    == f"{uploaded_file.name}:{uploaded_file.size}"
    and "pdf_text" in st.session_state
):

    extracted_text = st.session_state["pdf_text"]

    if extracted_text.strip():

        st.success(
            f"PDF text extracted from "
            f"{st.session_state['page_count']} pages."
        )

        with st.expander("Preview extracted text"):

            st.text_area(
                "Extracted text",
                value=extracted_text[:5000],
                height=250,
                disabled=True
            )

        if st.button("Ask Gemini"):

            if not question.strip():
                st.warning("Please enter a question.")

            else:
                try:
                    with st.spinner("Gemini is thinking..."):

                        answer = ask_gemini(
                            question,
                            extracted_text
                        )

                    st.session_state["ai_answer"] = answer
                    st.session_state["answer_question"] = question
                    st.session_state["answer_pdf_key"] = (
                        st.session_state["pdf_key"]
                    )

                except Exception as error:
                    st.error(
                        "Unable to get an AI response. "
                        "Check your API key, internet connection, "
                        "and the technical details below."
                    )
                    st.caption(str(error))

        # Keep the last answer visible when the page reruns
        if (
            st.session_state.get("answer_pdf_key")
            == st.session_state.get("pdf_key")
            and st.session_state.get("answer_question")
            == question
            and st.session_state.get("ai_answer")
        ):
            st.subheader("AI Answer")
            st.write(st.session_state["ai_answer"])

    else:
        st.warning(
            "No selectable text was found in this PDF. "
            "It may be a scanned document."
        )