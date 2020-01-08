FROM archlinux
COPY backend app
WORKDIR app
RUN pacman -Syu --noconfirm &&\
    pacman -S --noconfirm python-pip &&\ 
    pip install poetry &&\
    poetry install &&\
    pip install Flask
EXPOSE 5000
ENV FLASK_APP=backend/services.py
RUN pwd
RUN ls
ENTRYPOINT [ "flask","run","--host=0.0.0.0" ]
