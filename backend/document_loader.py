"""
Document Loaders
Load and process different document types
"""
from typing import List, Dict, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentLoader:
    """Load and chunk documents."""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize document loader.
        
        Args:
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
    
    def load_text(self, file_path: str) -> List[Dict[str, Any]]:
        """Load a text file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        chunks = self.text_splitter.split_text(text)
        
        return [
            {
                "content": chunk,
                "metadata": {
                    "source": file_path,
                    "chunk_index": i,
                    "type": "text"
                }
            }
            for i, chunk in enumerate(chunks)
        ]
    
    def load_pdf(self, file_path: str) -> List[Dict[str, Any]]:
        """Load a PDF file."""
        try:
            import pypdf
            
            text = ""
            with open(file_path, 'rb') as f:
                pdf_reader = pypdf.PdfReader(f)
                for page_num, page in enumerate(pdf_reader.pages):
                    text += f"\n--- Page {page_num + 1} ---\n"
                    text += page.extract_text()
            
            chunks = self.text_splitter.split_text(text)
            
            return [
                {
                    "content": chunk,
                    "metadata": {
                        "source": file_path,
                        "chunk_index": i,
                        "type": "pdf"
                    }
                }
                for i, chunk in enumerate(chunks)
            ]
        except ImportError:
            raise ImportError("pypdf not installed. Install with: pip install pypdf")
    
    def load_docx(self, file_path: str) -> List[Dict[str, Any]]:
        """Load a Word document."""
        try:
            from docx import Document
            
            doc = Document(file_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            
            chunks = self.text_splitter.split_text(text)
            
            return [
                {
                    "content": chunk,
                    "metadata": {
                        "source": file_path,
                        "chunk_index": i,
                        "type": "docx"
                    }
                }
                for i, chunk in enumerate(chunks)
            ]
        except ImportError:
            raise ImportError("python-docx not installed. Install with: pip install python-docx")
    
    def load_html(self, file_path: str) -> List[Dict[str, Any]]:
        """Load an HTML file."""
        try:
            from bs4 import BeautifulSoup
            
            with open(file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            text = soup.get_text(separator='\n', strip=True)
            
            chunks = self.text_splitter.split_text(text)
            
            return [
                {
                    "content": chunk,
                    "metadata": {
                        "source": file_path,
                        "chunk_index": i,
                        "type": "html"
                    }
                }
                for i, chunk in enumerate(chunks)
            ]
        except ImportError:
            raise ImportError("beautifulsoup4 not installed. Install with: pip install beautifulsoup4")
    
    def load_document(self, file_path: str, doc_type: str = None) -> List[Dict[str, Any]]:
        """
        Load a document based on file type.
        
        Args:
            file_path: Path to document
            doc_type: Document type (txt, pdf, docx, html) - auto-detected if None
            
        Returns:
            List of document chunks with metadata
        """
        # Auto-detect type from extension
        if doc_type is None:
            if file_path.endswith('.pdf'):
                doc_type = 'pdf'
            elif file_path.endswith('.docx'):
                doc_type = 'docx'
            elif file_path.endswith('.html') or file_path.endswith('.htm'):
                doc_type = 'html'
            else:
                doc_type = 'text'
        
        # Load based on type
        if doc_type == 'pdf':
            return self.load_pdf(file_path)
        elif doc_type == 'docx':
            return self.load_docx(file_path)
        elif doc_type == 'html':
            return self.load_html(file_path)
        else:
            return self.load_text(file_path)
