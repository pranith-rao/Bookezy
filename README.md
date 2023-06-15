# Bookezy
Welcome to Bookezy our railway reservation website, where booking train tickets has never been easier. Our platform offers a simple and efficient way for users to book tickets online, while also providing station masters with the tools they need to effectively manage their stations. With the added capability for admins to easily add new stations and station masters, our website offers a comprehensive solution for all your railway reservation needs. This project was built for a hackathon named Bhilai Hacks by our team named Entity💪

To have a glimpse of how this website works watch this https://youtu.be/NohdC1GSJNA

## Live Link
~~Click on this URL https://bookezy.herokuapp.com/ and let me know how it is. Cheers!~~  
Since Heroku took down the free hosting service, the site is no longer hosted anywhere.

## Steps to run the application
1. Clone this repo into your local machine and open it using VS code or any other editor of your choice.
2. Open the terminal and create a virtual environment using the command "python -m venv yourenvname".
3. Activate the virtual env created using the command "yourenvname\Scripts\activate".
4. Once activated, install all the packages using the command "pip install -r requirements.txt".
5. Once all packages are installed you are ready to run the application. Type 'py app.py' in the terminal and hit enter.
6. A link like http://127.0.0.1:9876/ will pop up in the terminal. Press Ctrl and click on the link to open it in the browser to see the landing page of the application.
7. Note! Since we are using SQLite for database management you need to uncomment line 142 in app.py the first time you run the command "py app.py" so that the tables are created. Comment the line once the tables are created so that new tables are not created again and again whenever you perform an action.

## Mail Auth and Google Auth
To set up the app password for the Gmail ID you will be used for sending emails:
1. Enable 2-factor authentication on your mail ID.
2. Go to this website https://myaccount.google.com/apppasswords
3. Select Other (Custom Name) from the Select App dropdown list and give it a name and click on Generate.
4. Copy the generated password and paste it on line 37 and the mail ID on lines 21 and 37.
5. Yea! You are all set to send alerts using the mailing services.

To set up Google Auth for user registration and login:
1. Go to this website https://console.cloud.google.com/ and log in with your Gmail credentials.
2. On the top bar click on "Create New Project" name it and click on Create.
3. Inside the project dashboard click on APIs & Services and go to the Credentials tab.
4. On the top bar click on Create credentials and select OAuth Client ID.
5. Click on Configure the consent screen and select the External option and click on Create.
6. Fill in the App name, User support email, and Developer contact information and click save and continue x 3 and back to the dashboard.
7. Now like Create credentials again and select OAuth Client ID. Select the application type as the desktop app and click Create.
8. Copy the generated Client ID and secret and paste it on lines 48 & 49 respectively.
9. Done! Now you can use Google auth to register and log in.

## Operations that can be performed
### Main Admin
1. Credentials for the main admin are hard coded. Use 'mainadmin@gmail.com' and 'entity123' as credentials to log in.
2. Add stations and notify the station admin via email.
3. View the list of stations added.

### Station admin
1. Has to use his/her email and phone number as the password for the first login.
2. Change their password.
3. Update his/her Profile.
4. Add trains starting from their respective stations and view the list of the trains added.
5. Schedule the trains for different dates and view the list of scheduled trains.
6. View the reservation requests of users and accept or reject them and inform them via email regarding the action taken.
7. Recover their password by using the forgot password on the station admin login page.

### Users
1. Register and log in using Google Auth or fill out the form.
2. Update their profile as the Google auth doesn't return their phone number and address.
3. Change their password if needed.
4. View the list of available trains.
5. Book tickets if the train is available to their preferred location on their preferred date and receive booking notification via email.
6. Reserve tickets if the train is not available to their preferred location on their preferred date and receive reservation update notifications via email.
7. View their booking history and cancel tickets only before 24 hours of their travel time.
8. Status of their reservation.
9. Recover their password by using the forgot password on the login page.

