# Flask Toy project _ my little memo

## Project Introduction

This project is a adorable web application using the Flask framework and MongoDB. Users can create new memo by entering a title and content, view a list of existing posts, and perform actions such as editing, deleting, and liking posts.
0.0.1 : deployment task has not completed. there is no login function using session.

## Key Features

* **Create New Memo:** Save new posts with a title and content to the database.
* **Post Listing:** Display a list of posts retrieved from the database, ordered by the latest creation date.
* **Edit Memo:** Modify the title and content of existing posts (in-place editing on the same page).
* **Delete Memo:** Remove existing posts from the database.
* **Like:** Indicate a like for each post.

## Tech Stack

* **Framework:** Flask(Python)
* **Database:** MongoDB
* **Frontend:** HTML, CSS, JavaScript
* Bootstrap 4

## Installation and Execution

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Sunhokim2/FlaskToy_memo.git
    ```

2.  **Set up a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate  # Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (Note: If you don't have a `requirements.txt` file yet, create one by running: `pip freeze > requirements.txt`)

4.  **Run MongoDB:** Ensure that your MongoDB server is running.

5.  **Run the Flask Application:**

    ```bash
    python app.py
    ```

6.  **Access in Web Browser:** Open your web browser and navigate to `http://127.0.0.1:5000/` to use the website.

## Usage

* Use the form at the top of the main page to write a new post and click the "저장하기" (Save) button.
* In the list of posts, click the "수정" (Edit), "삭제" (Delete), or "좋아요" (Like) buttons below each post to perform the corresponding action. Clicking "수정" (Edit) will transform the post content into an editable form; after making changes, click the "저장" (Save) button to update.

## Future Enhancements (Planned)

* 
