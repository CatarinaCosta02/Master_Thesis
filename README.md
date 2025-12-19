# Using Vector Databases In Predictive Analysis Systems 

**Master's Dissertation in Informatics Engineering (2025)**

The growing demand for integrating AI-based systems increases complex data (images, video, and audio), and traditional databases often fall short.

Vector databases can:
* manage complex data
* integrate machine learning models

These databases, when combined with predictive analysis systems, become a powerful tool for multiple domains. In healthcare: improving diagnosis, treatment planning, and supporting hospital resource management.

The core of this work is a **Predictive Disease Diagnosis System** that transcends standard classification. While traditional models predict based on learned patterns, this system uses **vector databases similarity search to validate predictions** by cross-referencing them with historical medical data stored as embeddings.

Essentially, a **predictive disease diagnosis system that uses vector databases to improve accuracy and validate the results.**


## Technical Workflow and Architecture

The system has two main layers to ensure accuracy and reliability in healthcare diagnostics:

* **Predictive Layer:** Classification Supervised Machine Learning models trained on clinical datasets to predict potential diagnoses.
* **Validation Layer:** To make the results more reliable, every new medical case is used as a query in a FAISS vector database. The system finds the 3 most similar cases from the original data used to train the model. By comparing the model’s prediction with the real results of these 3 past cases, the system adds a validation layer. This confirms if the new diagnosis matches proven medical history.

![Systems Architecture](https://github.com/CatarinaCosta02/Master_Thesis/blob/main/Graphs/Captura%20de%20ecr%C3%A3%202025-12-19%20230459.png)

## Achievments

* Construction of three predictive models, all capable of predicting the diagnosis of diseases.
* Integration of the XGBoost model with the FAISS vector database to validate the results.
* Creation of various types of vector index to allow comparison between them.
* Application of data preprocessing techniques, including cleaning, outlier detection, missing values handling, and building a pipeline that included feature engineering and variable encoding.
* Implementation of techniques such as cross-validation to prevent overfitting.

## Key Research Objectives

* Understand similarity analysis techniques.
* Explore different similarity algorithms.
* Analyse how vector databases work and how they can be integrated with predictive analytics systems.
* Build machine learning models and apply data preprocessing techniques.
* Develop an efficient predictive diagnostic system.

## Techn Stack

* **Language:** Python
* **Machine Learning Models:** XGBoost, Random Forest, Support Vector Machine
* **Vector Database:** FAISS
* **Vector Search Indexs:** IndexFlatL2,  IndexFlatIP, IndexHNSWFlat, IndexLSH
* **AI Tools:** scikit-learn, pandas,  seaborn, matplotlib, NumPy

## Dataset

[MIMIC-IV Clinical Database Demo v2.2 (2023)](https://physionet.org/content/mimic-iv-demo/2.2/)


## Repository Structure

| Folder/File | Description |
| :--- | :--- |
| `Datasets` | Final curated used for training and testing the predictive models |
| `documents` |  MIMIC-IV Demo v2.2 clinical database files |
| `First_models` | Initial iterations and results of supervised machine learning models |
| `Graphs` | Python scripts used to generate graphs|
| `profilling` | Scripts for data profilling and pre-processing |
| `Thesis_v1` | Version 1 of the models developed |
| `Thesis_v2` | Version 2 and final of the models and system developed |

## How To Run

1. ``` git clone https://github.com/CatarinaCosta02/Master_Thesis.git```

2. Unzip all .zip files within the repository

3. ```pip install pandas scikit-learn faiss-cpu```

4. Run Jupyter Notebook on Thesis_v2 folder called ```XGBoost_Final.ipynb```

Note: This is the primary notebook of the project. It features the full integration between the XGBoost predictive model and the FAISS vector database for similarity-based validation.

## Acknowledgements

This work was supported by the **University of Minho**, in collaboration with TU Wien University.

**Supervisors:** Orlando Manuel Oliveira Belo, Katja Hose, Milos Jovanovik  
