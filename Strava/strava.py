import streamlit as st

# from dotenv import load_dotenv
# from htmlTemplates import css, bot_template, user_template


def main():

    # load_dotenv()
    answer = ""
    st.set_page_config(
        page_title="strava",
    )
    # st.write(css, unsafe_allow_html=True)
    st.header("Get Your Activity Details")
    answer_placeholder = st.empty()

    # # user_question = st.text_input("Ask a question about your documents:")
    # a = st.write("Hello new techie,")
    # if user_question:
    # handle_userinput(user_question)
    if st.button("Process"):
        st.write("Hello")
    # with st.sidebar:
    #     st.subheader("Your documents")
    #     pdf_docs = st.file_uploader(
    #         "Upload your PDFs here and click on 'Process'", accept_multiple_files=True
    #     )
    #     if st.button("Process"):
    #         with st.spinner("Processing"):
    #             # get pdf text
    #             raw_text = get_pdf_text(pdf_docs)

    #             # get the text chunks
    #             text_chunks = get_text_chunks(raw_text)

    #             # create vector store
    #             vectorstore = get_vectorstore(text_chunks)

    #             # create conversation chain
    #             answer = get_conversation_chain(vectorstore)

    #             # Ensure JSON is parsed correctly
    #             try:
    #                 answer = answer.strip("```json").strip("```")
    #                 answer = json.loads(answer)
    #             except Exception as e:
    #                 st.error(f"Error parsing JSON: {e}")
    #                 return

    #             display_invoice_details(answer, answer_placeholder)
    #             print(answer)

    # Print the resulting Python dictionary
    # # "View Tally" Button
    # if st.button("View Tally"):
    #     # Call the function
    #     result = view_tally_function()
    #     if result == "success":
    #         st.success("Tally viewed successfully!")
    #     else:
    #         st.error(f"An error occurred: {result}")


if __name__ == "__main__":
    main()
