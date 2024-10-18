# PDF_QA

## 專案簡介

這是一個基於 Python 的 PDF 問答應用程式，使用 Gradio 建立使用者界面，並結合了多個自然語言處理工具來處理 PDF 文件、生成摘要，以及回答相關問題。

## 功能特點

- PDF 文件上傳和處理
- 自動生成 PDF 內容摘要
- 基於 PDF 內容的問答功能
- 使用 Gradio 構建的直觀用戶界面

## 安裝

1. 克隆此專案到本機：

   ```bash
    git clone https://github.com/EddieSHW/pdf_qa.git
    cd pdf_qa
   ```

2. 安裝所需的依賴套件：

   ```bash
    pip3 install -r requirements.txt
   ```

注意：本專案使用 Ollama 作為語言模型，請確保已在系統中安裝並執行 Ollama。

## 使用方法

執行應用程式：

```bash
    python3 pdf_qa_app.py
```

應用程式啟動後，使用瀏覽器開啟 `http://localhost:7860`

1. 在"PDF 讀取"標籤頁上傳 PDF 文件並處理。
2. 切換到"摘要"標籤頁查看生成的 PDF 摘要。
3. 在"問答"標籤頁輸入問題並獲取回答。

## 使用套件

- Gradio：用於創建 Web 界面
- Langchain：用於處理文檔、創建向量存儲和執行問答任務
- Ollama：作為底層語言模型
- PyPDFLoader：用於讀取 PDF 文件
- FAISS：用於高效的向量搜索

## 配置

如需調整，可以修改以下參數：

- `chunk_size`：在 `CharacterTextSplitter` 中調整文本分割大小
- Ollama 模型：可以在 `llm = Ollama(model="llama3.2")` 中更改模型名稱