## Snapshots
### Home Page
![1](https://github.com/pranith-rao/Bookezy/assets/65860350/e63a0ef4-0f8b-4b6f-970e-d175000df32a)
![2](https://github.com/pranith-rao/Bookezy/assets/65860350/094bbbc8-66e6-42bd-8a63-39637bd8f6d2)

### Main Admin Login
![3](https://github.com/pranith-rao/Bookezy/assets/65860350/69eaea2a-3bd6-4fb9-8d11-57d7eae71ef4)

### Main Admin Dashboard
![4](https://github.com/pranith-rao/Bookezy/assets/65860350/07e909c5-9841-41f4-b249-d0385f7dd0c8)

### Add Station & Station Admin Details
![5](https://github.com/pranith-rao/Bookezy/assets/65860350/81cb50b7-1a5b-49bb-a662-372bc5d9dcaf)

### Added Stations List
![6](https://github.com/pranith-rao/Bookezy/assets/65860350/a6f14dc3-0bec-458b-9cd2-f41d129df98c)

### Mail Confirmation
![7](https://github.com/pranith-rao/Bookezy/assets/65860350/46ff2afb-0acd-44f4-9b54-d54218413f87)

### Station Admin Login
![8](https://github.com/pranith-rao/Bookezy/assets/65860350/36abf580-5202-4300-a36d-f689a9b0fd98)

### Station Admin Dashboard
![9](https://github.com/pranith-rao/Bookezy/assets/65860350/82c0a244-98b9-405c-a05d-5cda7de4073c)

### Profile Update Page
![10](https://github.com/pranith-rao/Bookezy/assets/65860350/d027d5c0-e744-4e2e-acf3-84015e214662)

### Add Trains
![11](https://github.com/pranith-rao/Bookezy/assets/65860350/d7101389-394f-4aff-8167-160344a8e483)

### Added Trains List
![12](https://github.com/pranith-rao/Bookezy/assets/65860350/c20b8f3f-0087-4783-bc85-962c018c8ee6)

### Schedule Trains
![13](https://github.com/pranith-rao/Bookezy/assets/65860350/259358ea-1d05-46a3-9617-662e805f53f3)

### Scheduled Trains List
![14](https://github.com/pranith-rao/Bookezy/assets/65860350/d0e16e64-8969-4591-8591-89d00716bbcf)

### Reservation Requests List
![15](https://github.com/pranith-rao/Bookezy/assets/65860350/39f5c39e-057f-45eb-8526-7901e1576efc)

### Change Password
![16](https://github.com/pranith-rao/Bookezy/assets/65860350/bd4c0900-6ab6-4db8-9589-d8612fdd2bc4)

### Password Recovery
![17](https://github.com/pranith-rao/Bookezy/assets/65860350/201f0af1-2786-49c2-9eda-1cdc7e6bf121)

### OTP Mail
![18](https://github.com/pranith-rao/Bookezy/assets/65860350/f1c2db9b-e346-495c-a1e3-041c255bedef)

### New Password with Validation Check
![20](https://github.com/pranith-rao/Bookezy/assets/65860350/d19da4a2-205e-4bdf-a49f-f9713555b450)

### User Registration
![21](https://github.com/pranith-rao/Bookezy/assets/65860350/2838a6d0-6862-4d37-94ae-183478057b45)

### Google Auth Page
![22](https://github.com/pranith-rao/Bookezy/assets/65860350/7ea27a80-076a-4fe8-9379-825cd20d3fe2)

### Updating the random phone number and address
![23](https://github.com/pranith-rao/Bookezy/assets/65860350/3b73cb81-881f-4a8c-8f49-0937c3de6a16)

### User Login Page
![24](https://github.com/pranith-rao/Bookezy/assets/65860350/715f46a3-94e8-402d-ae13-8fddb31a39a4)

### User Dashboard
![25](https://github.com/pranith-rao/Bookezy/assets/65860350/32fa9a1b-ca29-49bb-b151-dcfd3d42e2de)

### User Profile Update
![26](https://github.com/pranith-rao/Bookezy/assets/65860350/c3a1dad4-e695-497e-84a9-49217b9c5e16)

### List of Available Trains
![27](https://github.com/pranith-rao/Bookezy/assets/65860350/49bc02ba-5dae-4dfe-b178-eac58a633e02)

### Book Tickets
![28](https://github.com/pranith-rao/Bookezy/assets/65860350/894519da-18b9-450c-bc4a-fa0a4dac75ef)

### Booking Confirmation Mail
![29](https://github.com/pranith-rao/Bookezy/assets/65860350/9272e26e-0519-4541-ac37-67f0158bcde8)

### Reserve Tickets
![30](https://github.com/pranith-rao/Bookezy/assets/65860350/489051cb-c5c3-42d5-9289-c3cb35fc369e)

### Reservation Request Mail
![31](https://github.com/pranith-rao/Bookezy/assets/65860350/49b60a42-94d9-4b63-8bb4-d15467b172fa)

### Check for Reservation Status
![32](https://github.com/pranith-rao/Bookezy/assets/65860350/e885a726-d6b4-4abb-ba0d-1dc6d1cd4f85)

### Mail for Reservation Confirmation
![33](https://github.com/pranith-rao/Bookezy/assets/65860350/b01b9dae-d41f-4ba1-a627-1addb906d773)

### Reservation Confirmation
![34](https://github.com/pranith-rao/Bookezy/assets/65860350/782b05bd-9ff2-476f-8ca0-96c780ce4a81)

### Booking History & Cancellation
![35](https://github.com/pranith-rao/Bookezy/assets/65860350/05216317-5c30-4a0a-ba57-864f538b7a5d)
