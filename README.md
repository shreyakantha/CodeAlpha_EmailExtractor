# 📧 Email Extraction Automation
This project focuses on automating a common real-life repetitive task using Python. The script extracts all valid email addresses from a plain text (.txt) file and saves them into a separate output file. Manually scanning large text files for email addresses is inefficient and error-prone. This automation simplifies the process using Python’s file handling and regular expressions, making it suitable for processing documents, logs, or exported data.

## 🎯 Goal
Automate the extraction of email addresses from a text file and store them in a separate file (e.g., .txt, .csv, .log etc.) for easy reuse.

## ⭐ Features
- Reads data from a .txt file
- Extracts valid email addresses using regular expressions
- Removes duplicate email entries automatically
- Saves extracted emails into a separate output file
- Simple and beginner-friendly Python script
- Includes basic error handling

## 🧠 Key Concepts Used
- File Handling
- Regular Expressions (re)
- Sets for duplicate removal
- Basic Python scripting

## 🛠 Tech Stack
**Language :** Python

**Libraries Used :** re (Regular Expressions)

## 📂 Project Structure
```Bash
CodeAlpha_EmailExtractor/
│
├── EmailExtractor.py     # Main Python script
├── input.txt             # Input text file (user-provided data)
├── README.md             # Project documentation
```
## 📥 Installation
Clone the repository using Git :
```Bash
  git clone https://github.com/shreyakantha/CodeAlpha_EmailExtractor
cd CodeAlpha_EmailExtractor
```
    
## 🖥 Run Locally
Navigate to the location of your file :
```bash
  cd CodeAlpha_EmailExtractor
```
Run the script :
```bash
 python EmailExtractor.py
```

## 🎥 Demo
*A video demonstration showing the complete working of the Email Extraction Automation script. The video covers the Python source code, the input text file containing sample email addresses, execution of the script, and the automatically generated output file with all extracted unique emails.*

[ ▶ click here to view the demo video of the email extraction automation ](https://github.com/shreyakantha/CodeAlpha_EmailExtractor/releases/tag/v1.0)

## 📝  Usage/Example
The example below shows how the script reads a text file containing email addresses and extracts all valid entries into a separate output file.
**Example input.txt**
```bash
[2025-01-12 11:02:15] INFO: Internship application submitted
Applicant Name: Shreya
Applicant Email: shreyakantha@gmail.com

[2025-01-12 11:05:42] INFO: Application forwarded to review team
Reviewer Email: reviewer@codealpha.tech

[2025-01-12 11:20:10] INFO: Confirmation email sent
Recipient: shreya.student@gmail.com

[2025-01-12 11:45:33] INFO: Technical task assigned
Coordinator Email: internships@codealpha.tech

[2025-01-12 12:10:27] INFO: Support ticket created
Contact Email: support@codealpha.tech
```
**Output (emails.log – generated automatically)**
```bash
internships@codealpha.tech
reviewer@codealpha.tech
shreya.student@gmail.com
shreyakantha@gmail.com
support@codealpha.tech
```
## 🚀 Deployment
This is a local Python script and does not require deployment. It can be executed on any system with Python installed.

## ⚙ Optimizations
- Uses a set to remove duplicate emails efficiently
- Can be optimized further by reading large files line-by-line instead of loading the entire file at once

## 📚 Lessons Learned
- Working with regular expressions for pattern matching
- Handling files safely using Python
- Automating repetitive tasks using simple scripts
- Structuring small automation projects professionally

## 🔮 Future Improvements
- Support reading large files line-by-line
- Export results in CSV or JSON format
- Improve regex for advanced email patterns
- Add command-line arguments for file names

## 📄 Documentation
The project follows a simple and readable structure. The script is short and self-explanatory, with clear function naming and logical flow. Detailed usage instructions and examples are provided in this README.

## 👤 Author
- [@shreyakantha](https://github.com/shreyakantha) 

## 🙌 Acknowledgements
- CodeAlpha Internship Program for providing the task and learning opportunity
- Python official documentation for file handling and regular expressions
- Online regex learning resources for understanding pattern matching
- Open-source README formatting guidelines

## 📜 License
This project is open for educational and personal use. Feel free to modify, improve, and expand it as needed.

## 💬 Feedback
If you have any feedback or suggestions, feel free to reach out at 📧 shreyakantha348@gmail.com

## ❓ FAQ
#### Q1. Does this script generate email addresses?
**Answer.** No. It only extracts existing email addresses from a .txt file.
#### Q2. What happens if the input.txt file has no emails?
**Answer.** The output file will be empty.
#### Q3. Where is the output file saved?
**Answer.** In the same directory where the script is executed.

## 🧩 Appendix
This project was completed as ***The third task which is Task Automation with Python Scripts*** under the **CodeAlpha Python Programming Internship**, where the ***Email Extraction Automation*** topic was selected for implementation.

## 📌 Related Projects
*The following projects were completed as part of the same **CodeAlpha internship** program and focus on strengthening core Python programming concepts.*
-  🔗 [Hangman Game – Python fundamentals and control flow](https://github.com/shreyakantha/CodeAlpha_HangmanGame)
-  🔗 [Stock Portfolio Tracker – Data processing using Python](https://github.com/shreyakantha/CodeAlpha_StockPortfolioTracker)
-  🔗 [Basic Chatbot – Rule-based conversation using conditional logic](https://github.com/shreyakantha/CodeAlpha_BasicChatbot)
