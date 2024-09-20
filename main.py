import sys
import os
import asyncio
from playwright.async_api import async_playwright
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QFileDialog,
)

class FacebookPosterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Facebook Auto-Poster")

        layout = QVBoxLayout()

        # Username field
        self.username_label = QLabel("Username or Email:")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        # Password field
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Folder selection button
        self.folder_button = QPushButton("Select Folder for Post Text")
        self.folder_button.clicked.connect(self.select_folder)
        layout.addWidget(self.folder_button)

        # Label to show the selected folder path
        self.folder_path_label = QLabel("Selected Folder: None")
        layout.addWidget(self.folder_path_label)

        # Start posting button
        self.post_button = QPushButton("Start Posting")
        self.post_button.clicked.connect(self.start_posting)
        layout.addWidget(self.post_button)

        self.setLayout(layout)
        self.post_text_folder = ""

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.post_text_folder = folder
            self.folder_path_label.setText(f"Selected Folder: {folder}")

    async def post_to_facebook(self, email, password):
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=False,
                args=[
                    '--disable-dev-shm-usage',
                    '--no-sandbox'
                ]
            )
            context = await browser.new_context(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.73 Safari/537.36'
            )
            context.set_default_timeout(100000)
            page = await context.new_page()
            await page.goto('https://www.facebook.com')

            # Fill in the login form
            await page.fill('input[name="email"]', email)
            await page.fill('input[name="pass"]', password)
            await page.click('button[name="login"]')
            await page.wait_for_load_state('networkidle')

            # Read post texts from the selected folder
            for filename in os.listdir(self.post_text_folder):
                if filename.endswith('.txt'):
                    file_path = os.path.join(self.post_text_folder, filename)
                    with open(file_path, 'r') as file:
                        post_text = file.read().strip()

                    # Create a post
                    await page.click('div[role="button"]:has-text("What\'s on your mind")')
                    await page.click('div[aria-label^="What\'s on your mind"]')
                    await page.keyboard.type(post_text)
                    await page.click('div[aria-label="Post"] span:has-text("Post")')
                    await asyncio.sleep(2)  # Wait a bit before next post

            await context.close()
            await browser.close()

    def start_posting(self):
        email = self.username_input.text()
        password = self.password_input.text()

        if not email or not password:
            QMessageBox.warning(self, "Input Error", "Please enter your email and password.")
            return
        
        if not self.post_text_folder:
            QMessageBox.warning(self, "Folder Error", "Please select a folder containing text files.")
            return

        # Start the posting process
        asyncio.run(self.post_to_facebook(email, password))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FacebookPosterApp()
    window.show()
    sys.exit(app.exec())
