import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/UMA/Downloads/supermarket_sales - Sheet1.csv")
df
# Calculate the total gross income for each city
city_gross_income = df.groupby('City')['gross income'].sum()

# Create a pie chart
plt.figure(figsize=(5, 5))  # Set the figure size (width, height) in inches

# Create the pie chart
plt.pie(city_gross_income, labels=city_gross_income.index, autopct="%1.1f%%", startangle=45)#The labels parameter sets the labels for each segment based on the city names, autopct specifies the format of the percentage labels, and startangle rotates the pie chart to start at 45 degrees.

# Set the title of the pie chart
plt.title('Gross Income Distribution by City')

# Add a legend based on the city names
plt.legend(city_gross_income.index, title='City', loc='upper right')

# Show the pie chart
plt.show()



#Find the most popular payment method used by the customer
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']#Defines a list of custom colors that will be used for the bars in the bar chart.

value_counts = df['Payment'].value_counts()#Calculates the value counts for the 'Payment' column and stores the result in the value_counts variable.
ax = value_counts.plot(kind="bar", color=colors)# Creates the bar chart with custom colors and assigns the Axes object to the variable ax.

plt.title('Payment Method Distribution')# Sets the title of the chart to 'Payment Method Distribution'.

for i, v in enumerate(value_counts):#Iterates through the value counts using enumerate, where i is the index and v is the count for each category.
    ax.text(i, v, str(v), ha='center', va='bottom')#Adds the count v as text on top of each bar at position (i, v). It's centered horizontally (ha='center') and positioned slightly above the top of the bar (va='bottom').

plt.show()#Displays the bar chart with the count labels on top of each bar.



#Monthly Sales by product category

# Create a new 'Month' column by formatting the 'Date' column
df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%b %Y')

# Get unique product categories
product_categories = df['Product line'].unique()

# Create a multiline chart to visualize sales for each product category by month
plt.figure(figsize=(6, 4))  # Set the figure size (width, height) in inches

# Plot separate lines for each product category
for category in product_categories:
    # Filter data for the current category
    category_data = df[df['Product line'] == category]
    
    # Group the data by 'Month' and sum the 'Total' column
    monthly_sales = category_data.groupby('Month')['Total'].sum()
    
    # Plot the line for the current category with markers
    plt.plot(monthly_sales.index, monthly_sales.values, label=category, marker='o')

# Customize the plot
plt.title('Monthly Sales by Product Category')  # Set the title of the chart
plt.xlabel('Month')  # Label for the x-axis
plt.ylabel('Total Sales')  # Label for the y-axis
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend()  # Display the legend for product categories

# Show the plot
plt.show()


# Define a list of custom colors for the bars
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta']

# Group the data by 'Product line', sum the 'Quantity', and create a bar chart
(df.groupby('Product line').sum()['Quantity']).plot(kind='bar', color=colors)

# Set the title of the bar chart
plt.title('Total Quantity by Product Line')

# Set labels for the x and y axes
plt.xlabel('Product Line')
plt.ylabel('Total Quantity')

# Show the bar chart
plt.show()