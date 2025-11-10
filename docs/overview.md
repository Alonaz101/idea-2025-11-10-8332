# Project Overview

This repository implements a Mood-based Recipe Recommendation System with the following major features:

- **SCRUM-253:** Backend FastAPI application with endpoints for recipes retrieval, mood-based filtering, and health check. Relational database models for Recipe and Mood entities.

- **SCRUM-254:** Frontend single-page application (SPA) using HTML/CSS/JavaScript providing mood input and recipe listing/details views integrated with the backend API.

- **SCRUM-255:** User authentication system with secure registration, login, JWT auth, and favorite recipes management. Password hashing implemented.

- **SCRUM-256:** Advanced mood detection supporting text analysis integrated in backend API. Frontend enhanced for mobile responsiveness and usability.

- **SCRUM-257:** Machine learning microservice for personalized recipe recommendations based on user history. Social sharing features for recipes with privacy considerations.

- **SCRUM-258:** Localization and dietary preference filtering. Multilingual support both frontend and backend. Dietary restrictions integrated in backend data models and API.

This modular architecture ensures scalability, security, and a user-friendly experience across devices, compliant with privacy and internationalization standards.

# Repository Structure

- `backend/` - FastAPI backend application and modules.
- `frontend/` - SPA frontend application files.
- `docs/` - Documentation and project overviews.

# How to Run

- Backend: `uvicorn backend.main:app --reload`
- Frontend: Serve `frontend/index.html` on a web server.

This is an initial commit with core functionalities and will be expanded progressively.
