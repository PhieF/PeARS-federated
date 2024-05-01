FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Additionally, install Gunicorn
RUN pip install gunicorn

RUN flask db init

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable (example placeholder values, replace them as needed)
ENV PEARS_LANGS=en
ENV TRANSLATION_DIR=/app/translations

ENV MAIL_DEFAULT_SENDER=your-email@example.com
ENV EMAIL_USER=your-email@example.com
ENV MAIL_SERVER=smtp.example.com
ENV MAIL_PORT=587
ENV EMAIL_PASSWORD=your-email-password

ENV SECRET_KEY=your-secret-key
ENV SECURITY_PASSWORD_SALT=your-security-password-salt

ENV SITENAME="Cool PeARS pod"
ENV SITE_TOPIC="Cool topic of my cool PeARS pod"
ENV SEARCH_PLACEHOLDER="Search example: Books, Articles"

# Run the application using Gunicorn
# Adjust the number of workers and threads as needed
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "3", "-t", "120", "app:app"]

