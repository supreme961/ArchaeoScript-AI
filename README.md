# ArchaeoScript AI: A Computational Pattern Recognition and Epigraphical Analysis Platform for Ancient Inscriptions

<p align="center">
  <img src="https://img.shields.io/badge/Project-Final%20Year%20Capstone-blueviolet" alt="Final Year Capstone" />
  <img src="https://img.shields.io/badge/Domain-Digital%20Humanities%20%26%20AI-green" alt="Domain" />
  <img src="https://img.shields.io/badge/Focus-Epigraphy%20%2B%20Computer%20Vision-orange" alt="Focus" />
</p>

## 1. Project Title & Abstract

### Project Title
ArchaeoScript AI: A Computational Pattern Recognition and Epigraphical Analysis Platform for Ancient Inscriptions

### Abstract
ArchaeoScript AI is a final-year B.Tech Computer Science capstone project focused on the computational interpretation of ancient inscriptions and historical writing systems. The system is designed to support researchers, archaeologists, historians, and digital humanities scholars by combining artificial intelligence, computer vision, and epigraphic analysis in a unified platform. The project addresses a critical challenge in heritage studies: the automated recognition and comparison of both undeciphered and deciphered scripts, many of which remain fragmented, degraded, or partially preserved in archaeological artifacts.

The platform implements a dual-engine architecture to process inscriptions in two complementary ways:

- Engine A: Undeciphered Script Analysis
  - Designed for historically uncertain or partially deciphered scripts such as Indus Valley inscriptions.
  - Uses symbol segmentation via YOLOv8 to detect individual glyph-like structures from noisy inscription images.
  - Extracts deep feature vectors using ResNet50 to capture visual patterns and morphological similarities.
  - Performs fast vector retrieval and corpus matching using FAISS similarity search.
  - Applies N-gram conditional statistical analysis to model visual and positional patterns and infer likely script relationships.

- Engine B: Deciphered Script Recognition and Translation
  - Designed for known scripts such as Brahmi and related historical writing systems.
  - Uses OCR, normalization, and transliteration workflows to recognize characters and textual sequences.
  - Supports translation into modern English for better interpretability and research usability.

By integrating these two engines, the system creates a practical workflow for ancient inscription analysis, from image preprocessing and recognition to similarity-based pattern search and translation support. This makes the project academically valuable, technically relevant, and socially impactful in the preservation of historical heritage.

---

## 2. System Architecture Diagram

```text
+----------------------------------------------------------------------------------+
|                                Input Image / Inscription                          |
|  (seal, tablet, inscription plate, ancient artifact photography)                 |
+----------------------------------------------+-----------------------------------+
                                               |
                                               v
+----------------------------------------------+-----------------------------------+
| Preprocessing (OpenCV)                                                                        |
| - grayscale conversion                                                                       |
| - CLAHE contrast normalization                                                               |
| - denoising and sharpening                                                                   |
| - thresholding and artifact enhancement                                                      |
+----------------------------------------------+-----------------------------------+
                                               |
                                               v
+----------------------------------------------+-----------------------------------+
| Symbol Detection (YOLOv8)                                                                    |
| - object detection of glyphs/symbols                                                        |
| - bounding boxes and segmentation                                                           |
+----------------------------------------------+-----------------------------------+
                                               |
               +---------------------------+------------------------------------+
               |                                                           |
               v                                                           v
+----------------------------------------------+-----------------------------------+   
| Engine A: Undeciphered Script Analysis                                                  |
| - ResNet50 Feature Extraction                                                            |
| - FAISS Similarity Matching                                                              |
| - N-gram Statistical Pattern Analysis                                                    |
+----------------------------------------------+-----------------------------------+
                                               |
                                               v
+----------------------------------------------+-----------------------------------+
| Engine B: Deciphered Script Analysis                                                     |
| - OCR + Character Recognition                                                             |
| - Transliteration / OCR to text                                                           |
| - Translation into English                                                                 |
+----------------------------------------------+-----------------------------------+
                                               |
                                               v
+----------------------------------------------+-----------------------------------+
| Backend API (FastAPI)                                                                       |
| - upload endpoint                                                                            |
| - inference orchestration                                                                   |
| - model response serialization                                                               |
+----------------------------------------------+-----------------------------------+
                                               |
                                               v
+----------------------------------------------+-----------------------------------+
| User Interface (Streamlit)                                                                  |
| - image upload + visualization                                                              |
| - detection results + matches                                                              |
| - OCR output + translated text                                                             |
+----------------------------------------------------------------------------------+
```

