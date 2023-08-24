# Summary
IRIS-FlaskBlog Application is a real-world application that leverages Flask web framework, SQLALchemy ORM, and InterSystems IRIS db using Flask, SQLAlchemy, and InterSystems IRIS. User Registration and authentication by using Flask-Login library, Uses SQLALchemy to create data structure and use CRUD (Create, Read, Update, Delete) operations for relevant data entities. Bootstrap to design UI.

# Application layout
![main](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/9cd462a5-920f-4d0d-9c8f-604468ca8244)

# Features
* User registration and authentication
* Auto Create a data structure with SQLALcemy model classes
* Responsive user interface to create, edit, and delete posts
* Like and add comments to the post
* Search based on the user and based on the tags

# Used Technologies
Flask: A micro web framework for Python that allows you to build web applications quickly and efficiently.Conduit
SQLAlchemy: An Object-Relational Mapping (ORM) library that provides a high-level, Pythonic interface for interacting with databases.
InterSystems IRIS: A high-performance, data platform that combines a powerful database with integration, analytics, and AI capabilities.

# Installation
1. Clone/git pull the repo into any local directory

```
git clone https://github.com/mwaseem75/FFFFFFFFFF
```

2. Open a Docker terminal in this directory and run:

```
docker-compose build
```

3. Run the IRIS container:

```
docker-compose up -d 
```
# Getting Started 
## Run the application
To run the application Navigate to http://localhost:4040 
#### Home Page
![image](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/a484538b-1fb7-435c-9254-25f1dc6b8c92)

#### Register a User
To register a user, Click on Sign Up link
![Sign-up](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/cddac1bb-88f7-49a0-ac05-4a31ac8cec7f)

Once registered, the user will log in automatically, To sign Out click on the User Name link and then click on Sign out.
In order to log in, click on Sign in link
![Login](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/ea89e967-b753-4678-938f-18de9c187e7f)

#### Create a post
From the home page, click on Create a Post button to create a post. 
Enter Title, Content, and Related Tags.
![CreatePost](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/b362958a-ac92-4be0-9364-35769f08b775)

#### View a post (Edit, Delete, Like, or add comments)
Click on the title or on the content of the post in order to Edit or Delete a Post, or Like or add comments to the post.
![ViewPost](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/60c55817-90ef-45bc-9c57-11a9c55f061e)

#### Edit post
In order to modify the Post, click on Edit Post from the view post page 
![editpost](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/dc6febb6-0a32-47ee-96c8-edc50b404fd2)

#### List Posts based on User or Tags
Click on Post User to list down all the posts related to users or click on a Tag to list all the related posts.
![userfeed](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/87e4036b-2bee-4e50-ba78-956a8226c84e)











Remember that the scope of this project may vary based on your requirements and available resources. Break down the project into manageable tasks and milestones for easier development and tracking. Additionally, consider seeking guidance from experienced developers or mentors, especially if you are new to any of the technologies involved.

Deliverables:
The application will be available on OEX.
	Documentation, DC article, readme.md and wiki for technical details.
	Video tutorial with application demo and comments about its features.

