import re


def clean_text(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    return text.strip()


from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(
    text: str,
    chunk_size: int = 1200,
    chunk_overlap: int = 200,
) -> list[str]:
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            "? ",
            "! ",
            " ",
            "",
        ],
    )

    return splitter.split_text(text)


def chunk_documents(documents: list[dict]) -> list[dict]:
    chunks = []

    for document_index, document in enumerate(documents):
        cleaned_text = clean_text(document["content"])
        text_chunks = split_text(cleaned_text)

        for chunk_index, content in enumerate(text_chunks):
            chunks.append(
                {
                    "chunk_id": f"doc_{document_index}_chunk_{chunk_index}",
                    "document_index": document_index,
                    "chunk_index": chunk_index,
                    "title": document["title"],
                    "url": document["url"],
                    "query": document["query"],
                    "content": content,
                }
            )

    return chunks