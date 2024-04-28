# InternshipWebsiteV1

This is the first version of the codebase for the website of a company that I am interning for. The website was created using the Flask package in python, and it uses a MongoDB database for its user authentication system.

This code base is modularized, with the application factory and database code located in the factory.py and db.py files respectively. The authentication system and homepage views located in the user and homepage folders respectively.

Note that the config variables are stored in a local .env file for privacy reasons. Thus some functionality will not work, such as the database as the database URI is not provided.
