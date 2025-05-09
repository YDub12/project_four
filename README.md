# Restaurant Project
This project was built to showcase an interactive restaurant webiste, with a Menu, Booking option and a contact page. 

## Features
- Home, Menu, Contact, and Booking pages
- 15-minute time slot selection
- Automatic 90 minute reservation window enforcement
- Excludes already booked tables in time slot dropdown
- Booking confirmation with success page
- No login required to make a booking
- User dashboard for managing bookings 
- Deployed to Heroku
### Features left to implement
- Email confimation after booking for admin and user
- Google Calendar integration
- Matches tables to guest count dynamically
- Taking tables down 

## Testing 
The website was tested on Google Chrome and Microsoft Edge.

The website was checked on mobile, laptop and desktop.

All features have been continually tested to ensure they work and dynamic additions added while in the process of creating 
On the landing page there is an option to book a table

![Landing booking page](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Booking-link-front-page-1.PNG)

In addition to this there is a navbar across the top of the page

![Login](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Navbar-logged-in.PNG)

![Logout](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Navbar-logged-out.PNG)

The dashboard is only available if logged in and can edit bookings or cancel from there: 

![Dashboard](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Reservations.PNG)

I would like to add styling to the dashboard to bring it in line with the rest of the site. 

The site has a contact form for special requests 

![Contact form](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Contact-form.PNG)

The next step would be to link this up to send an email. It does acknowledge the contact has been made

![Contact](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Contact-submission.PNG)

The booking page allows for you to input your name select the guests, time and date as well as the table you would like to sit on. I would like to add a seating chart so that the front end user would be able to see where the table is located. 

![Reservation form] (https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Reservation-page.PNG)

![Table](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Table-booking.png)

This then takes you through to a confirmation page

![Confirmation](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Reservation-confirmed.PNG)

The table availability should update dynamically, however if it does not there is still logic to prevent people booking at that time

![Booked table] (https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Table-booked-message.PNG)

The Menu opens in a new tab

![Menu](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Menu-open-page.PNG)

## Accessibility
![Lighthouse report](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Accessibility%20report.PNG)

## Bugs
Initial issues that were detected included:
Errors with the Google Maps API - 
[Now resolved](https://raw.githubusercontent.com/YDub12/project_four/refs/heads/main/Readme%20images/Google-maps-link.PNG)
Issues with the booking form and how the data was handled
## Design 
I broke the design and implementation phases down into three parts:

Part 1:
Hand draw the ERDs and do a basic sketch of what I wanted the website to look like, I tried using online resources, but these did not really suit te purpose. 

Part 2:
Implement the initial features into a working version that will be usable

Part 3: 
Improvement on the design to make it more ready for pushing into a live environment and make it more unique

Throughout the development of this restaurant web page, we followed the principles of Agile methodology by breaking down the project into manageable, iterative tasks and delivering functionality incrementally. Starting with core features like table booking, contact forms, and a dynamic menu, we continuously gathered feedback to adapt and improve the application. New features such as user authentication, a personalized dashboard, and dynamic table availability were introduced through short development cycles, allowing for rapid testing and refinement. This process enabled us to remain flexible, prioritize user needs, and ensure a functional, user-centered final product.

Testing was an ongoing and integrated part of the Agile development process for this project. Rather than leaving testing until the end, we adopted a test-as-you-go approach, continuously validating functionality with each feature iteration. Every new component — from the booking system to user authentication and the dashboard — was tested across different devices and browsers, ensuring responsive and reliable performance. Features were released incrementally, allowing for quick feedback, bug identification, and rapid adjustments. This iterative testing cycle aligned closely with Agile principles, ensuring the product evolved flexibly in response to both technical findings and user experience insights. 

## Deployment
1. Log in to Heroku
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Scroll to the top and select "Deploy" tab
7. Select GitHub as deployment method and search for your repository and link them together
8. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
9. Deployed site here [restaurantproject1](https://restaurantproject1-ec477cb615a2.herokuapp.com/)