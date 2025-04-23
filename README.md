---

## 🚀 Features

- 🧾 Create tasks and store them in a MongoDB database
- 👀 View your task list
- ❌ Delete tasks by ID
- 🔁 Update tasks with new descriptions
- 🖥️ Interactive CLI menu for ease of use

---

## 💠 Tech Stack

| Technology                                                                 | Description           |
|---------------------------------------------------------------------------|-----------------------|
| ![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)       | Programming Language  |
| ![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen?logo=mongodb) | NoSQL Database        |
| ![PyMongo](https://img.shields.io/badge/PyMongo-Client-orange?logo=python) | Python MongoDB Driver |

---


## 📆 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/mongodb-cli-todo.git
cd mongodb-cli-todo

# Install dependencies
pip install pymongo
```

---

## ⚙️ Setup

1. Ensure MongoDB is installed and running locally:
   ```bash
   mongod
   ```
2. Modify the connection string in the script if your MongoDB isn't hosted locally:
   ```python
   uri = "mongodb://localhost:27017/"
   ```

---

## 🧹 Usage

```bash
python todo.py
```

You'll see a simple interactive menu:

```
1. Create Task
2. View Tasks
3. Delete Task
4. Update Task
5. Exit
```

---

## 📸 Demo

![CLI Demo](./Screenshot%202025-04-23%20162739.png)

---

## 📂 Project Structure

```
📁 mongodb-cli-todo
│
├── todo.py           # Main script with all operations
├── README.md         # Documentation
└── requirements.txt  # Python dependencies
```

---

## 🙌 Author

**Chethan Nazre S**\
🔗 [GitHub](https://github.com/chethannazres) | 💼 [LinkedIn](https://linkedin.com/in/chethannazre)

---

## 📄 License

This project is licensed under the MIT License.

---

