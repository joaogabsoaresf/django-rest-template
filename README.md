# Django REST Framework SaaS Template

A powerful, scalable, and production-ready Django REST Framework (DRF) template for building SaaS applications. This template includes essential tools and integrations to streamline development, deployment, and monitoring.

## Features

- **Docker** – Containerized development environment for consistency across all stages.
- **Django REST Framework** – Simplifies API development with robust features.
- **DRF Spectacular** – Automatic OpenAPI documentation generation for clear API specs.
- **PostgreSQL** – A reliable, scalable, and performant database solution.
- **RabbitMQ & Redis** – Efficient asynchronous task management and real-time messaging.
- **Resend** – Easy-to-integrate email service for transactional communications.
- **Sentry** – Comprehensive error tracking and performance monitoring to ensure stability.

## Feature Checklist

### Implemented Features:
- [x] Docker support
- [x] Django REST Framework integration
- [x] DRF Spectacular for API documentation
- [x] PostgreSQL as the database
- [x] RabbitMQ & Redis for messaging and task management
- [x] Resend for email service
- [x] Sentry for error tracking and monitoring

### Upcoming Features:
- [ ] User authentication and authorization (JWT, OAuth)
- [ ] Multi-tenancy support
- [ ] Payment integration (Stripe, PayPal)
- [ ] Role-based access control (RBAC)
- [ ] WebSockets for real-time updates
- [ ] Background task processing with Celery
- [ ] API rate limiting and throttling
- [ ] CI/CD pipeline setup
- [ ] Logging and monitoring improvements
- [ ] Automated testing and coverage reports
- [ ] Customizable admin panel
- [ ] Internationalization and localization support
- [ ] Google Cloud Platform (GCP) integrations

## Getting Started

### Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/joaogabsoaresf/django-rest-template.git your-app
   cd your-app
   ```
2. Run the initial configuration script:
    ```sh
    make init-config
    ```

3. Create an `.env` file with the required environment variables based on the example:
    ```sh
    cp dotenv_files/.env-example .env
    ```

4. Build, start services, and run migrations:
   ```sh
   docker-compose up --build
   ```

## Development Scripts
To simplify development, the template includes useful scripts:
- `make db-update` – Create and apply database migrations.
- `make new-app` – Generate a new Django app and register it in settings.

## API Documentation
DRF Spectacular automatically generates OpenAPI documentation. Access it at:
- **Swagger UI**: `http://localhost:8001/api/schema/swagger-ui/`
- **ReDoc**: `http://localhost:8001/api/schema/redoc/`

## Current Project Status
Currently, this application is only set up to run in a local development environment. Future updates will include cloud deployments and production-ready configurations.

## Contributing
We welcome contributions! Feel free to submit issues and pull requests to improve this template.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy coding! 🚀

