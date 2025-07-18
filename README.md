
# Auth-Domain 🔑 - Microservices for User Authentication

## 📦 Project Overview

**Auth-Domain** is a set of microservices built using **Python** and **SQL Server** designed to manage user authentication within an application. This repository includes services for handling login functionality for both **root** and **normal users**, as well as user registration. These microservices provide secure access and authentication for users of the platform.

### 🚀 Main Features:
- **Login Root**: Provides authentication for root-level users.
- **Login**: Handles authentication for normal users.
- **Register**: Allows new users to register an account in the system.

## 🔧 Technologies Used

- **Python** 🐍: The primary programming language used for building these microservices.
- **Flask** 🖥️: A lightweight web framework for building APIs.
- **SQL Server** 🛢️: A relational database management system used to store user credentials and authentication data.
- **Docker** 🐳: Containerization for easy deployment and portability.

## 🔍 Folder Structure

Here’s a breakdown of the folder structure in the **Auth-Domain** repository:

```
Auth-Domain/
├── .github/workflows/  - GitHub Actions workflows for CI/CD 🚀
├── Login-Root/         - Microservice for root-level user authentication 🔑
├── Login/              - Microservice for normal user authentication 🔐
├── Register/           - Microservice for user registration ✍️
├── README.md           - This file 📄
```

- **Login-Root/**: Contains the logic for authenticating root-level users.
- **Login/**: Contains the logic for normal user authentication.
- **Register/**: Contains the logic for registering new users in the system.
- **.github/workflows/**: Contains GitHub Actions for CI/CD automation.

## 🎯 Purpose of the Project

The **Auth-Domain** microservices handle user authentication, providing secure access to the system. The purpose of these services is to:
- **Authenticate root users** for administrative tasks.
- **Authenticate normal users** for accessing general features of the platform.
- **Allow new users** to register and create accounts in the system.

## ⚙️ Architecture & Design Pattern

- **Architecture**: The services follow a **RESTful architecture** for communication between the client and the server. Each service exposes HTTP endpoints for user authentication and registration.
- **Design Pattern**: These services follow the **Microservices Design Pattern**, which allows them to operate independently, making it easier to scale, maintain, and update each service.

## 🚀 How It Works

1. **Login Root**: The `POST` request to the `/login-root` endpoint authenticates root-level users based on their credentials. The service checks the credentials against the database and grants access if they match.
2. **Login**: The `POST` request to the `/login` endpoint authenticates normal users based on their credentials.
3. **Register**: The `POST` request to the `/register` endpoint allows new users to create an account by providing their username, email, and password.

## 🌟 Future Enhancements

- **Two-Factor Authentication**: Add an additional layer of security for user authentication with 2FA.
- **Password Reset**: Allow users to reset their password if forgotten.
- **OAuth Integration**: Implement third-party login options using OAuth for Google, Facebook, etc.

## 💬 Contact Information
For any questions or contributions, feel free to reach out to me through my GitHub profile!

Happy coding! 👨‍💻👩‍💻
