<p align="right">
  <img style="width: 200px; margin: 16px; margin-bottom: 0;" src="docs/exxeta_logo_positiv_RGB.svg" alt="Exxeta Logo">
</p>

# Sustainability Companion app 🌱 👣


###### TODO

- [x] Finish up api paths for:
    - [x] Creating / Deleting User
    - [x] Deleting Trip
    - [x] Updating Trip
- [ ] Calculate CO2 emissions through external / internal API
    - [ ] Add routing information (distances, etc.) via external API
    - [x] Add static values for CO2 emissions for each vehicle type via internal API
- [x] Use Azure PostgreSQL database
- [ ] Deploy App in Azure
- [ ] Add more features to the app

# TOC

- [What is the Sustainability Companion app?](#what-is-the-sustainability-companion-app)
- [How to use the app](#how-to-use-the-app)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [How to run the app locally](#how-to-run-the-app-locally)
- [Local Development](#local-development)
- [Deployment to Azure](#deployment-to-azure)
- [Possible Features Ideas](#possible-features-ideas)

---

## What is the Sustainability Companion app?

The Sustainability Companion app is a web application that helps users to track their CO2 emissions while traveling. The
app allows users to create trips and calculate the CO2 emissions for each trip. The app also provides
information about the CO2 emissions for each vehicle type.

## How to use the app

The project is split into two main parts: the companion app and the carbon footprint API. The project was developed in
Django and uses Django Rest Framework for the API. The companion app is a web application that allows users to create
trips and calculates the CO2 emissions for each trip. The carbon footprint API is a (for now) simple API that provides
information about the CO2 emissions for a give trip.

## Project Structure

```shell
$ tree --gitignore -L 2
```

```
.
├── carbon                    # Django app for the carbon footprint API #
│   ├── carbon_calculator.py
│   ├── urls.py
│   ├── vehicle_enum.py
│   └── views.py
├── companion                 # Django app for the companion app #
│   ├── Application
│   ├── domain
│   ├── infrastructure
│   └── presentation
├── Dockerfile
├── docs
│   ├── enititaeten.svg
│   └── sc-be-qs-xx.yaml      # OpenAPI / Swagger spec for the API #
├── README.md
├── requirements.txt
└── sc_be_qs_xx
    ├── settings.py           # Django settings for the project #
    └── urls.py
```

## API Endpoints

The OpenAPI / Swagger spec for the API can be found in the `/docs/` folder.
If you're using Intellij you can test the endpoint with the given `*.http` file in the `/test/` folder.

## Local Development

1. Have PyCharm and Python 3.10 installed
2. Clone the repository and open it in PyCharm
3. Create a virtual environment, if you don't have one already (PyCharm should create one)
4. Install the dependencies with `pip install -r requirements.txt`
5. Run the migrations with `python manage.py migrate`
6. Run the server with `python manage.py runserver`
7. Access the app at `http://localhost:8000`

## Deployment to Azure

Deployment to Azure:
> https://medium.com/@DawlysD/deploying-django-apps-with-postgresql-on-azure-app-services-from-scratch-fe4a10db5e7c

Django settings for production:
> https://stackoverflow.com/questions/1626326/how-to-manage-local-vs-production-settings-in-django

## Possible Features Ideas

These are up to you :)
