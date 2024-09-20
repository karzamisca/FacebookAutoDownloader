import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,  # Set to True if you want to run headless
            args=[
                '--disable-dev-shm-usage',  # Avoid issues with limited shared memory
                '--no-sandbox'  # Disabling sandbox for compatibility
            ]
        )
        
        # Create a new context with a custom user-agent
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.73 Safari/537.36'
        )
        
        # Set the default timeout to 100000 milliseconds
        context.set_default_timeout(100000)

        # Open a new page and navigate to Facebook
        page = await context.new_page()
        await page.goto('https://www.facebook.com')

        # Click on the "What's on your mind" button
        await page.click('div[role="button"] span:has-text("What\'s on your mind, Quân?")')

        # Click on the contenteditable textbox
        await page.click('div[aria-label="What\'s on your mind, Quân?"]')

        # Input post text
        post_text = "I am the best!"
        await page.keyboard.type(post_text)

        # Click "Next" button
        await page.click('div[aria-label="Next"] span:has-text("Next")')

        # Click the "Post" button
        await page.click('div[aria-label="Post"] span:has-text("Post")')

        # Optional: Wait for a bit before closing
        await asyncio.sleep(5)

        # Close the context and browser
        await context.close()
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
