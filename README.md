# FilesOrganizator

FilesOrganizator is a project developed to automate file organization in a Linux environment (also available for Windows), helping to keep folders and directories well-structured.

## Features

The project includes the following features:

- Automatically organizes files into directories based on their extensions.
- Creates specific folders for each file type (such as documents, images, videos, etc.).
- Handles duplicate file names, ensuring no file is overwritten.
- Allows customization of organization categories and associated file types.
- Logs all operations to track which files were moved and their destinations.
- Flexible and adaptable structure for new file types and configurations.

## Technologies

The project was developed using the following technologies:

- **Python**: Primary programming language for the project.
- **os**: Library for interacting with the file system.
- **shutil**: Used for moving and copying files.
- **logging**: Tool for recording detailed logs of performed operations.
- **Watchdog**: Library for monitoring changes in the Downloads folder, ensuring the code runs only when changes occur.

## Key Learnings

Key takeaways from this project include:

- Using Python's native libraries for file and directory manipulation.
- Creating a script that is efficient and easy to use, even for users with little technical experience.
- Implementing error handling to manage unpredictable scenarios, such as file permissions.
- Logging operations to facilitate process monitoring and debugging.
- Applying Python programming best practices, including modularization and code reuse.

## Conclusion

FilesOrganizator is a valuable tool for anyone looking to automate file organization in Linux systems. The project combines important concepts of automation, file manipulation, and logging, providing an efficient solution for maintaining a clean and organized file system.
