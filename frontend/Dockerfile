FROM node:10-alpine

WORKDIR /frontend

COPY . /frontend

RUN yarn install

EXPOSE 3000

RUN yarn build 
RUN yarn global add serve

CMD [ "serve", "-s", "build" ]