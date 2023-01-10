# The Cheese Shop
![Mock up of home]()

[Link to LIVE shop]()

# Table of Contents:

1. Project Goals
2. Project Sprints
3. UX & UI
4. Structure
5. Features
6. Technologies used 
7. Testing
8. Deployment
9. Acknowledgments 


# 1. Project Goals
Build a site for customers to be able to purchase cheese and cheese accesories from. 

# 2. Project Sprints

I used an agile approach to this project by following sprints. The sprints were broken down into issues which were logged on the Github project board. [View here](https://github.com/users/angharadcaswell/projects/1/views/1)

As seen in the image below, I used a kanban board to track the progress of my tickets. 

![Project board](/readmeimages/project_board.png)

## Sprints:
1. Set up Python, database
2. Set up base html/css and create Home app
3. Set up Authorisation for the site
4. Set up Base template
5. Set up home page
6. Create product App and views for filtering and searching. 
7. Create bag app and add CRUD functionality.
8. Build Check out app and Stripe
9. Edit admin panel 
10. Deploy
11. Marketing initative. 


# 3. User Experience

## 3.1 User Stories 

### Customer:


### Shop admin:
 

## 3.2 Wireframes
### Homepage/Desktop :
![Homepage](/readmeimages/Homepage_desktop.png)

## 3.3 Design

### 3.3.1 Colour
I started the colour design for the site with a deep purple to represent the grapes and wine that are so often paired with cheese. I then used [Coolors](https://coolors.co/) to generate a colour pallete based on the deep purple. I particularly liked this set of colours because they are similar to the colour of cheeses and also some other neutral colours. 

I also checked the contrast of the foreground and background colours based on this pallete passed the standards of [WebAIM.](https://webaim.org/resources/contrastchecker/)

![color](readmeimages/colors.png)

### 3.3.2 Logo
I decided upon a very simple logo so customers would know exactly what the site did. It is also a simple design so it can be used with various colors and edited for future marketing if needed. 

![logo](/readmeimages/mobile-logo.png)

### 3.3.3 Font family 

Similar to the colour palette and logo I wanted to keep thing simple with the font so that the design wouldn't distract from the content of the site. 

1. Title: Imprima
2. Body: Inter

# 4. Structure

### Models
![shop Model](/readmeimages/models.png)

### Data Schema



### Site Map
![Site map](/readmeimages/Sitemap.png)

# 5. Features

## 5.1 All features
[Current Features](features.md)

## 5.2 Features to implement:

1. 
2. 


# 6. Technologies used 
* [Python 3.2](https://en.wikipedia.org/wiki/Python_(programming_language)) - Content and structure
* [Heroku](https://id.heroku.com/login) - Host
* [Gitpod](https://www.gitpod.io/) - IDE
* [Github/ Github pages](https://github.com/)- Code repositary
* [Am I responsive?](http://ami.responsivedesign.is/#)- To see display the website as mock ups  
* [Django Alauth](https://django-allauth.readthedocs.io/en/latest/installation.html)- User athentication 
* [Bootstrap4](https://getbootstrap.com/) - UI framework
* [Font Awesome](https://fontawesome.com/) - Free Icons 
* [Figma](https://www.figma.com/) - Wireframes design
* [WebAIM.](https://webaim.org/resources/contrastchecker/) - Check color contrast 
* [Coolors](https://coolors.co/)- To create color palette. 
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - forms
* [Stripe](https://stripe.com/gb) - Payments
* [ElephantSQL](https://www.elephantsql.com/) - Database
* [Psycopg2](https://pypi.org/project/psycopg2/)- Supports connection to DB
* [AWS](https://aws.amazon.com/)- media and static host
* [Bulma](https://bulma.io/)0 line height of Font Awesome icons.
* [Gunicorn](https://gunicorn.org/)- server to run Django on Heroku.


# 7. Testing  
The site was tested in Gitpod terminal and Heroku by users and myself on all browsers. The site was also peer reviewed by the Code Institute community. 

## 7.1 User testing:
I tested the deployed site with several users. I asked each user to complete the following task, tell me how they did it and score it out of 5 for 


[User Stories Tested](userstories.md)

## 7.2 Bugs:
These significant bugs were found during user testing and during the build process. 

### 1. The logo was not showing in the header on any pages of the deployed site
> >#### **FIX**: *I changedthe URL in the base.html template to include the {{ MEDIA_URL }} and delete an additional slash.*     

### 2. A user noticed that the currency was inconsistent across the LIVE site.
> >#### **FIX**: *This was an easy fix, as I just needed to change the currency symbol in a couple of templates*

### 3. When I tested the deployed site on adding a product as an admin user, I recieved an error message.
> >#### **FIX**:  *Back in development, Django gave me an error that "product" did not exist. I needed to assign the variable "product" in the view.*




## 7.3 Code Validation
[Code Validation](codevalidation.md)

## 7.4 Performance testing
[Lighthouse](performance.md)




# 8. Deployment

## Github:

To start the deployment process you need to create a new repository.

1. Log into Github
2. Open [Code Institute's template](https://github.com/Code-Institute-Org/python-essentials-template)
3. Click the "Use This Template", then the "Create new repository" and add repository name.

### Forking:
1. Visit [the_cheese_shop](https://github.com/angharadcaswell/the_cheese_shop) repository.
2. Click the "Fork" button in the top right hand corner.
3. Click the "Create Fork" button

### Clone:
1. Visit [the_cheese_shop](https://github.com/angharadcaswell/the_cheese_shop) repository.
2. Press the arrow on the Code button
3. Copy the link that is shown in the drop-down and select the directory in Gitpod.
4. Use the command'git clone' in the terminal and paste the link you copied.
5. View the requirements.txt file and install all of the packages using the CLI *pip install -r requirements.txt*

## Gmail SMTP:
Gmail SMTP has been used to send order confirmations and user contact emails.
1. To use this configuration, add the following code to your settings.py file.
![email ](/readmeimages/email_setup.png)

## Stripe:
I used Stripe to take test payments on the deployed site. 
1. Create a new Stripe account.
2. Follow the documentation on [how to set up Stripe](https://stripe.com/docs).
3. You can test your checkout app using the following test card details:

| Card number           | MM/YY | CVC | Postcode |
| ----------------------| ----- | ----| ---------|
| 4242 4242 4242 4242   | 42/42 | 424 | 42424    |


## Amazon Web Services (AWS) Storage:
All static and media files are stored with AWS S3.I have created a bucket, user group and user that can access this site and the relevant files.
1. Add the following to your setting.py file:

![AWS](/readmeimages/aws.png)


##


# 9. Credits
- Pxhere: Free images [free image website](https://pxhere.com)
- Stackoverflow: [Stackoverflow](https://stackoverflow.com/)
- Wikipedia: content for product description [Wikipedia](https://en.wikipedia.org/wiki/Main_Page)


## Acknowledgments: 
* [Code Institute](https://codeinstitute.net/) student support, slack community and tutorials. 