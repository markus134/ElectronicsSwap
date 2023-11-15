# Use an official Node.js runtime as a parent image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json /app
COPY package-lock.json /app

# Copy the rest of the application code to the working directory
COPY . /app

# Install project dependencies
RUN npm install

# Expose the port the app will run on
EXPOSE 5173

CMD ["npm", "run", "dev"]
