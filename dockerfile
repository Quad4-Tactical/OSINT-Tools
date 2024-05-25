FROM archlinux:latest

WORKDIR /usr/src/app

COPY setup.sh .

RUN pacman -Syu --noconfirm sudo && chmod +x setup.sh

ENTRYPOINT ["./setup.sh"]

CMD ["bash"]