FROM node:8
WORKDIR /edge-device
COPY ./package.json .
RUN npm install --only=production
COPY index.js .
CMD node .