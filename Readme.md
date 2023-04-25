Pricing Module
The Pricing Module is a web application that provides a configurable pricing module for managing product/service prices. It is built using the Django web framework and supports differential pricing based on the distance traveled and total ride time.

Getting Started
To get started with the Pricing Module, follow these steps:

Clone the GitHub repository to your local machine:
bash
Copy code
git clone https://github.com/your_username/pricing-module.git
Install the required Python dependencies using pip:
Copy code
pip install -r requirements.txt
Run the Django development server:
Copy code
python manage.py runserver
Open your web browser and navigate to http://localhost:8000/admin to access the Django admin interface.
Usage
The Pricing Module provides an admin interface for managing pricing configurations, including the ability to enable/disable different configurations as needed.

To add a new pricing configuration, follow these steps:

Log in to the Django admin interface using your credentials.

Navigate to the Pricing Configuration section and click the "Add" button.

Enter the configuration details, including the Distance Base Price (DBP), Distance Additional Price (DAP), and Time Multiplier Factor (TMF).

Click the "Save" button to create the new pricing configuration.

Once you have created one or more pricing configurations, you can use the Pricing Module API to calculate the final price of a ride based on the distance traveled and total ride time. To use the API, send a GET request to the following URL:

perl
Copy code
http://localhost:8000/api/price?distance=<distance>&time=<time>
Replace <distance> with the distance traveled in kilometers, and <time> with the total ride time in minutes. The API will return a JSON object containing the calculated price based on the active pricing configuration.

Testing
The Pricing Module includes a set of unit tests to ensure that the pricing calculations are accurate and the API functions correctly. To run the tests, use the following command:

bash
Copy code
python manage.py test
License
The Pricing Module is open-source software licensed under the MIT license. Feel free to use, modify, and distribute the software as needed.