---

## 3. Key Features & Modules

### 3.1 Preprocessing & Artifact Enhancement
The preprocessing pipeline is built to clean and standardize raw inscription imagery before model inference. This stage is crucial for historical documents that are often degraded, low-contrast, noisy, or affected by erosion and uneven lighting.

Key techniques include:
- Contrast Limited Adaptive Histogram Equalization (CLAHE)
- Grayscale conversion and normalization
- Noise reduction and blur suppression
- Binarization and threshold handling
- Edge enhancement and artifact correction using OpenCV

### 3.2 Symbol Segmentation & Bounding Box Detection
The system detects discrete visual units or glyph-like components from inscription images.

Features include:
- YOLOv8-based bounding box generation
- Glyph-level region extraction
- Detection of repeated motifs and sign clusters
- Symbol segmentation for undeciphered script analysis

### 3.3 Vector Embedding & Corpus Matching
For undeciphered scripts, the system compares extracted visual entities against a standardized catalog of reference sign patterns.

Components include:
- ResNet50 feature extraction for visual embeddings
- FAISS vector database for fast similarity lookup
- Matching against curated archaeological corpora and symbol catalogs
- Retrieval of nearest visual neighbors for interpretation support

### 3.4 Statistical Syntax & Spatial Co-occurrence Engine
A crucial component of the project is the statistical modeling of sign arrangements and spatial relationships. Historical scripts frequently display recurring motifs, sign orderings, and positional distributions that are informative even when direct decipherment remains uncertain.

This module includes:
- N-gram conditional pattern analysis
- Co-occurrence statistics across symbol sequences
- Spatial frequency modeling of glyph arrangement
- Support for candidate script family clustering and expert review

### 3.5 Dual-Engine OCR & Transliteration Module
The system supports deciphered scripts through a complementary OCR and transliteration workflow.

This module handles:
- OCR on inscriptions written in recognized scripts such as Brahmi
- Character recognition and normalization
- Transliteration into a readable intermediate representation
- Text translation into modern English
- Integration with scholarly interpretation workflows

---

## 4. Tech Stack & System Requirements

### 4.1 Technology Stack
The project is built using a robust and modern AI-driven stack suitable for academic research, experimentation, and deployment.

#### Core Technologies
- Python 3.10+
- PyTorch
- OpenCV
- Ultralytics YOLOv8
- FAISS
- FastAPI
- Streamlit
- PostgreSQL

#### Supporting Libraries
- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn
- PIL / Pillow
- SQLAlchemy
- Python-dotenv
- Docker (for deployment packaging)

### 4.2 Hardware Requirements
- Minimum RAM: 16 GB
- Recommended RAM: 32 GB for model training and processing
- GPU: CUDA-enabled NVIDIA GPU recommended
- Suggested GPU: NVIDIA RTX 3050 or equivalent
- Storage: 50 GB or more free SSD storage
- CPU: Modern multi-core processor for preprocessing and ML workloads

### 4.3 Software & Environment Requirements
- Operating System: Windows 11 / Linux / Ubuntu 20.04+
- IDE: VS Code
- Python Version: 3.10+
- Virtual Environment: venv / conda
- PostgreSQL Database
- Git and GitHub for version control
- CUDA-enabled PyTorch for GPU acceleration

---

## 5. 20-Day Agile Daily Sprint Plan (4 Weeks, 5 Working Days/Week)

The project was planned and executed in a structured 20-day sprint model to support end-to-end development from dataset preparation to final deployment.

### Week 1: Environment Setup, Dataset Curation & Preprocessing Pipeline (Days 1–5)

#### Day 1: Repository Setup and Environment Initialization
- Initialize Git repository
- Create project structure and core directories
- Set up Python virtual environment
- Install base dependencies and verify environment

#### Day 2: Dataset Collection and Directory Structuring
- Gather inscription datasets from digital archives and public corpora
- Organize datasets into training, validation, and test folders
- curate reference corpora such as Mahadevan Concordance and Parpola Corpus
- Prepare Brahmi script OCR and transliteration datasets

#### Day 3: OpenCV Preprocessing Pipeline Development
- Write image preprocessing scripts using OpenCV
- Implement CLAHE and contrast normalization
- Prepare standardized image resizing and orientation scripts

