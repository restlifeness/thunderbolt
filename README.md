# Why Thunderbolt ✈ ? 
Because aviation is my _second love_, right after programming. There's something fascinating about airplanes that I can't resist, and I often find myself naming my projects after some truly special models. Allow me to give you a brief rundown on the significance of this particular model I've named my latest project after.
>The Republic P-47 Thunderbolt is a World War II-era fighter aircraft produced by the American company Republic Aviation from 1941 through 1945. It was a successful high-altitude fighter, and it also served as the foremost American fighter-bomber in the ground-attack role.
>
>![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/P47_Thunderbolt_-_Chino_2014_%28cropped%29.jpg/300px-P47_Thunderbolt_-_Chino_2014_%28cropped%29.jpg)

# 🔎 Project Overview
The fundamental concept of our project is not novel, yet it's quite simple and effective - we aim to merge a discussion forum and a shop into one seamless platform. This fusion creates a unique environment where users can pose questions or seek advice on various topics. However, for more complex issues or scenarios requiring specific professional expertise, users have the ability to engage directly with industry professionals. These experts, in exchange for their services, would receive a mutually agreed-upon fee. In this way, we create an ecosystem that balances the free exchange of information with the availability of paid professional consultancy.

# 💾 Current state of the project

This project was originally created as a test task. Many features were implemented more to showcase potential, rather than for full-fledged functionality. The current version is an MVP (Minimum Viable Product) v0.0.1.

## June 2023 update
- Created core-endpoints
- Laid the groundwork for the forum
- Established the foundation for the store
- Payment system has been created and implemented

## June 2023 todo's
- Payment system
- Testing
- Group system

# ⚙️ Stack
### Core
- FastAPI
- SQLAlchemy
- Alembic

### Tests
- pytest

### Database
- Postgres
- Redis (future)

### Deployment
- Docker
- docker-compose
- Makefile

# ▶️ Quick start

1. Clone repo
  ```bash
  git clone https://github.com/djentelmen/thunderbolt.git
  ```
2. __FOR WINDOWS:__ Install and run [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) 
3. Install and run [Docker Desktop](https://www.docker.com/products/docker-desktop/)
4. Run migrations
```bash
make migrate
```
5. Run application
```bash
make start
```
