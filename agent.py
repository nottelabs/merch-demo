# pip install notte-sdk
from notte_sdk import NotteClient
from loguru import logger

# Initialize the notte sdk client
client = NotteClient(api_key="sk-notte-6a0cf6fbeaec6800d882de6c1e2f2966d7b098dbf7ae56fb21785f24f378581a")

# Personal information for shipping
name = "<your-name>"
email = "<your-email>"
address = "<your-address>"
phone = "<your-phonenumber>"
country = "United States"

# Secure vault for the credit card details
vault = client.Vault("94f42a8f-fd88-4143-991b-9078280230b1")
# Launch the session & the agent
with client.Session(browser_type="firefox") as session:
    agent = client.Agent(
        session=session,
        vault=vault,
        max_steps=20,
    )
    # should take a few minutes to complete
    response = agent.run(
        url="https://shop.notte.cc",
        task=f"""
1. Go to https://shop.notte.cc and wait for the page to fully load
2. Go to the product page for the cap
3. Add the item to the cart
4. Go to the checkout page
5. Fill the shipping "Email" field with: {email} (don't try to login, just fill this specific email)
6. Select {country} from the country dropdown
7. Fill the shipping "Full Name" field with: {name}
8. Fill the shipping "Street address" field with: {address}
9. Choose the right combobox option for the address. Choosing the right one is important and will fill the remaining fields automatically (i.e state, city, postal code, country). Never use the `fill` action to fill any fields.
10. Scroll down 2x to the payment section
11. Fill in the credit card details using the provided values
12. Click on the "Complete Order" button. 
""")
    if response.success:
        logger.info(f"✅ Order placed successfully. Check your email for the order confirmation.")
    else:
        logger.error(f"❌ Order failed with the following error: {response.answer}")