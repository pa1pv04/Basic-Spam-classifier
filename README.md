#  Spam Email Classifier

A simple Machine Learning and NLP project that classifies messages as **Spam** or **Ham (Not Spam)**.

This project uses **TF-IDF Vectorization** and a **Naive Bayes Classifier** to analyze text messages and predict whether they are spam.

---

##  Features

- Detects spam and non-spam messages
- Uses NLP-based text processing
- Converts text into numerical vectors using TF-IDF
- Trains a Machine Learning classification model
- Interactive terminal-based prediction system

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- NLP
- TF-IDF Vectorization
- Naive Bayes Algorithm

---

##  Project Structure

```bash
spam_email/
│
├── spam.csv
├── spam_classifier.py
```

---

##  Installation

Install the required libraries:

```bash
pip install pandas scikit-learn
```

---

##  How to Run

Run the Python file:

```bash
python spam_classifier.py
```

After running the program, enter any message in the terminal to check whether it is spam or ham.

### Example

Input:

```text
You won a free iPhone
```

Output:

```text
Prediction: spam
```

---

##  Sample Predictions

| Message | Prediction |
|---|---|
| You won a free recharge | Spam |
| Meeting tomorrow at 10 AM | Ham |
| Claim your reward now | Spam |
| Let's have lunch today | Ham |

---

##  Learning Outcomes

Through this project, I learned:

- Basics of Natural Language Processing (NLP)
- Text preprocessing techniques
- TF-IDF vectorization
- Machine Learning model training
- Spam message classification
- Working with Scikit-learn and Pandas

---

##  Future Improvements

- Build a Flask web application
- Add a larger real-world dataset
- Improve accuracy using advanced NLP models
- Deploy the project online
- Integrate embeddings and semantic analysis

---

##  Author

**Pavan Kumar**
