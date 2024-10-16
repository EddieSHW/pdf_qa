import gradio as gr
from langchain_community.llms import Ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from tqdm import tqdm

# 初始化Ollama model
llm = Ollama(model="llama3.2")

qa_chain = None
summary = None

def process_pdf(pdf_file):
    global qa_chain, summary
    
    # 讀取PDF
    loader = PyPDFLoader(pdf_file.name)
    documents = []
    try:
        for page in tqdm(loader.load(), desc="PDF處理中"):
            documents.append(page)
    except Exception as e:
        return f"讀取PDF時發生錯誤: {e}"

    # 分割文本
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    # embedding並儲存至vectorstore
    embeddings = OllamaEmbeddings(model="llama3.2")
    vectorstore = FAISS.from_documents(texts, embeddings)

    # 搜尋用的chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )

    # 生成概要
    summary_prompt = "請用300字詞概括PDF檔的內容"
    summary = qa_chain.run(summary_prompt)

    return "PDF處理完成。摘要已生成。"

def get_summary():
    return summary if summary else "PDF尚未處理。"

def answer_question(question):
    if qa_chain:
        return qa_chain.run(question)
    else:
        return "PDF尚未處理。"

# Gradio界面
with gr.Blocks() as app:
    gr.Markdown("# PDF QA APP")
    
    with gr.Tab("PDF讀取"):
        pdf_input = gr.File(label="上傳PDF檔")
        process_button = gr.Button("讀取PDF")
        process_output = gr.Textbox(label="處理結果")
        process_button.click(process_pdf, inputs=pdf_input, outputs=process_output)

    with gr.Tab("摘要"):
        summary_button = gr.Button("顯示摘要")
        summary_output = gr.Textbox(label="PDF摘要")
        summary_button.click(get_summary, outputs=summary_output)

    with gr.Tab("問答"):
        question_input = gr.Textbox(label="輸入問題")
        answer_button = gr.Button("取得回答")
        answer_output = gr.Textbox(label="回答")
        answer_button.click(answer_question, inputs=question_input, outputs=answer_output)


if __name__ == "__main__":
    app.launch()