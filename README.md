### 🖼️ Capture Server

Server designed for the storage and sharing of screenshots. The primary means of communication between users and the server is conducted via WebSocket, fostering an efficient communication environment.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Socket.io](https://img.shields.io/badge/Socket.io-25c2a20?style=for-the-badge&logo=socket.io&badgeColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### 🛠️ Installation and Configuration

The system was developed using **Python 3.12**, and it is recommended to use this version to ensure compatibility.

#### 1️⃣ Clone Repository

You will need to obtain a local copy of the source code, which can be done with the following command:

```bash
git clone https://github.com/davidsantana06/capture-server
```

#### 2️⃣ Configure Environment

Once you have the files, create a `.env` file based on the template provided in `.env.example`, and specify the `ALLOWED_HOSTS` field as a space-separated list of addresses or domains that are allowed to make requests to the server.

#### 3️⃣ Install Dependencies

Next, install the application dependencies using the following command:

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run

Finally, start the server with:

```bash
flask --app app run
```

### 💻 Client

The client can be integrated by following the configuration instructions available in the [**🔗 Images Folder - Client**](https://github.com/DiovanaS/images-folder/tree/main/client).

### ⚖️ License

This project adopts the **MIT License**, which allows you to use and make modifications to the code as you wish. The only thing I ask is that proper credit is given, acknowledging the effort and time I invested in building it.