#### Day 4: Binarization, Noise Reduction & Artifact Handling
- Build scripts for denoising, sharpening, thresholding, and edge enhancement
- Remove background noise from degraded inscription images
- Create helper functions for artifact cleanup

#### Day 5: Batch Automation & Preprocessing Validation
- Build automated batch processing for large image directories
- Validate output consistency across transformed images
- Check preprocessing quality using sample visual inspection

### Week 2: Model Architecture, Bounding Box Annotation & Training (Days 6–10)

#### Day 6: Annotation Setup and Labeling Workflow
- Configure LabelImg / Roboflow-based annotation workflow
- Create bounding box labels for script symbols and glyphs
- Standardize dataset labeling for YOLOv8 compatibility

#### Day 7: YOLOv8 Dataset Configuration
- Prepare dataset YAML files
- Configure training, validation, and testing splits
- Build training pipeline structure for glyph detection

#### Day 8: YOLOv8 Training Execution
- Train YOLOv8 for symbol and motif detection
- Evaluate detection metrics and refine dataset quality
- Save trained model checkpoints

#### Day 9: ResNet50 Feature Extraction Module
- Build feature extractor pipeline using ResNet50
- Generate embeddings for detected glyph images
- Prepare feature vectors for similarity comparison

#### Day 10: FAISS Integration for Similarity Retrieval
- Build FAISS index for corpus search
- Integrate nearest-neighbor matching for historical symbol similarity
- Validate retrieval quality across sample datasets

### Week 3: Backend API & Frontend UI Development (Days 11–15)

#### Day 11: FastAPI Backend Setup
- Create backend project structure
- Set up API routes and Pydantic models
- Add image upload endpoint for inscription analysis

#### Day 12: YOLOv8 and OpenCV Inference inside API
- Connect preprocessing and detection pipeline with FastAPI
- Add inference orchestration for uploaded images
- Return detection metadata and processed results

#### Day 13: ResNet50 + FAISS Search Integration
- Integrate feature extraction with FAISS retrieval
- Return similar pattern matches to the client
- Add result serialization for UI display

#### Day 14: Streamlit Frontend Setup
- Build the user interface for image upload and analysis
- Display input image, detected symbols, and similarity matches
- Add research-friendly result cards and output visualization

#### Day 15: Frontend-Backend Connectivity
- Connect Streamlit frontend with FastAPI API
- Handle HTTP requests, output rendering, and status updates
- Validate the complete user workflow end-to-end

### Week 4: Testing, Integration, Refinement & Deployment (Days 16–20)

#### Day 16: Engine B OCR & Transliteration Integration
- Add OCR pipeline for deciphered scripts such as Brahmi
- Create transliteration and text extraction logic
- Integrate recognized text with translation support

#### Day 17: End-to-End Integration Testing
- Validate complete pipeline from image upload to output generation
- Test low-quality images, noisy artifacts, and edge cases
- Improve detection and OCR accuracy under varied conditions

#### Day 18: Code Cleanup, Logging & Unit Tests
- Improve modularity and maintainability
- Add logging and error handling
- Implement unit tests for preprocessing and matching modules

#### Day 19: Containerization and Deployment Packaging
- Create Dockerfile and docker-compose setup
- Package backend and frontend services
- Prepare deployment-ready configuration files

#### Day 20: Final Deployment & Documentation
- Deploy on Hugging Face Spaces / Streamlit Community Cloud or similar platform
- Finalize the README and project documentation
- Validate that the app is accessible and stable in a live environment

---

## 6. Project Directory Layout

```text
ArchaeoScript-AI/
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── LICENSE
├──
├── data/
│   ├── raw/
│   │   ├── inscriptions/
│   │   ├── scans/
│   │   └── reference_corpus/
│   ├── processed/
│   │   ├── enhanced/
│   │   ├── thresholded/
│   │   └── segmented/
│   ├── labels/
│   │   ├── annotations/
│   │   └── yolo_dataset/
│   └── corpus/
│       ├── indus/
│       ├── brahmi/
│       └── metadata/
├── src/
│   ├── preprocessing/
│   │   ├── enhance_images.py
│   │   ├── binarize.py
│   │   ├── denoise.py
│   │   └── segmentation.py
│   ├── models/
│   │   ├── yolov8_detector.py
│   │   ├── resnet_feature_extractor.py
│   │   ├── faiss_search.py
│   │   ├── ngram_analyzer.py
│   │   └── ocr_pipeline.py
│   ├── utils/
│   │   ├── file_handlers.py
│   │   ├── config.py
│   │   └── logger.py
│   └── pipeline/
│       ├── inference_pipeline.py
│       └── orchestrator.py
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── core/
│   └── tests/
├── frontend/
│   ├── app.py
│   ├── pages/
│   ├── components/
│   └── assets/
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   ├── training_pipeline.ipynb
│   └── evaluation_metrics.ipynb
├── tests/
│   ├── test_preprocessing.py
│   ├── test_inference.py
│   ├── test_api.py
│   └── test_ocr.py
├── docs/
│   ├── architecture.md
│   ├── dataset.md
│   └── deployment.md
└── deployment/
    ├── nginx/
    └── scripts/
```

