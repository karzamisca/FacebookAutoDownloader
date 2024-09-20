# Warning: USE BURNER ACCOUNT ONLY, USE MAIN ACCOUNT AT YOUR OWN RISK 

# Facebook Auto-Poster

This application automates the process of posting text content to Facebook using user-provided credentials and text files stored in a selected folder.

## Classes

### `FacebookPosterApp`
The main application class that creates the user interface and handles interactions.

#### Methods:
- **`__init__(self)`**
  - Initializes the UI and sets up the initial state of the application.

- **`init_ui(self)`**
  - Configures the layout and widgets for the user interface, including input fields for username and password, a button for selecting a folder, and a button to start posting.

- **`select_folder(self)`**
  - Opens a dialog for the user to select a folder containing text files. Updates the UI to display the selected folder path.

- **`post_to_facebook(self, email, password)`**
  - Automates the login to Facebook and posts text content read from text files in the selected folder.
  - **Parameters:**
    - `email`: The user's Facebook email or username.
    - `password`: The user's Facebook password.

- **`start_posting(self)`**
  - Validates user inputs and initiates the posting process by calling `post_to_facebook`.

## Usage Instructions

1. **Install Dependencies**:
   Make sure you have the required libraries installed:
   ```bash
   pip install playwright PyQt6
   playwright install
   ```

2. **Run the Application**:
   Execute the script to launch the UI:
   ```bash
   python main.py
   ```

3. **Fill in Credentials**:
   - Enter your Facebook username or email.
   - Enter your Facebook password.

4. **Select Folder**:
   - Click on "Select Folder for Post Text" to choose a folder containing `.txt` files that include the text you want to post.

5. **Start Posting**:
   - Click on "Start Posting" to begin the posting process.

6. (Optional) **Compilation**:
   - Use
   ```bash 
   pyinstaller -D main.py
   ``` 
   in the directory

## Notes
- Ensure that the text files in the selected folder have the `.txt` extension.
- The application will attempt to post the content of each text file in the order they are found in the folder.

---
