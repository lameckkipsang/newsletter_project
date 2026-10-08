# Chronicle Courier - Django Newsletter Subscription App

A full-stack Django web application that enables users to subscribe to a newsletter via email. The application validates input, prevents duplicate subscriptions, securely manages environment variables using `python-decouple`, and automatically sends confirmation emails using Django's standard SMTP configuration.

---

## Key Features

- **Subscriber Management:** Captures unique email addresses and subscription timestamps.
- **Form Validation:** Enforces correct email syntax and prevents duplicate database entries.
- **Automated SMTP Confirmation:** Sends welcome emails upon successful submission.
- **Environment Security:** Isolates secret keys and email credentials via a `.env` file.
- **Modern User Interface:** Fully responsive subscription card built with Tailwind CSS.

---

## Tech Stack

- **Framework:** Django 6.1
- **Language:** Python 3.10+
- **Database:** SQLite3
- **Frontend Styling:** Tailwind CSS (via CDN)

---

## Project Structure

```text
chronicle_courier/
├── newsletter_app/
│   ├── admin.py          
│   ├── forms.py          
│   ├── models.py         
│   ├── urls.py           
│   └── views.py          
├── newsletter_project/
│   ├── settings.py       
│   └── urls.py           
├── templates/
│   └── subscribe.html                    
├── .gitignore            
├── manage.py             
└── requirements.txt