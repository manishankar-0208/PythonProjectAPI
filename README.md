# Assignment 3 — GitHub & Wikipedia API Demonstration

**Author:** ManiShakar Reddy Ramapuram  
**Course:** CP1404/CP5632  
**Date Started:** 14/11/2025  

---

## Overview

This project demonstrates how to interact with two REST APIs using Python:  

1. **GitHub REST API**  
   - Fetches user profile details  
   - Lists the user’s repositories  
   - Searches repositories by a keyword  

2. **Wikipedia REST API**  
   - Fetches a summary of any topic  
   - Provides a description and link to the full article  

The programs show how to send HTTP requests, parse JSON responses, and display information in a clean and readable format.

---

## What APIs Are

**API (Application Programming Interface)** is a set of rules and protocols that lets different software systems communicate with each other.  
- An API defines how applications request services and exchange data, acting as a clear contract between a client (your program) and a server (e.g., GitHub or Wikipedia).  

**REST APIs**  
- Both GitHub and Wikipedia use **REST APIs**, which rely on standard HTTP methods like GET to fetch data.  
- Responses are usually returned in **JSON format**, which Python can parse easily.  

**Endpoints**  
- APIs are organized into **endpoints**, which are URLs pointing to specific resources.  
- Examples:  
  - GitHub:  
    - `/users/{username}` → fetch user profile  
    - `/users/{username}/repos` → fetch user repositories  
    - `/search/repositories?q={keyword}` → search repositories  
  - Wikipedia:  
    - `/page/summary/{topic}` → fetch topic summary  

**HTTP Status Codes**  
- When a request is sent, the server responds with a **status code** indicating success or failure:  
  - `200 OK` → Request succeeded  
  - `404 Not Found` → Resource does not exist (e.g., invalid username or topic)  
  - `403 Forbidden` → Access denied (e.g., missing or blocked User-Agent)  
  - `500 Internal Server Error` → Server encountered an error  

> Including error handling in your Python program ensures the application responds gracefully when an API request fails.

**Use API Documentation Links**
1. [GitHub REST API documentation](https://docs.github.com/en/rest?apiVersion=2022-11-28)
