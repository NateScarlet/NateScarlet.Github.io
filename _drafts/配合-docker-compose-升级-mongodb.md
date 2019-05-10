---
layout: post
title: 配合 Docker Compose 升级 MongoDB
---

最近 [Rocket.Chat] 发布了 1.0 版本

我升级时看到当时 compose 文件里用的 MongoDB 还是 3.2 版本

就研究了下怎么升级 MongoDB 版本

docker-compose.yml

```yml
version: '2.4'

services:
  app:
    image: rocket.chat:1
    restart: unless-stopped
    mem_limit: 1000000000
    volumes:
      - ./uploads:/app/uploads
    environment:
      - ROOT_URL=https://chat.example.com
      - MONGO_URL=mongodb://mongo:27017/rocketchat
      - MONGO_OPLOG_URL=mongodb://mongo:27017/local
    depends_on:
      - mongo
    labels:
      traefik.docker.network: traefik_default
      traefik.backend: rocket-chat
      traefik.frontend.rule: Host:chat.example.com
    networks:
      - default
      - traefik_default
  mongo:
    image: mongo:3.2
    restart: unless-stopped
    volumes:
      - ./data/db:/data/db
    command: mongod --smallfiles --oplogSize 128 --replSet rs0 --storageEngine=mmapv1
  mongo-init-replica:
    image: mongo:3.2
    command: >-
      bash -c 'for i in `seq 1 30`;
      do mongo mongo/rocketchat --eval "
      rs.initiate({
         _id: ''rs0'',
         members: [ { _id: 0, host: ''localhost:27017'' } ] })" &&
      s=$$? && break || s=$$?; echo "Tried $$i times. Waiting 5 secs...";
      sleep 5; done; (exit $$s)'
    depends_on:
      - mongo
networks:
  traefik_default:
    external: true
```
