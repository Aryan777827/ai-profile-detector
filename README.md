

\# 🕵️ AI Profile Detector



A machine learning-powered web application that analyzes profile images and metadata to determine the likelihood of AI-generated identities.



---



\## 📌 Overview



The \*\*AI Profile Detector\*\* is designed to identify synthetic or AI-generated profile images by combining multiple model predictions with heuristic-based metadata analysis.



The system produces a unified \*\*suspicion score (0–100)\*\* along with interpretable insights, making it useful for early-stage fraud detection, moderation systems, and research experimentation.



---



\## ✨ Key Features



\* \*\*Multi-model ensemble detection\*\*



&nbsp; \* Aggregates predictions from multiple AI detection models

\* \*\*Confidence scoring system\*\*



&nbsp; \* Provides calibrated probability and confidence levels

\* \*\*Metadata-based heuristics\*\*



&nbsp; \* Evaluates behavioral signals (followers, posts, account age, etc.)

\* \*\*Explainable output\*\*



&nbsp; \* Transparent breakdown of model decisions

\* \*\*Interactive UI\*\*



&nbsp; \* Built with Streamlit for rapid testing and demonstration



---



\## 🧠 System Architecture



```

Input (Image + Metadata)

&nbsp;       ↓

Image Analysis (Ensemble Models)

&nbsp;       ↓

Metadata Heuristics Engine

&nbsp;       ↓

Weighted Scoring System

&nbsp;       ↓

Final Suspicion Score + Verdict

```



---



\## 📊 Scoring Logic



\* \*\*60% Image Analysis\*\*

\* \*\*40% Metadata Analysis\*\*



The final score is normalized on a scale of \*\*0–100\*\*, categorized as:



| Score Range | Risk Level    |

| ----------- | ------------- |

| 0 – 39      | Low Risk      |

| 40 – 64     | Moderate Risk |

| 65 – 100    | High Risk     |



---



\## 🛠️ Tech Stack



| Layer            | Technology                     |

| ---------------- | ------------------------------ |

| Frontend         | Streamlit                      |

| Backend          | Python                         |

| Image Processing | PIL                            |

| Networking       | Requests                       |

| ML Models        | Hugging Face / Custom Ensemble |



---



\## 🚀 Getting Started



\### 1. Clone the repository



```bash

git clone https://github.com/Aryan777827/ai-profile-detector.git

cd ai-profile-detector

```



\### 2. Setup environment



```bash

python -m venv venv

venv\\Scripts\\activate   # Windows

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the application



```bash

streamlit run app.py

```



---



\## 📸 Usage



1\. Upload a profile image or provide an image URL

2\. (Optional) Enter profile metadata

3\. Click \*\*Analyze Profile\*\*

4\. Review:



&nbsp;  \* AI probability

&nbsp;  \* Confidence level

&nbsp;  \* Model breakdown

&nbsp;  \* Suspicion score



---



\## ⚠️ Limitations



\* AI detection models are not fully reliable and may produce false positives/negatives

\* Performance depends on image quality and input data

\* Not suitable for production-grade moderation without further validation



---



\## 🔮 Future Enhancements



\* Improved ensemble weighting strategies

\* Facial symmetry \& landmark-based analysis

\* GAN artifact detection improvements

\* REST API for external integration

\* Real-time social media profile scanning



---



\## 📂 Project Structure



```

ai-profile-detector/

│

├── app.py

├── src/

│   └── detector.py

├── requirements.txt

└── README.md

```



---



\## 👨‍💻 Author



\*\*Aryan Sharma\*\*

GitHub: https://github.com/Aryan777827



---



\## 📄 License



This project is for educational and research purposes.



A machine learning-powered web application that analyzes profile images and metadata to determine the likelihood of AI-generated identities.



---



\## 📌 Overview



The \*\*AI Profile Detector\*\* is designed to identify synthetic or AI-generated profile images by combining multiple model predictions with heuristic-based metadata analysis.



The system produces a unified \*\*suspicion score (0–100)\*\* along with interpretable insights, making it useful for early-stage fraud detection, moderation systems, and research experimentation.



---



\## ✨ Key Features



\* \*\*Multi-model ensemble detection\*\*



&nbsp; \* Aggregates predictions from multiple AI detection models

\* \*\*Confidence scoring system\*\*



&nbsp; \* Provides calibrated probability and confidence levels

\* \*\*Metadata-based heuristics\*\*



&nbsp; \* Evaluates behavioral signals (followers, posts, account age, etc.)

\* \*\*Explainable output\*\*



&nbsp; \* Transparent breakdown of model decisions

\* \*\*Interactive UI\*\*



&nbsp; \* Built with Streamlit for rapid testing and demonstration



---



\## 🧠 System Architecture



```

Input (Image + Metadata)

&nbsp;       ↓

Image Analysis (Ensemble Models)

&nbsp;       ↓

Metadata Heuristics Engine

&nbsp;       ↓

Weighted Scoring System

&nbsp;       ↓

Final Suspicion Score + Verdict

```



---



\## 📊 Scoring Logic



\* \*\*60% Image Analysis\*\*

\* \*\*40% Metadata Analysis\*\*



The final score is normalized on a scale of \*\*0–100\*\*, categorized as:



| Score Range | Risk Level    |

| ----------- | ------------- |

| 0 – 39      | Low Risk      |

| 40 – 64     | Moderate Risk |

| 65 – 100    | High Risk     |



---



\## 🛠️ Tech Stack



| Layer            | Technology                     |

| ---------------- | ------------------------------ |

| Frontend         | Streamlit                      |

| Backend          | Python                         |

| Image Processing | PIL                            |

| Networking       | Requests                       |

| ML Models        | Hugging Face / Custom Ensemble |



---



\## 🚀 Getting Started



\### 1. Clone the repository



```bash

git clone https://github.com/Aryan777827/ai-profile-detector.git

cd ai-profile-detector

```



\### 2. Setup environment



```bash

python -m venv venv

venv\\Scripts\\activate   # Windows

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the application



```bash

streamlit run app.py

```



---



\## 📸 Usage



1\. Upload a profile image or provide an image URL

2\. (Optional) Enter profile metadata

3\. Click \*\*Analyze Profile\*\*

4\. Review:



&nbsp;  \* AI probability

&nbsp;  \* Confidence level

&nbsp;  \* Model breakdown

&nbsp;  \* Suspicion score



---



\## ⚠️ Limitations



\* AI detection models are not fully reliable and may produce false positives/negatives

\* Performance depends on image quality and input data

\* Not suitable for production-grade moderation without further validation



---



\## 🔮 Future Enhancements



\* Improved ensemble weighting strategies

\* Facial symmetry \& landmark-based analysis

\* GAN artifact detection improvements

\* REST API for external integration

\* Real-time social media profile scanning



---



\## 📂 Project Structure



```

ai-profile-detector/

│

├── app.py

├── src/

│   └── detector.py

├── requirements.txt

└── README.md

```



---



\## 👨‍💻 Author



\*\*Aryan Sharma\*\*

GitHub: https://github.com/Aryan777827



---



\## 📄 License



This project is for educational and research purposes.



