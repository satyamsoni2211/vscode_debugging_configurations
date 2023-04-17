FROM node:16
RUN useradd -ms /bin/bash -d /home/demo demo
USER demo
WORKDIR /home/demo
COPY --chown=demo:demo package.json .
RUN npm install
COPY --chown=demo:demo . .
EXPOSE 3000
CMD ["npm", "start"]