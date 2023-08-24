# Summary
IRIS-FlaskBlog Application is a real-world application that leverages the functionality of Flask web framework, SQLALchemy ORM, and InterSystems IRIS. 
The application contains user registration and authentication with the help of Flask-Login python library, a responsive user interface to create and edit posts.

# Application layout
![main](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/9cd462a5-920f-4d0d-9c8f-604468ca8244)

# Features
* User registration and authentication
* Creation of a data structure with SQLALcemy model classes
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
git clone https://github.com/mwaseem75/IRIS-FlaskBlog.git

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
![image](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/acf3e68b-cf2d-4ce1-9997-b4b648ec845f)

Once registered, the user will log in automatically, To sign out click on the User Name link and then click on Sign out.
In order to log in, click on sign in link
![image](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/047f88dd-db3d-45d3-ba57-d7d83a30e6d8)

#### Create a post
From the home page, click on Create a Post button to create a post. 
Enter the title, Content, and Related Tags and save the post.
![image](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/11734230-c27d-4f87-bf5e-56084ce62e61)


#### View a post (Edit, Delete, Like, or add comments)
Click on the title or on the content of the post in order to Edit or Delete a Post, or Like or add comments to the post.
![ViewPost](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/60c55817-90ef-45bc-9c57-11a9c55f061e)

#### Edit post
In order to modify the Post, click on Edit Post from the view post page 
![editpost](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/dc6febb6-0a32-47ee-96c8-edc50b404fd2)

#### List Posts based on User or Tags
Click on Post User to list down all the posts related to users or click on a Tag to list all the related posts.
![userfeed](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/87e4036b-2bee-4e50-ba78-956a8226c84e)

## Application database
SQLALchemy will create below tables:
* user: To store User information
* post: To store Posts related data
* tags: To store Tags against the post
* tags_association:  To store links between Posts and Tags
* comments: To save post comments by users
* like: To store likes details by users

To view table details, navigate to http://localhost:52775/csp/sys/exp/%25CSP.UI.Portal.SQL.Home.zen?$NAMESPACE=USER#
![image](https://github.com/mwaseem75/IRIS-FlaskBlog/assets/18219467/de303374-af23-40cc-874b-cad560ca1a87)


## Special Thanks to:
Dmitry Maslennikov for sqlalchemy-iris liabrary (An InterSystems IRIS dialect for SQLAlchemy ) which was helpful to connect with IRIS