---

## 7. Installation & Local Execution Steps

### 7.1 Clone the Repository
```bash
git clone https://github.com/your-username/ArchaeoScript-AI.git
cd ArchaeoScript-AI
```

### 7.2 Create a Virtual Environment
```bash
python -m venv venv
```

Activate the environment:

#### Windows PowerShell
```powershell
venv\Scripts\Activate.ps1
```

#### Windows Command Prompt
```cmd
venv\Scripts\activate.bat
```

#### Linux / macOS
```bash
source venv/bin/activate
```

### 7.3 Install Project Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 7.4 Configure Environment Variables
Create a `.env` file or set environment variables for the database and app settings.

Example:
```bash
DATABASE_URL=postgresql://postgres:password@localhost:5432/archaeoscript
APP_ENV=development
```

### 7.5 Run the FastAPI Backend
```bash
cd backend/app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend API will be available at:
- http://localhost:8000
- API docs: http://localhost:8000/docs

### 7.6 Run the Streamlit Frontend
```bash
cd frontend
streamlit run app.py
```

The frontend interface will be available at:
- http://localhost:8501

### 7.7 Optional: Docker Deployment
```bash
docker-compose up --build
```

---

## 8. Future Scope & Enhancements

The project lays the foundation for a broader research platform in computational epigraphy and historical AI. Several enhancements can be explored in future iterations:

- Interactive web-canvas annotation tools for scholars
- Semi-automated manual verification interfaces for expert curation
- Multi-modal transformer models integrating image, text, and metadata understanding
- Expansion to additional undeciphered scripts such as Linear A and Rongorongo
- Improved multilingual transliteration pipelines for South Asian, Near Eastern, and Mediterranean inscriptions
- Integration with larger archaeological knowledge graphs and historical linguistic databases
- Real-time comparative analysis against global script corpora

These future directions would significantly improve the platform’s usefulness as both a research tool and a public-facing cultural heritage analytics system.

---

## 9. License & Acknowledgments

### License
This project is licensed under the MIT License. It is intended for academic, educational, and research-oriented use.

### Acknowledgments
We acknowledge the foundational contributions of public epigraphical and archaeological research communities, including:
- Mahadevan Concordance
- Parpola Corpus
- Historical script archives and open research repositories

These datasets and scholarly resources provide essential reference material for inscription analysis, pattern recognition, and script comparison.

---

## Project Summary

ArchaeoScript AI is a research-oriented and technically ambitious final-year capstone project that combines deep learning, computer vision, and script analysis to study ancient inscriptions with computational precision. The project demonstrates how AI can support historical interpretation by bridging undeciphered script recognition and deciphered text translation in a single practical platform.

The system not only addresses a challenging technical problem but also contributes to the digital preservation of cultural heritage, the advancement of interdisciplinary AI research, and the growing role of machine intelligence in humanities and epigraphy.

---

## Authors / Academic Credits Placeholder

- Student Author: [Your Full Name]
- Degree: B.Tech in Computer Science and Engineering
- Institution: [Your University / College Name]
- Batch: [2024–2028 or applicable batch]
- Project Guide: [Guide Name]
- Department: Computer Science and Engineering
- Domain: Artificial Intelligence, Computer Vision, Digital Humanities, Epigraphy

---

## Contact

For inquiries, collaboration, or academic discussion, please contact:

- Email: [your.email@example.com]
- GitHub: [your-github-username]
- LinkedIn: [your-linkedin-profile]

---

This repository serves as a professional academic showcase for our final-year B.Tech Computer Science capstone project in AI-driven historical script analysis and computational epigraphy.
